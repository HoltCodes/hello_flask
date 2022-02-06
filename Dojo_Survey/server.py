from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)

app.secret_key="Holt.Codes"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/success')
def success():
    return render_template('success.html')    

if __name__=="__main__":
  app.run(debug=True)