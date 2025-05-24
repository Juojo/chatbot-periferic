from logica.util import *
from logica.buscador_respuestas import obtener_respuesta
from logica.manejo_archivo_preguntas import agregar_pregunta_respuesta_aprendida
from logica.puntaje import *
from logica.manejo_archivo_logs import generarArchivoLog
from logica.manejo_archivo_logs import guardarLog


def mostrar_presentacion_chatbot(nombre_chatbot):
    input(cambiarColor("Presioná Enter para continuar...\n", "rojo"))
    print("Hola mi nombre es", cambiarColor(nombre_chatbot, "rojo"), "se mucho sobre perifericos y me encataria resolver cualquier duda que tengas relacionada a este tema.\n")

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
 
    guardarLog("user", pregunta, nombre_usuario) # Se guarda la pregunta del usuario en el log.
    
    pregunta = normalizar(pregunta)
    pregunta = stemizar(pregunta)
    
    return pregunta

def mostrar_respuesta(respuesta, nombre_chatbot, nombre_usuario, preguntas_almacenadas):
    # Si solo se devolvio una respuesta
    if len(respuesta["respuestas"]) == 1: 
        print(cambiarColor("Respuesta de " + nombre_chatbot + ": ", "amarillo") + respuesta["respuestas"][0], end="")
        guardarLog("consola", respuesta["respuestas"][0], nombre_usuario, respuesta["porcentajes_similitud"][0]) # Se guarda la respuesta de la consola en el log.
    
    # Si se devolvio mas de una
    else:
        texto_disculpa = "Disculpame, no logre encontrar una respuesta precisa a tu pregunta."
        print(cambiarColor("Respuesta de " + nombre_chatbot + ":", "amarillo"), texto_disculpa, "\n")
        
        # Se guarda la respuesta de la consola en el log.
        #guardarLog("consola", texto_disculpa, nombre_usuario, respuesta["porcentaje_similitud"])

        # Se printea la advertencia de pregunta muy larga
        if respuesta["cantidad_palabras_usuario"] >= 8:
            mostrar_advertencia_pregunta_larga(nombre_usuario)
            
        # Se muestran el menu con las sugerencias y la opcion de enseñar
        mostrar_ingresar_menu_sugerencias(respuesta["preguntas_sugerencia"], respuesta["porcentajes_similitud"], respuesta["respuestas"], respuesta["enseniar_pregunta_usuario"], preguntas_almacenadas, nombre_chatbot, nombre_usuario)

def mostrar_advertencia_pregunta_larga(nombre_usuario):
    print(f"Tu pregunta fue muy larga {nombre_usuario}, si queres podes volver a preguntarmela de una manera mas corta y directa.")
    print("Por ejemplo, si queres saber que es un periferico:")
    print()
    print("Decime: ", cambiarColor("'¿Que es un perifercio?'", "verde"))
    print("No me digas: ", cambiarColor("'Hola ¿como estas? me gustaria saber que es un periferico'", "rojo"))
    print()
    print("De todos modos, capaz me estas preguntando algo que no sepa. Puedo aprender la pregunta que me hiciste si me decis la respuesta.")

def mostrar_ingresar_menu_sugerencias(preguntas_sugeridas, porcentajes_similitudes, respuestas_sugeridas, pregunta_usuario, preguntas_almacenadas, nombre_chatbot, nombre_usuario):
    print("Pero aca te dejo 3 sugerencias que creo que te pueden servir:\n")
    
    print(f"1: ({porcentajes_similitudes[0]}% de similitud) {preguntas_sugeridas[0]}")
    print(f"2: ({porcentajes_similitudes[1]}% de similitud) {preguntas_sugeridas[1]}")
    print(f"3: ({porcentajes_similitudes[2]}% de similitud) {preguntas_sugeridas[2]}")

    print("\nSi ninguna de las sugerencias es adecuada a tu pregunta, tambien me podes enseñar la respuesta\n")

    print("4: Enseñar la respuesta")
    print("5: Hacer otra pregunta\n")
    
    print("Opcion seleccionada: ", end="")
    opcion = int(input())

    while opcion < 1 or opcion > 5:
        print("La opcion seleccionada es incorrecta.")
        opcion = int(input("Seleccione otra opcion: "))
        
    if opcion == 1:
        print(cambiarColor("Respuesta de " + nombre_chatbot + ": ", "amarillo") + respuestas_sugeridas[0])
        guardarLog("consola", ("(Respuesta sugerida) " + respuestas_sugeridas[0]), nombre_usuario, porcentajes_similitudes[0])
    elif opcion == 2:
        print(cambiarColor("Respuesta de " + nombre_chatbot + ": ", "amarillo") + respuestas_sugeridas[1])
        guardarLog("consola", ("(Respuesta sugerida) " + respuestas_sugeridas[1]), nombre_usuario, porcentajes_similitudes[1])
    elif opcion == 3:
        print(cambiarColor("Respuesta de " + nombre_chatbot + ": ", "amarillo") + respuestas_sugeridas[2])
        guardarLog("consola", ("(Respuesta sugerida) " + respuestas_sugeridas[2]), nombre_usuario, porcentajes_similitudes[2])
    elif opcion == 4:
        ingresar_enseniar(pregunta_usuario, preguntas_almacenadas)
    elif opcion == 5:
        guardarLog("consola", "(No se encontro respuesta y el usuario no selecciono ninguna sugerencia)", nombre_usuario, 0)
    
def ingresar_enseniar(pregunta_usuario, preguntas_almacenadas):
    nueva_respuesta = input("Por favor, escribí la respuesta: ")
    
    # Guardar en el archivo CSV
    if agregar_pregunta_respuesta_aprendida(pregunta_usuario, nueva_respuesta): # Devuelve True si no hay fallas
        print("\nNueva pregunta-respuesta guardada correctamente.")
        print("¡Gracias! He aprendido algo nuevo.")
        # También actualizar la lista en memoria
        preguntas_almacenadas.append((stemizar(pregunta_usuario), nueva_respuesta + "\n", pregunta_usuario.split(), calcular_puntaje_lista_palabra(pregunta_usuario.split())))

def ejecutar(preguntas_almacenadas, nombre_chatbot):
    mostrar_presentacion_chatbot(nombre_chatbot)
    nombre_usuario = preguntar_ingresar_nombre_usuario()

    print("\nAhora si", cambiarColor(nombre_usuario, "verde"), "en que puedo ayudarte hoy?")
    generarArchivoLog() # Generamos el archivo log para que empiece a guardar la interaccion del usuario con el bot.
    pregunta_usuario = ingresar_pregunta_usuario(nombre_usuario)

    while pregunta_usuario != stemizar("salir"):
        respuesta = obtener_respuesta(pregunta_usuario, preguntas_almacenadas) # Se busca la respuesta
        mostrar_respuesta(respuesta, nombre_chatbot, nombre_usuario, preguntas_almacenadas) # Se muestra por pantalla
        
        pregunta_usuario = ingresar_pregunta_usuario(nombre_usuario) # El usuario ingresa una nueva pregunta

    mostrar_fin_programa(nombre_usuario)
