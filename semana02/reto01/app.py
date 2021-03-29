# Reto 01: Desarollar una API de mostrar departamentos

# Importando librerías
from flask import Flask,request
from flask_cors import CORS

# Instanciando Flask y aplicando CORS
app = Flask(__name__)
CORS(app)

# Lista de departamentos
departamentos = [
	{
		'id': 1,
		'ubicacion': 'Ubicacion 01',
		'numero_cuartos': 4,
		'numero_banios': 2,
		'cocina': True,
		'lavadero': False
	},
	{
		'id': 2,
		'ubicacion': 'Ubicacion 02',
		'numero_cuartos': 2,
		'numero_banios': 1,
		'cocina': False,
		'lavadero': False
	},
	{
		'id': 3,
		'ubicacion': 'Ubicacion 03',
		'numero_cuartos': 3,
		'numero_banios': 2,
		'cocina': True,
		'lavadero': True
	},
	{
		'id': 4,
		'ubicacion': 'Ubicacion 04',
		'numero_cuartos': 4,
		'numero_banios': 1,
		'cocina': False,
		'lavadero': True
	},
]

# Creando la ruta depoartamentos
@app.route('/api/departamentos')
def get_departamentos():
	return {
		'ok': True,
		'content': departamentos,
		'message': 'Departamentos enviados correctamente'
	}, 200

# Levantando el servidor
if __name__ == '__main__':
	app.run(port=5000,debug=True)
