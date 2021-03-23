# Reto 1: Desarrollar un programa de bienvenida

# 1. Ingresar un nombre y su edad.
# 2. Si es menor de edad que indique que dependiendo de la hora (si es mas de las 6pm) debe ir a dormir y si no hacer la tarea.
# 3. Si es mayor de edad que indique que no esta obligado a hacer nada.

# --------------------------------------------------------------------------

# Importando módulo para obtener la hora
from datetime import datetime

# Obteniendo datos del usuario
nombre = str(input('Ingrese su nombre: '))
edad = int(input('Ingrese su edad: '))

# Obteniendo hora actual
hora_actual = datetime.now().hour

# Aplicando Condiciones
if edad < 18 :
  if hora_actual >= 18 :
    print(nombre,'debes ir a dormir!')
  else :
    print(nombre,'debes hacer la tarea!')
else :
  print(nombre,'no tienes ninguna obligación')
