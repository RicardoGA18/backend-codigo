Entorno virtual: librería virtualenv
#instalar virtualenv
pip install virtualenv
#crear entorno virtual
virtualenv venv
#Activar entorno virtual
windows: venv\Scripts\actibate.bat
linux: source venv/Scripts/activate

#Librerias
pip install flask flask-cors flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy mysqlclient

#Requirements
pip freeze > requirements.txt
pip install -r requirements.txt