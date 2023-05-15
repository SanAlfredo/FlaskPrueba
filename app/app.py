#importar la libreria flask
from flask import Flask, render_template, request, url_for, redirect,jsonify

#llamar la libreria para usar mysql
from flask_mysqldb import MySQL

#inicializamos la app
app=Flask(__name__)

#ahora iniciar la conexion Mysql
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'prueba1'

conn = MySQL(app)

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

#Ahora crearemos una request o algo que el cliente solicita al servidor
#notar que no se le pone una url o ruta con @ como en las anteriores
#ya que esta funcion se la llama desde main
def query_string():
    print(request)
    print(request.args)
    print(request.args.get('param1'))
    return "ok"

#nueva ruta que devuelve los datos de la base de datos
@app.route('/personas')
def listar_personas():
    data={}
    try:
        cursor=conn.connection.cursor()
        sql='SELECT * FROM personas'
        cursor.execute(sql)
        personas=cursor.fetchall()
        data['personas']=personas
        data['mensaje']='Exitoso'
    except Exception as ex:
        data['mensaje']='Error...'
    return jsonify(data)
#configurar el error 404
def pagina_no_encontrada(error):
    return render_template('404.html'), 404
    #tambien es posible enviar una redirecion al pagina principal
    #return redirect(url_for('index'))

#antes y despues de que se ejecute un request tambien podemos tener funciones que actuen
@app.before_request
def before_request():
    print("antes de la peticion ...")

@app.after_request
def after_request(response):
    print("despues de la peticion")
    return response

#si la aplicacion es main entonces correra
if __name__=='__main__':
    #aqui llamamos al request
    app.add_url_rule('/query_string', view_func=query_string)
    #manejador de errores
    app.register_error_handler(404,pagina_no_encontrada)
    #es posible mandarle el modo debug
    app.run(debug=True)