# python
https://www.python.org/downloads/

## Tabla de contenido

- [Editores](#editores).
- [Mostrar versión](#mostrar-versión).
- [Ejecutar tu código](#ejecutar-tu-código).
- [Comentario corto](#comentario-corto).
- [Comentario largo](#comentario-largo).
- [Variables](#variables).
- [Expresiones aritméticas](#expresiones-aritméticas).
- [Operadores de relación](#operadores-de-relación).
- [Operadores lógicos](#operadores-lógicos).
- [Funciones internas](#funciones-internas).
- [Entrada y salida de la información](#entrada-y-salida-de-la-información).
- [Estructuras repetitivas](#estructuras-repetitivas).
- [Estructuras de datos](#estructuras-de-datos).

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

Después de instalar vscode, al abrir el editor nos mostrará la pestaña Welcome, Customize, Tools and language, Install support for Python (picamos ahí). Abrimos la paleta de comandos y escribiemos "shell command" para que desde la terminal podamos abrir este editor escribiendo "code ."
```
mkdir carpetaApp
cd carpetaApp
code .
```
Para ejecutar, click derecho en nuestro código, "Ejecutar archivo Python en la terminal".
Para el debug, pinchamos a la izquierda en Debug, y ahí encontraremos el botón "Start Debugging".


## Comentario corto
```
#Esto es un comentario corto igual que Bash
```

## Comentario largo
```
"""
comentario 
largo
"""
```

## Variables
```
varCadena="un texto "

varLogica = True
varLogica = False

varLong = 0.5

varCadena='hola 'que hace' # Obvio que da error.

# Concatenación es como en Java con "+"
# Otra manera
varCadena = "a "
varCadena += "b"

\n \t
```

## Expresiones aritméticas
```
+
-
*
/ 
5 ** 2 # Potencia

5 + (4 * 2) 
0.3 + 0.1 # long
```

## Operadores de relación
```
== # La comparación es sencible a Mayúsculas y Minúsculas.
!= # Distinto
<  # Menor que
<= # Obvio
>  
>=
%  # Operador módulo 20 % 5
```

## Operadores lógicos
```
and 
or
```

## Funciones internas
```
varCadena.title() #Mayúscula principio de cada palabra
varCadena.upper()
varCadena.lower()
varCadena.rstrip() # Quitar espacio en blanco por la derecha.
varCadena.lstrip()
varCadena.strip() # Equivalente al trim.

```

## Entrada y salida de información
Entrada de texto y númerica
```
respuesta = input("Introduzca la opción correcta: ")
print(respuesta)

# Para casos de enteros
respuesta = int(respuesta)

# Para la versión 2 el input es raw_input()
```

Salida
```
print('hola mundo')
```

## Casting
```
int(unaCadena)
str(unNumero)

str(num) #Cast int a String
```

## Estructuras selectivas
```
if condicion:
    sentencia
elif:
    sentencia
else:
    sentencia

var in miLista # Obvio
var not in miLIsta

# Si la lista no es empty
miLista = []
if miLista:
    sentencia
else:
    sentencia
```

## Estructuras repetitivas
```
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

```

## Estructuras de datos
```
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

# Hasta aquí queda pendiente investigar si se crean zoombies, pero lo dejo para luego.

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
```

```
# Se puede utilizar return
# Podemos retornar un diccionario
# Los parametros opcionales es igual que el resto de lenguajes por ejemplo vb.
# Se puede pasar una lista como argumento y tened claro que el paso es por referencia
# El paso por valor de una lista es sencillo paramLista[:]
```

```
# N parámetros 
def miFuncion(*params):
    sentencia

miFuncion('a','b','c')
```

```
def miFuncion(**paramsKeyValor):
    sentencia

miFuncion(nombre='Juan', materia='Java')
```

## Import
```
ficheroA.py

ficheroB.py
-----------
import ficheroA

ficheroA.unaFuncion()
```

```
ficheroA.py

ficheroB.py
-----------
from ficheroA import unaFuncion, otraFuncion

unaFuncion()
```

```
ficheroA.py

ficheroB.py
-----------
from ficheroA import unaFuncion as uf

uf()
```

```
ficheroA.py

ficheroB.py
-----------
import ficheroA as fa

fa.unaFuncion()
```

```
ficheroA.py

ficheroB.py
-----------
from ficheroA import *

unaFuncion()
```

## Clases