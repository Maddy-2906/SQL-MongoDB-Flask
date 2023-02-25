from flask import Flask

app = Flask(__name__)

@app.route("/welcome")
def welcome():
    return "<h1> welcome to ABC corporation <h1>"

@app.route("/")
def company_details():
    return "<h1>compnay_name : welcome to ABC corporation</h1> location : India<h1> mobile_details : 9999999999"

if __name__=="__main__":
    app.run(host="0.0.0.0")
