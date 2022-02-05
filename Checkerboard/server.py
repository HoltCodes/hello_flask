from turtle import color
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", row=8,col=8,color_one='orange', color_two= 'black')

if __name__=="__main__":
    app.run(debug=True)