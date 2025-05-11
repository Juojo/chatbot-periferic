import hashlib, sys

# Variables

ruta_archivo_preguntas = "./preguntas.csv";
ruta_archivo_preguntas_aprendidas = "./preguntasAprendidas.csv";
sha256_correcto = "4ade749a379aa7acf0e45dc184367d57f3b018c99101c950deb89cdeebfacd8a"

campos = ["Pregunta", "Respuesta"]

datos = [
    ["¿Qué es un periférico?", "Es un dispositivo que se conecta a una computadora para enviar o recibir datos."],
    ["¿Un teclado es un periférico?", "Sí, es un periférico de entrada."],
    ["¿El monitor es de entrada o salida?", "Es un periférico de salida."],
    ["¿Para qué sirve el mouse?", "Sirve para controlar el puntero y seleccionar elementos en pantalla."],
    ["¿Un escáner es entrada o salida?", "Es un periférico de entrada."],
    ["¿La impresora es un periférico?", "Sí, es un periférico de salida."],
    ["¿El micrófono es entrada o salida?", "Es un periférico de entrada."],
    ["¿Los auriculares son periféricos?", "Sí, y son de salida."],
    ["¿Una cámara web es de entrada?", "Sí, captura video o imágenes para la computadora."],
    ["¿El disco duro externo es entrada o salida?", "Puede ser ambos, entrada y salida."],
    ["¿El joystick es un periférico?", "Sí, es un periférico de entrada."],
    ["¿Un lector de huellas es periférico?", "Sí, y es de entrada."],
    ["¿Un proyector es de entrada o salida?", "Es un periférico de salida."],
    ["¿El trackpad es un periférico?", "Sí, es de entrada, como el mouse."],
    ["¿Una tableta gráfica es entrada o salida?", "Es un periférico de entrada."],
    ["¿Un lector de DVD es periférico?", "Sí, es de entrada o ambos si graba."],
    ["¿Un módem es un periférico?", "Sí, y permite la conexión a internet."],
    ["¿El panel táctil de una laptop es periférico?", "Sí, es de entrada."],
    ["¿Un sistema de sonido es periférico?", "Sí, es un periférico de salida."],
    ["¿Todos los periféricos son necesarios?", "No, depende del uso de la computadora."],
    ["¿Qué mouse es bueno para jugar?", "Uno con alta DPI y buenos clics, como los Logitech o Razer."],
    ["¿Necesito un buen teclado?", "Sí, uno mecánico mejora la respuesta en juegos."],
    ["¿Qué auriculares uso?", "Unos con buen sonido envolvente, como HyperX o SteelSeries."],
    ["¿Se puede jugar sin joystick?", "Sí, pero para algunos juegos es mejor usar uno."],
    ["¿Sirve un monitor de 60Hz?", "Sí, pero uno de 144Hz o más es mejor para juegos rápidos."],
    ["¿Cuánta velocidad tiene que tener el mouse?", "Depende, pero entre 800 y 1600 DPI es común para juegos."],
    ["¿El teclado tiene que tener luces?", "No es obligatorio, pero ayuda en la oscuridad."],
    ["¿Qué es un mousepad gamer?", "Una alfombrilla grande y suave para mover mejor el mouse."],
    ["¿Sirve una silla gamer?", "Sí, da más comodidad en sesiones largas."],
    ["¿Qué tipo de monitor compro?", "Uno con buena tasa de refresco y baja latencia."],
    ["¿Es necesario un micrófono?", "Sí, para comunicarte en juegos online."],
    ["¿Puedo jugar con auriculares baratos?", "Sí, pero los buenos mejoran la experiencia."],
    ["¿Qué control funciona en PC?", "Casi todos, pero los de Xbox tienen mejor compatibilidad."],
    ["¿Qué es un headset?", "Auriculares con micrófono integrado."],
    ["¿Se puede jugar con teclado de oficina?", "Sí, pero uno gamer es más cómodo y rápido."],
    ["¿Una cámara web sirve para juegos?", "No es necesaria, solo si haces streaming."],
    ["¿Qué monitor usan los gamers?", "De 24 a 27 pulgadas, 144Hz o más, baja respuesta."],
    ["¿Qué es DPI en el mouse?", "Es la sensibilidad, si se aumenta el DPI el cursor se movera mas rapido."],
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
        archivo_preguntas = open(ruta_archivo_preguntas, "w", encoding="utf-8", newline="\n") # Abre o crea el archivo con permisos de escritura

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

def leerArchivoPreguntas(ruta_archivo):
    # La funcion devuele los datos cargados en una matriz para poder ser utilizados directamente desde la memoria
    
    if ruta_archivo == ruta_archivo_preguntas:
        # Se escribe/crea el archivo si no existe o su contenido no es correcto
        if calcularSha256(ruta_archivo_preguntas) != sha256_correcto:
            print("El archivo con las preguntas no existe en el directorio o su contenido no es correcto")
            escribirArchivoPreguntas()
        
    # Lectura
    try:
        archivo_preguntas = open(ruta_archivo, "r") # Abre el archivo como read only
        array_preguntas_respuestas = archivo_preguntas.readlines() # Asigna todas las lineas del archivo en un array, cada linea es un elemento y contiene una pregunta y su respuesta
        
        # Elimina el primer elemento del archivo preguntas (Solo se usa en el csv para indicar los campos)
        if ruta_archivo == ruta_archivo_preguntas:
            array_preguntas_respuestas.pop(0)
        
        matriz_preguntas_respuestas = []
        
        for i in range (0, len(array_preguntas_respuestas)):
            pregunta_respuesta = array_preguntas_respuestas[i].split(";") # Divide el string en un array de dos posiciones. La primera es la pregunta, la segunda la respuesta
        
            matriz_preguntas_respuestas.append(pregunta_respuesta) # Guarda ese array en la ultima posicion de la matriz
        
        return matriz_preguntas_respuestas
    except FileNotFoundError as e:
        if ruta_archivo == ruta_archivo_preguntas_aprendidas:
            print("(No hay preguntas aprendidas de sesiones anteriores)")
            return False
    except Exception as e:
        print("Ocurrio un error con la lectura del archivo:", e)
        sys.exit(1) # Se finaliza el programa si ocurre un error

def agregarPreguntaRespuestaAprendida(pregunta, respuesta):
    # La funcion devuelve True si escribio correctamente los datos
    
    try:
        with open(ruta_archivo_preguntas_aprendidas, "a", encoding="utf-8") as archivo: # Abre el archivo en append mode (Escribe al final del arhivo)
            archivo.write(f"{pregunta};{respuesta}\n")
        print("\nNueva pregunta-respuesta guardada correctamente.")
        print("¡Gracias! He aprendido algo nuevo.\n")
        return True
    except Exception as e:
        print("\nError al guardar la nueva pregunta:", e)
        return False