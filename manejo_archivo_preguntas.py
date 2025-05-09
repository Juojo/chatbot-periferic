import hashlib, sys

# Variables

ruta_archivo_preguntas = "./preguntas.csv";
sha256_correcto = "3d30890753dcf1a9c8e96ac499f7363506a7725555af63b48af3fe8efeb7dd04"

campos = ["Pregunta", "Respuesta"]

datos = [
    ["¿Como es tu nombre?", "Mi nombre es chatbot"],
    ["¿Cual es tu color favorito?", "Mi color favorito es el rojo!"],
    ["Como es tu nombre", "Mi nombre es chatbot"],
    ["Como es tu nombre", "Mi nombre es chatbot"],
    ["Como es tu nombre", "Mi nombre es chatbot"],
]

# Funciones

def calcularSha256(ruta_archivo):
    sha256 = "0" # Inicializo variable local
    try:
        with open(ruta_archivo, "rb") as f: # Abre el archivo en read only y en binario
            f = f.read()
            preguntas_sha256 = hashlib.sha256(f).hexdigest()
        sha256 = str(preguntas_sha256)
    except FileNotFoundError:
        sha256 = "0"
    return sha256

def escribirArchivoPreguntas():
    print("Se esta generando el archivo '" + ruta_archivo_preguntas + "'")
    
    try:
        archivo_preguntas = open(ruta_archivo_preguntas, "w") # Abre o crea el archivo con permisos de escritura

        # En la primer linea se escriben los campos
        for i in range (0, len(campos)):
            archivo_preguntas.write(str(campos[i]))
            
            # Se imprime un ; entre campos y un salto de linea al terminar la fila
            if i < len(campos)-1:
                archivo_preguntas.write(";")
            else:
                archivo_preguntas.write("\n")

        # Y luego los datos (preguntas y respuestas)
        for i in range (0, len(datos)): # Itera sobre la cantidad de preguntas (filas)
            for j in range (0, len(campos)): # Itera sobre la cantidad de columnas de cada fila (2)
                archivo_preguntas.write(str(datos[i][j]))
                
                if j < len(campos)-1:
                    archivo_preguntas.write(";")
            archivo_preguntas.write("\n")
                
        archivo_preguntas.close()
        
        print("El archivo se genero correctamente")
    except Exception as e:
        print("Ocurrio un error con la escritura del archivo:", e)
        sys.exit(1) # Se finaliza el programa si ocurre un error

def leerArchivoPreguntas():
    # La funcion devuele los datos cargados en una matriz para poder ser utilizados directamente desde la memoria
    
    # Se escribe / crea el archivo si no existe o su contenido no es correcto
    if calcularSha256(ruta_archivo_preguntas) != sha256_correcto:
        print("El archivo con las preguntas no existe en el directorio o su contenido no es correcto")
        escribirArchivoPreguntas()
        
    # Lectura
    try:
        archivo_preguntas = open(ruta_archivo_preguntas, "r") # Abre el archivo como read only
        array_preguntas_respuestas = archivo_preguntas.readlines() # Asigna todas las lineas del archivo en un array, cada linea es un elemento y contiene una pregunta y su respuesta
        array_preguntas_respuestas.pop(0) # Elimina el primer elemento (Solo se usa en el csv para indicar los campos)
        
        matriz_preguntas_respuestas = []
        
        for i in range (0, len(array_preguntas_respuestas)):
            pregunta_respuesta = array_preguntas_respuestas[i].split(";") # Divide el string en un array de dos posiciones. La primera es la pregunta, la segunda la respuesta
        
            matriz_preguntas_respuestas.append(pregunta_respuesta) # Guarda ese array en la ultima posicion de la matriz
        
        return matriz_preguntas_respuestas
    except Exception as e:
        print("Ocurrio un error con la lectura del archivo:", e)
        sys.exit(1) # Se finaliza el programa si ocurre un error