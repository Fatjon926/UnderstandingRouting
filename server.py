from flask import Flask , render_template 
app = Flask(__name__)    
@app.route('/')          
def hello_world():
    return 'Hello World!' 
@app.route('/dojo')          
def dojo():
    return 'Dojo!' 
@app.route('/say/<name>')          
def say(name):
    return "Hi " + name + "!"

@app.route('/repeat/<int:num>/<string:word>')
def hello(num,word):
     output=''

     for i in range(0,num):
          output +=word
     return output


if __name__=="__main__":   
    app.run(debug=True)    

