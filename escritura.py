import hashlib

# Funciones

def calcularSha256(ruta_archivo):
    with open(ruta_archivo, "rb") as f: # Abre el archivo en read only y en binario
        f = f.read()
        preguntas_sha256 = hashlib.sha256(f).hexdigest()
    return str(preguntas_sha256)

# Variables

ruta_archivo_preguntas = "./preguntas.csv";
sha256_correcto = "4e8a59126d1301f95826087b9a52ab340538458180ce05c4598c499025e8a599"

campos = ["Pregunta", "Respuesta"]

datos = [
    ["¿Como es tu nombre?", "Mi nombre es chatbot"],
    ["¿Cual es tu color favorito?", "Mi color favorito es el rojo!"],
    ["Como es tu nombre", "Mi nombre es chatbot"],
    ["Como es tu nombre", "Mi nombre es chatbot"],
    ["Como es tu nombre", "Mi nombre es chatbot"],
]

# Codigo

if calcularSha256(ruta_archivo_preguntas) == sha256_correcto:
    print("El archivo con las preguntas ya existe en el directorio y su contenido es correcto")
else:
    print("El archivo con las preguntas no existe en el directorio o su contenido no es correcto")

    preguntas = open(ruta_archivo_preguntas, "w") # Abre o crea el archivo con permisos de escritura

    # Escritura del archivo preguntas

    # Campos
    for i in range (0, len(campos)):
        preguntas.write(str(campos[i]))
        
        # Se imprime un ; entre campos y un salto de linea al terminar la fila
        if i < len(campos)-1:
            preguntas.write(";")
        else:
            preguntas.write("\n")

    # Datos (preguntas y respuestas)
    for i in range (0, len(datos)): # Itera sobre la cantidad de preguntas (filas)
        for j in range (0, len(campos)): # Itera sobre la cantidad de columnas de cada fila (2)
            preguntas.write(str(datos[i][j]))
            
            if j < len(campos)-1:
                preguntas.write(";")
        preguntas.write("\n")
            
    preguntas.close()