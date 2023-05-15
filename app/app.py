#importar la libreria flask
from flask import Flask, render_template

#inicializamos la app
app=Flask(__name__)

#ruta inicial
@app.route('/')
#funcion inicial para ejecutar
def index():
    #return "<h1>Hola mundo1!!</h1>"F
    data={
        'titulo':'Index',
        'bienvenido':'SALUDOS'
    }
    return render_template('index.html',data=data)
#si la aplicacion es main entonces correra
if __name__=='__main__':
    #es posible mandarle el modo debug
    app.run(debug=True)