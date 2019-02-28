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

Después de instalar vscode, al abrir el editor nos mostrará la pestaña Welcome, Customize, Tools and language, Install support for Python (picamos ahí); abrimos la paleta de comandos y escribiemos "shell command" para que desde la terminal podamos abrir el vscode escribiendo code .
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
```
