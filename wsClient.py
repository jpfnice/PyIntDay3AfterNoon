import requests

# methods: get post put delete head ...

response = requests.get('https://ipwhois.app/json/128.178.115.174')
print(response.status_code)
print(response.headers)

js=response.json()
print(type(js),js)

# HTTP (header/body):  method + URL + parameter
# post
# delete
# put
# head
# get
# epfl.ch/labo/compute1 + get
# epfl.ch/labo/compute1 + post
# epfl.ch/labo/compute2 + get

# response = requests.get("https://itunes.apple.com/search?term=dave+gahan&limit=10")
# # response = requests.post("http://sicourspc220:5000/facto/10")

# print(response.status_code)
# #print(response.headers)

# js=response.json()
# #print(type(js),js)
# # print(js["factorial"])

# for track in js["results"]:
#     print(track["trackName"])