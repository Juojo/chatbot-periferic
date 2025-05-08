from manejo_archivo import escribirArchivo, leerArchivo

escribirArchivo()
preguntas_almacenadas = leerArchivo()

pregunta_usuario = input("Cual es tu pregunta?")

for i in range (0, len(preguntas_almacenadas)):
    if pregunta_usuario.lower() == preguntas_almacenadas[i][0].lower(): # El primer valor de la lista numero i = 0 > es el primer lugar
        print(preguntas_almacenadas[i][1])