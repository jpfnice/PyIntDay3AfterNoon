import subprocess

# To run an external command without interacting with it (<=> os.system())

# Simple command
subprocess.call(['ls', '-a', '/bin/*.c'], shell=True)

# Command with shell expansion
subprocess.call('echo %PATH%', shell=True)

# Capturing Output
output = subprocess.check_output(['ls', '-l'])
print('Have {} bytes in output'.format(len(output)))
print(output)

# To prevent error messages from commands run through check_output() from being written to the console, 
# set the stderr parameter to the constant STDOUT.

output = subprocess.check_output(
    'echo to stdout; echo to stderr 1>&2; exit 1',
    shell=True,
    stderr=subprocess.STDOUT,
    )
print('Have {} bytes in output'.format(len(output)))
print(output)

# To run a process and read all of its output, set the stdout value to PIPE 
# and call communicate().

print('\nread:')
proc = subprocess.Popen(['echo', '"to stdout"'], 
                        stdout=subprocess.PIPE,
                        )
stdout_value = proc.communicate()[0]
print('\tstdout:', repr(stdout_value))

#To set up a pipe to allow the calling program to write data to it, set stdin to PIPE.

print('\nwrite:')
proc = subprocess.Popen(['cat', '-'],
                        stdin=subprocess.PIPE,
                        )
proc.communicate('\tstdin: to stdin\n')

# To set up the Popen instance for reading and writing, use a combination of the previous techniques.

print('\npopen2:')

proc = subprocess.Popen(['cat', '-'],
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        )
stdout_value = proc.communicate('through stdin to stdout')[0]
print('\tpass through:', repr(stdout_value))

print('\npopen3:')
proc = subprocess.Popen('cat -; echo "to stderr" 1>&2',
                        shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        )
stdout_value, stderr_value = proc.communicate('through stdin to stdout')
print('\tpass through:', repr(stdout_value))
print('\tstderr      :', repr(stderr_value))

# To direct the error output from the process to its standard output channel, use STDOUT for stderr instead of PIPE.

print('\npopen4:')
proc = subprocess.Popen('cat -; echo "to stderr" 1>&2',
                        shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT,
                        )
stdout_value, stderr_value = proc.communicate('through stdin to stdout\n')
print('\tcombined output:', repr(stdout_value))
print('\tstderr value   :', repr(stderr_value))

# Multiple commands can be connected into a pipeline, similar to the way the Unix shell works:
#  cat index.rst | grep ".. include" | cut -f 3 -d: 


cat = subprocess.Popen(['cat', 'index.rst'], 
                        stdout=subprocess.PIPE,
                        )

grep = subprocess.Popen(['grep', '.. include::'],
                        stdin=cat.stdout,
                        stdout=subprocess.PIPE,
                        )

cut = subprocess.Popen(['cut', '-f', '3', '-d:'],
                        stdin=grep.stdout,
                        stdout=subprocess.PIPE,
                        )

end_of_pipe = cut.stdout

print('Included files:')
for line in end_of_pipe:
    print('\t', line.strip())
    
# Interacting with Another Command
# The communicate() method reads all of the output and waits for child process to exit before returning. 
# It is also possible to write to and read from the individual pipe handles used by the Popen instance. 
# A simple echo program that reads from standard input and writes to standard output illustrates this:

import sys

sys.stderr.write('repeater.py: starting\n')
sys.stderr.flush()

while True:
    next_line = sys.stdin.readline()
    if not next_line:
        break
    sys.stdout.write(next_line)
    sys.stdout.flush()

sys.stderr.write('repeater.py: exiting\n')
sys.stderr.flush()


print('One line at a time:')
proc = subprocess.Popen('python repeater.py', 
                        shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        )
for i in range(10):
    proc.stdin.write('%d\n' % i)
    output = proc.stdout.readline()
    print(output.rstrip())
    
remainder = proc.communicate()[0]
print(remainder)

print
print('All output at once:')
proc = subprocess.Popen('python repeater.py', 
                        shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        )
for i in range(10):
    proc.stdin.write('%d\n' % i)

output = proc.communicate()[0]
print(output)
