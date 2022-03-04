import requests

sourceLang="en"
targetLang="it"
sourceText="Hello world"

url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={sourceLang}&tl={targetLang}&dt=t&q={requests.utils.quote(sourceText)}";

response = requests.get(url)

print(response.status_code)  
js=response.json()
print(type(js), js);

