import requests
 
response = requests.post("http://localhost:5000/facto/7")
# 
print(response.status_code)
print(response.text)

