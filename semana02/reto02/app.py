# Reto 02: Desarrollar una API para ingresar datos y mostrarlos

# Importando librerías
from flask import Flask,request
from flask_cors import CORS

# Instanciando Flask y aplicando CORS
app = Flask(__name__)
CORS(app)

# Lista de futbolistas
futbolistas = [
	{
		'nombre': 'Mbappe',
		'equipo': 'Paris saint germain',
		'goles': 159,
		'edad': 22
	},
	{
		'nombre': 'Messi',
		'equipo': 'Barcelona',
		'goles': 770,
		'edad': 330
	}
]

# Creando ruta para obtener futbolistas
@app.route('/api/futbolistas/obtener',methods=['GET'])
def obtener_futbolistas():
	return {
		'ok': True,
		'content': futbolistas,
		'messages': None
	}, 200

# Creando ruta para agregar futbolistas
@app.route('/api/futbolistas/agregar',methods=['POST'])
def agregar_futbolistas():
	futbolista = request.get_json()
	futbolistas.append(futbolista)
	return {
		'ok': True,
		'content': futbolista,
		'message': 'Futbolista agregado correctamente'
	}, 201

# Levantando el servidor
if __name__ == '__main__':
	app.run(port=5000,debug=True)