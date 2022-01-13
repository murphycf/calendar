from flask import Flask, render_template

app =  Flask(__name__)
app = Flask(__name__,template_folder='template')

@app.route('/')
def calendar():
    return render_template("templates\calendar.html")

if __name__ == "main":
    app.run(debug=True, port=5000)