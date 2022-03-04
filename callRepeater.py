import subprocess

print('One line at a time:')
proc = subprocess.Popen('python repeater.py', 
                        shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        )
for i in range(10):
    proc.stdin.write(f'line {i}\n'.encode())
    proc.stdin.flush()
    output = proc.stdout.readline()
    print(output.decode().rstrip())
    
remainder = proc.communicate()[0]
print(remainder.decode())