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


class Blog():
    def __init__(self,titulo,desc) -> None:
        self.titulo=titulo
        self.desc=desc


@app.route('/blogs')
def blogs():
    b1=Blog('Que es Python', 'Descripcion 1')
    b2=Blog('Que es Flask', 'Descripcion 2')    
    lista=[b1,b2]
    return render_template('blogs.html',blogs=lista)

if __name__=='__main__': 
    app.run(debug=True)