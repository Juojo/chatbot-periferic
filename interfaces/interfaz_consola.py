from logica.util import *
from logica.buscador_respuestas import obtener_respuesta
from logica.manejo_archivo_preguntas import agregar_pregunta_respuesta_aprendida
from logica.puntaje import *
from logica.manejo_archivo_logs import generarArchivoLog
from logica.manejo_archivo_logs import guardarLog


def mostrar_presentacion_chatbot(nombre_chatbot):
    print("\nHola mi nombre es", cambiarColor(nombre_chatbot, "rojo"), "se mucho sobre perifericos y me encataria resolver cualquier duda que tengas relacionada a este tema.\n")

def mostrar_fin_programa(nombre_usuario):
    print("Gracias", cambiarColor(nombre_usuario, "verde"), "por utilizar nuestro chatbot.")

def preguntar_ingresar_nombre_usuario():
    print("Antes de empezar, " + cambiarColor("¿como es tu nombre?", "amarillo"))
    print("Ingrese su nombre acá: ", end="")
    nombre = input()
    
    return nombre

def ingresar_pregunta_usuario(nombre_usuario):
    print(cambiarColor("\nIngrese su pregunta", "amarillo"), "(o escriba", cambiarColor("'salir'", "rojo"), "si ya no tiene mas preguntas): ",  end="")
    pregunta = input()
    pregunta = normalizar(pregunta)
    guardarLog("user", pregunta, nombre_usuario) # Se guarda la pregunta del usuario en el log.
    
    return pregunta

def mostrar_advertencia_pregunta_larga(nombre_usuario):
    print(f"Tu pregunta fue muy larga {nombre_usuario}, si queres podes volver a preguntarmela de una manera mas corta y directa.")
    print("Por ejemplo, si queres saber que es un periferico:")
    print()
    print("Decime: ", cambiarColor("'¿Que es un perifercio?'", "verde"))
    print("No me digas: ", cambiarColor("'Hola ¿como estas? me gustaria saber que es un periferico'", "rojo"))
    print()
    print("De todos modos, capaz me estas preguntando algo que no sepa. Puedo aprender la pregunta que me hiciste si me decis la respuesta.")

def mostrar_ingresar_enseniar(pregunta_usuario, preguntas_almacenadas):
    aprender = input("¿Querés enseñarmela? (si/no): ").strip().lower()
    if aprender == "si":
        nueva_respuesta = input("Por favor, escribí la respuesta: ")
        
        # Guardar en el archivo CSV
        if agregar_pregunta_respuesta_aprendida(pregunta_usuario, nueva_respuesta): # Devuelve True si no hay fallas
            print("\nNueva pregunta-respuesta guardada correctamente.")
            print("¡Gracias! He aprendido algo nuevo.")
            # También actualizar la lista en memoria
            preguntas_almacenadas.append((pregunta_usuario, nueva_respuesta + "\n", pregunta_usuario.split(), calcular_puntaje_lista_palabra(pregunta_usuario.split())))
    else:
        print("Está bien, no hay problema. Si más adelante querés enseñarmela, avisame :)\n")

def mostrar_respuesta(respuesta, nombre_chatbot, nombre_usuario, preguntas_almacenadas):
    if respuesta["contenido_respuesta"] == False: # Es falsa solo si no se encontro respuesta
        texto_disculpa = "Disculpame, no tengo respuesta a tu pregunta."
        print(cambiarColor("Respuesta de " + nombre_chatbot + ":", "amarillo"), texto_disculpa, "\n")
        guardarLog("consola", texto_disculpa, nombre_usuario) # Se guarda la respuesta de la consola en el log.

        if respuesta["cantidad_palabras_usuario"] >= 10:
            mostrar_advertencia_pregunta_larga(nombre_usuario)

        mostrar_ingresar_enseniar(respuesta["pregunta_usuario"], preguntas_almacenadas)
    else: # Caso contrario se encontro una respuesta
        print(cambiarColor("Respuesta de " + nombre_chatbot + ": ", "amarillo") + respuesta["contenido_respuesta"], end="")
        guardarLog("consola", respuesta["contenido_respuesta"], nombre_usuario) # Se guarda la respuesta de la consola en el log.


def ejecutar(preguntas_almacenadas, nombre_chatbot):
    mostrar_presentacion_chatbot(nombre_chatbot)
    nombre_usuario = preguntar_ingresar_nombre_usuario()

    print("\nAhora si", cambiarColor(nombre_usuario, "verde"), "en que puedo ayudarte hoy?")
    generarArchivoLog() # Generamos el archivo log para que empiece a guardar la interaccion del usuario con el bot.
    pregunta_usuario = ingresar_pregunta_usuario(nombre_usuario)

    while pregunta_usuario != "salir":
        respuesta = obtener_respuesta(pregunta_usuario, preguntas_almacenadas) # Se busca la respuesta
        mostrar_respuesta(respuesta, nombre_chatbot, nombre_usuario, preguntas_almacenadas) # Se muestra por pantalla
        
        pregunta_usuario = ingresar_pregunta_usuario(nombre_usuario) # El usuario ingresa una nueva pregunta

    mostrar_fin_programa(nombre_usuario)
