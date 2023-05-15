#importar la libreria flask
from flask import Flask, render_template

#inicializamos la app
app=Flask(__name__)

#ruta inicial
@app.route('/')
#funcion inicial para ejecutar
def index():
    #return "<h1>Hola mundo1!!</h1>"
    cursos=['Python','Java','JavaScript','C++']
    data={
        'titulo':'Primera app Flask',
        'bienvenido':'SALUDOS',
        'cursos':cursos,
        'numero_cursos':len(cursos)
    }
    return render_template('index.html',data=data)

#url Dinamica que le metes un parametro nombre
@app.route('/contacto/<nombre>')
#hay que tomar en cuenta que los parametros y nombres de las def deben ser iguales a lo 
#que se pone en la ruta para que no genere errores
#entonces si quisieramos la edad def contacto (nombre,edad), mientras que la ruta seria
#route ('/contacto/<nombre>/<int:edad>')
def contacto(nombre):
    data={
        'titulo':'Contacto',
        'nombre':nombre
    }
    return render_template('contacto.html',data=data)





#si la aplicacion es main entonces correra
if __name__=='__main__':
    #es posible mandarle el modo debug
    app.run(debug=True)