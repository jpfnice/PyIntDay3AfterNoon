from flask import Flask, url_for, json, request, jsonify 

def factorial(nb):
    if nb== 0:
        return 1
    else:
        return factorial(nb-1) * nb
    
app = Flask(__name__) 

@app.errorhandler(404) 
def not_found(error=None):     
    message = {             
        'status': 404,             
        'message': 'Not Found: ' + request.url,     }     
    resp = jsonify(message)     
    resp.status_code = 404 
 
    return resp
 
@app.route('/') # http://localhost:5050/
def api_root():     
    return 'Welcome' 
 
@app.route('/articles') # http://localhost:5050/articles
def api_articles():     
    return 'List of ' + url_for('api_articles') 
 
@app.route('/articles/<articleid>') # http://localhost:5050/articles/3
def api_article(articleid):     
    return 'You are reading ' + articleid 

# http://localhost:5050/facto/23 + GET
@app.route('/facto/<int:number>', methods=["GET", "POST"]) 
def api_facto(number):
    if request.method == "GET":     
        result=factorial(number) 
        message={"nb":number, "factorial":result}
        resp = jsonify(message)     
        resp.status_code = 200
        return resp
    elif request.method == "POST":
        message={"nb":number, "factorial":"PROBLEM!!"}
        resp = jsonify(message)     
        resp.status_code = 200
        return resp
    
if __name__ == '__main__':     
    app.run(host="localhost")
    