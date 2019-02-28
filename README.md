# python
https://www.python.org/downloads/

### Mostrar versión
$ python3

## Editores
|vscode
|:-------|
|https://code.visualstudio.com

Instalar plugin, "Python 2019.2.5433, Linting, Debuggin ...", Install, Reload.

|geany
|:-------|
| https://www.geany.org/Download/Releases

Menú Construir, Establecer comandos de construcción: Compile: python3 -m py_compile "%f", Execute: python3 "%f"

## Ejecutar
Por ejemplo creamos el archivo main.py 
```
print("hola mundo")
```
Abrimos una terminal y escribimos python3 main.py

¡Guao!.

Utilizaré vscode como editor y sobre git al principio desde la terminal, luego desde el vscode.

Después de instalar vscode, al abrir el editor nos mostrará la pestaña Welcome, Customize, Tools and language, Install support for Python (picamos ahí); abrimos la paleta de comandos y escribiemos "shell command" para que desde la terminal podamos abrir el vscode escribiendo "code ."
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

#Mayúscula principio de cada palabra
print(msg.title())

msg.upper()
msg.lower()

#Concatenación es como en Java con "+"

#\n \t

#Quitar espacio en blanco por la derecha.
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

#Cast int a String
str(num)

# Inicia en 0
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
```
