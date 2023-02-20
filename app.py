from flask import Flask
from flask import request
#import flask 
app = Flask(__name__) #dunder

@app.route("/") #url is language independent
def hello_world():
    return "Hello, World!"
#copy lab url,port no & put server
@app.route("/hello1") #url is language independent
def hello_world1():
    return "Hello, World1!"
#if server up & running so everyone access but when close than its can not acess
@app.route("/hello2") #url is language independent
def hello_world2():
    return "Hello, World2!"

@app.route("/test_fun")
def test():
    a=5+6
    return "This is my Fisrt fun Flash {}".format(a)    
@app.route("/input_url")
def request_input():
    data = request.args.get('x')
    return "this is my input from url {}".format(data)
if __name__=="__main__":
    app.run(host="0.0.0.0")
