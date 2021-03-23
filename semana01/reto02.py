# Reto 2: Ingresar Personas

# Hacer un programa que primero capture cuantas Personas vamos a ingresar
# luego pedir su nombre, dni y fecha de nacimiento y al final
# mostrarlas en un orden de la mas joven a la mas adulta

# ----------------------------------------------------------

# Obteniendo numero de personas a ingresar
num_per = int(input('Ingrese el numero de personas: '))

# Array para almacenar personas
personas = []

# Obteniendo la información de cada persona
# y almacenándola
for iterador in range(num_per):
  newPerson = {}
  print('Persona',iterador+1)
  newPerson['nombre'] = str(input('Ingrese el nombre: '))
  newPerson['dni'] = int(input('Ingrese el dni: '))
  newPerson['edad'] = int(input('Ingrese la edad: '))
  personas.append(newPerson)

# Ordenando personas por edad
# Funcion para definir la clave de orden
def porEdad(persona):
  return persona['edad']

# Ordenando
personas.sort(key=porEdad)

#Mostrando en consola
for iterador in range(len(personas)):
  print('----------------------------------------')
  print('Persona',iterador+1,':')
  print('Nombre:',personas[iterador]['nombre'])
  print('DNI:',personas[iterador]['dni'])
  print('Edad:',personas[iterador]['edad'])
