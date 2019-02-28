# python
https://www.python.org/downloads/

## Tabla de contenido

- [Editores](#editores).
- [Mostrar versión](#mostrar-versión).
- [Ejecutar tu código](#ejecutar-tu-código).

## Editores
|vscode
|:-------|
|https://code.visualstudio.com

Instalar plugin, "Python 2019.2.5433, Linting, Debuggin ...", Install, Reload.

|geany
|:-------|
| https://www.geany.org/Download/Releases

Menú Construir, Establecer comandos de construcción: Compile: python3 -m py_compile "%f", Execute: python3 "%f"

## Mostrar versión
```
python3
```

## Ejecutar tu código
Creamos main.py
```
print("hola mundo")
```
Para ejecutar el código, abrimos una terminal y escribimos 
```
python3 main.py
```

¡Guao!.

Utilizaré vscode como editor y también git.

Después de instalar vscode, al abrir el editor nos mostrará la pestaña Welcome, Customize, Tools and language, Install support for Python (picamos ahí). Abrimos la paleta de comandos y escribiemos "shell command" para que desde la terminal podamos abrir el vscode escribiendo "code ."
```
mkdir carpetaApp
cd carpetaApp
code .
```
Para ejecutar, click derecho en nuestro código, "Ejecutar archivo Python en la terminal".

Pinchamos a la izquierda en Debug, y ahí encontraremos el botón Start Debugging.

```
# Esto es un comentario corto igual que Bash

# Comentario largo
"""
comentario 
largo
"""

# Variables
msg="una cadena "
print(msg)

var='cat'
if var == 'cat':
    print('Categoría')
else:
    print('Autor')

# La comparación es sencible a Mayúsculas y Minúsculas.

!= # Distinto
<  # Menor que
<= # Obvio
>  
>=
%  # Operador módulo 20 % 5

and 
or

var in miLista # Obvio
var not in miLIsta

var = True
var = False

if condicion:
    sentencia
elif:
    sentencia
else:
    sentencia

# Si la lista no es empty
miLista = []
if miLista:
    sentencia
else:
    setnencia

while condicion:
    sentencia

while miLista:
    sentencia

while 'unValorRepe' in miLista:
    miLista.remove('unValorRepe')

# Se pueden utilizar flags o sentinelas pero esto no pertenece al lenguaje
# sino a conocimiento.
# En Python tenemos break pero mejor no utilizarlo.
# continue

#Mayúscula principio de cada palabra
print(msg.title())

msg.upper()
msg.lower()

# Concatenación es como en Java con "+"
# Otra manera
var = "a "
var += "b"

#\n \t

# Quitar espacio en blanco por la derecha.
msg.rstrip()

# Obvio
msg.lstrip()

# Equivalente al trim.
msg.strip()

# Obvio que da error.
msg='hola 'que hace'


+, -, *, / # Operadores típicos

5 ** 2 # Potencia

5 + (4 * 2) 

0.3 + 0.1 # long

# El índice de una lista inicia en 0

miLista = [1, 2, 3]
min(miLista)
max(miLista)
sum(miLista)

miLista = list(range(1,6)) # Valor de los elementos 1 hasta 5
miLista = lista(range(2,7,2)) # Lo mismo, pero de 2 en dos
miLista = [num**2 for num in range(1,3)] # Primero, que valor tiene num en el for, resp 1, potencia de 1 es 1, etc.

miLista=[] #Lista vacía.
miLista = ['a', 'b', 'c']
print(miLista)
print(miLista[1])
miLista[-1] #Primer elemento desde la derecha.
miLista[0]='A'
miLista.append('d')
miLista.insert(0, 'aa')
del miLista[0]
miLista.pop() # Quita el elemento -1 a la lista y retorna el elemento quitado 
miLista.pop(0) # Obvio
miLista.remove('c')
miLista.sort()
miLista.sort(reverse=True)
sorted(miLista) # Para mantener la lista intacta, retorna la lista aplicando sort.
miLista.reverse() # No se trata de ordenar más bien de que el orden de los elementos vaya al revés.
len(miLista)

for elemento in miLista:
    print(elemento)
    print('\nlo que sea\n')  #Esta línea está dentro del for, lo sé por la identación.

# Desde 1 hasta 4
for num in range(1,5):
    print(num)

miLista[0:3] # Retorna una lista desde el elemento 0 al 2
miLista[:3] # Obvio
miLista[1:] # Obvio
miLista[-3:] # Índice negativo, cuento de derecha a izquierda como quien lee un manga, tercer índice hasta n.

for num in miLista[:3]:
    print(num)

miLista2 = miLista[:] # Equivalente a copiar la lista.

# Tuplas
# Las tuplas son estáticas.
# Para definir una tubla se utilizan los paréntesis
miTupla = (200, 300)
print(miTupla[0])
miTupla[0] = 4 # ¡Ojo!, no se puede porque la tupla es estática, que ya no se puede modificar.

for num in miTupla:
    print(num)

miTupla = ('a')
miTupla = ('b') #Obvio

# Diccionarios
#------------
# Equivalente a arrays asociativos, hashtable, diccionarios de vb.
# Son pares key-valor

miDic = {} # Diccionario vacío
miDic = {'nombre':'Marco', 'edad': 20}
miDic['nombre']
miDic['edad']=19
miDic['telefono']=0
del miDic['telefono']

miDic = {
    'nombre': 'Marco',
    'edad': 20,
    'telefono': 0
}

# Me suena al foreach de PHP
for k, v in miDic.items():
    print(k)
    print(v)

for k in miDic.keys():
    print(k)

for k in sorted(miDic.keys()):
    print(k)  

for v in miDic.values():
    print(v)

# Si el valor está reptido no lo vuelve a mostrar
for v in set(miDic.values()):
    print(v)

# Nesting, anidación.

persona0 = {'nombre':'Esteban'}
persona1 = {'nombre':'Juan'}
personas = [persona0, persona1]
for persona in personas:
    print(persona)

persona=[]

miDic = {
    'nombre': 'Juan',
    'asignaturas':['Java', 'XML']
}

miDic = {
    'ID001':{
        'nombre':'Pablo'
    },
    'ID002':{
        'nombre':'Valentín'
    }
}

# Entrada de texto y númerica
# Al ejecutar desde la terminal externa tened cuidado que escribamos
# python3 main.py
respuesta = input("Introduzca la opción correcta: ")
print(respuesta)

# Para casos de enteros
respuesta = int(respuesta)

# Para la versión 2 el input es raw_input()

# Hasta aquí queda pendiente investigar si se crean zoombies, pero lo dejo para luego.

```
### Casting
```
# Casting
int(unaCadena)
str(unNumero)

#Cast int a String
str(num)
```

## Funciones
```
def mostrarMsg(msg):
    sentencia

mostrarMsg('hola')
mostrarMsg(msg='hola')
```

Función con parámetro opcional
```
def mostrarMsg(msg, titulo='valorPorDefecto'):
    sentencia

mostrarMsg(msg='hola')
```

```
def mostrarMsg(msg, titulo):
    sentencia

mostrarMsg(msg='hola', titulo='saludo')
mostrarMsg(titulo='saludo', msg='hola')

# Se puede utilizar return
# Podemos retornar un diccionario
# Los parametros opcionales es igual que el resto de lenguajes por ejemplo vb.
# Se puede pasar una lista como parámetro y tened claro que el paso es por referencia
# El paso por valor de una lista es sencillo paramLista[:]

# N argumentos 
def miFuncion(*args):
    sentencia

miFuncion('a','b','c')


```
