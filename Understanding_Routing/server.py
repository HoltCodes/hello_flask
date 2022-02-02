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

@app.route('/say/<name>')
def say_name(name):
    return f"Hi {name.capitalize()}!"

@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num, word):
    output = ''

    for i in range(0,num):
      output += f"<p>{word}</p>"

    return output    

if __name__=="__main__":
    app.run(debug=True)