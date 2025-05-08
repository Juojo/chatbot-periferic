from manejo_archivo_preguntas import escribirArchivoPreguntas, leerArchivoPreguntas

escribirArchivoPreguntas()
preguntas_almacenadas = leerArchivoPreguntas()

pregunta_usuario = input("Cual es tu pregunta?")

for i in range (0, len(preguntas_almacenadas)):
    if pregunta_usuario.lower() == preguntas_almacenadas[i][0].lower(): # El primer valor de la lista numero i = 0 > es el primer lugar
        print(preguntas_almacenadas[i][1])