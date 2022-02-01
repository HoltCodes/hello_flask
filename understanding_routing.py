from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'
    
@app.route('/Dojo')
def Dojo():
    return 'Dojo'

@app.route('/say/<Flask>')
def say(Flask):
  print(Flask)
  return "Hi " + Flask

@app.route('/say/<Michael>')
def say(Michael):
  print(Michael)
  return "Hi " + Michael  

@app.route('/say/<John>')
def say(John):
  print(John)
  return "Hi " + John

if __name__=="__main__":
    app.run(debug=True)