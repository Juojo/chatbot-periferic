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
    sha256 = 0 # Inicializo variable local
    try:
        with open(ruta_archivo, "rb") as f: # Abre el archivo en read only y en binario
            f = f.read()
            preguntas_sha256 = hashlib.sha256(f).hexdigest()
        sha256 = str(preguntas_sha256)
    except FileNotFoundError:
        sha256 = "0"
    return sha256

def escribirArchivo():
    if calcularSha256(ruta_archivo_preguntas) == sha256_correcto:
        print("El archivo con las preguntas ya existe en el directorio y su contenido es correcto")
        print("No es necesario generar el archivo")
    else:
        print("El archivo con las preguntas no existe en el directorio o su contenido no es correcto")
        print("Se esta generando el archivo '" + ruta_archivo_preguntas + "'")
        
        try:
            preguntas = open(ruta_archivo_preguntas, "w") # Abre o crea el archivo con permisos de escritura

            # Escritura del archivo preguntas

            # En la primer linea se escriben los campos
            for i in range (0, len(campos)):
                preguntas.write(str(campos[i]))
                
                # Se imprime un ; entre campos y un salto de linea al terminar la fila
                if i < len(campos)-1:
                    preguntas.write(";")
                else:
                    preguntas.write("\n")

            # Y luego los datos (preguntas y respuestas)
            for i in range (0, len(datos)): # Itera sobre la cantidad de preguntas (filas)
                for j in range (0, len(campos)): # Itera sobre la cantidad de columnas de cada fila (2)
                    preguntas.write(str(datos[i][j]))
                    
                    if j < len(campos)-1:
                        preguntas.write(";")
                preguntas.write("\n")
                    
            preguntas.close()
            
            print("El archivo se genero correctamente")
        except Exception as e:
            print("Ocurrio un error con el archivo:", e)
            sys.exit(1) # Se finaliza el programa si ocurre un error

def leerArchivo():
    return