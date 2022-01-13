from flask import Flask 

app =  Flask(__name__)

@app.route('/')
def hello():
    return "Hello"

if __name__ == "main":
    app.run(debug=True, port=5000)