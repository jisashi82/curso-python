from flask import Flask, render_template


app=Flask(__name__)

@app.route('/')
def hola():
   # return '<h1>Hola Mundo de Flask</h1>'
   mensaje='Hola Mundo con Flask'
   return render_template('index.html', msj=mensaje)

@app.route('/<name>')
def show_user(name):
    return f'Hola {name}'


if __name__=='__main__': 
    app.run(debug=True)