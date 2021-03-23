# Reto 3: Desarrollo de Productos con POO

# Tener un programa que reciba una cantidad de productos a ingresar,
# que luego de ingresarlos (instanciar) podamos llamar a uno de ellos y
# que nos muestre su descripción y si no, tengamos una opción para terminar
# el programa. (Usar if elif else y while)

# -----------------------------------------------------------------------------

# Creando la clase Producto
class Producto:
  def __init__(self,uuid,nombre,descripcion):
    self.uuid = uuid
    self.nombre = nombre
    self.descripcion = descripcion

# array para almacenar productos
almacen = []

# Bienvenida
print('Bienvenido a Almacen Python')

# Obteniendo cantidad de productos a ingresar
num_prod = int(input('Ingrese la cantidad de productos: '))

# Obteniendo la informacion de cada producto
# y almacenandola

for iterador in range(num_prod):
  print('---------------------------------')
  print('Producto',iterador+1)
  uuid = str(input('Ingrese el id del producto: '))
  nombre = str(input('Ingrese el nombre del producto: '))
  descripcion = str(input('Ingrese la descripcion del producto: '))
  almacen.append(Producto(uuid,nombre,descripcion))

# Estado de la aplicación
estaCorriendo = True

# Inicio del bucle para realizar consultas
while estaCorriendo:
  print('---------------------------------')
  print('Lista de opciones')
  print('a. Obtener producto por id.')
  print('b. Obtener producto por nombre.')
  print('c. Finalizar programa.')
  print('---------------------------------')
  
  opcion = str(input('Ingrese una opcion: '))
  if opcion == 'a':
    # Obteniendo id
    uuid = str(input('Ingrese el id del producto: '))
    # Funcion para filtrar el producto
    def filtrarPorId(producto):
      if producto.uuid == uuid:
        return True
    # Filtrando para obtener producto
    producto_deseado = list(filter(filtrarPorId,almacen))
    if(len(producto_deseado)):
    # Mostrando Producto
      print('-----------------------------------------')
      print('Producto',producto_deseado[0].uuid)
      print('Nombre:',producto_deseado[0].nombre)
      print('Descripcion:',producto_deseado[0].descripcion)
      print('----------------------------------------------')
    else:
      print('producto no encontrado')
    str(input('Ingrese cualquier valor para continuar: '))
  elif opcion == 'b':
    # Obteniendo nombre
    nombre = str(input('Ingrese el nombre del producto: '))
    # Funcion para filtrar el producto
    def filtrarPorNombre(producto):
      if producto.nombre == nombre:
        return True
    # Filtrando para obtener producto
    producto_deseado = list(filter(filtrarPorNombre,almacen))
    if len(producto_deseado):
      # Mostrando Producto
      print('-----------------------------------------')
      print('Producto',producto_deseado[0].uuid)
      print('Nombre:',producto_deseado[0].nombre)
      print('Descripcion:',producto_deseado[0].descripcion)
      print('----------------------------------------------')
    else:
      print('producto no encontrado')
    str(input('Ingrese cualquier valor para continuar: '))
  elif opcion == 'c':
    # Cambiando estado de la aplicacion
    print('Finalizando Programa')
    estaCorriendo = False
  else:
    print('Opcion invalida')



