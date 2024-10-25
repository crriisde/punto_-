print (" ") #Esta linea da el espacio para el nombre
print ("Cristian David Salas De La O 3-W") # Esta linea muestra el nombre 
print (" ") #Esta linea da el espacio para el nombre
archivo_nombre = "demofile.txt" #Esta linea define el nombre del archivo

try: #esta linea inicia el try
    with open(archivo_nombre, 'r') as file: #Esta linea define abrir el archivo 
        content = file.read() #Esta linea define el contenido 
        print("Contenido del archivo:") #Esta linea da un aviso del contenido del archivo 
        print(content) #Esta linea muestra el contenido del arochivo
except FileNotFoundError: #Esta linea como mostrara el error que no se encotro 
    print(f"Error: El archivo '{archivo_nombre}' no se encontró.") #Esta linea avisa del error que no se encontro 
except Exception as e: #Esta linea avisa del error
    print(f"Se produjo un error: {e}") #Esta linea muestra el error
