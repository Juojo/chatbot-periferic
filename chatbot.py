from util import *
from manejo_archivo_preguntas import leerArchivoPreguntas, agregarPreguntaRespuestaAprendida
from manejo_archivo_preguntas import ruta_archivo_preguntas, ruta_archivo_preguntas_aprendidas

preguntas_almacenadas = leerArchivoPreguntas(ruta_archivo_preguntas) # Guarda en memoria las preguntas originales

# Intenta agregar preguntas aprendidas en sesiones anteriores
preguntas_aprendidas = leerArchivoPreguntas(ruta_archivo_preguntas_aprendidas) # Matriz de preguntas aprendidas
if preguntas_aprendidas != False: # Solo puede ser falso en caso de que no se haya encontrado el archivo con preguntas aprendidas
    for i in range (0, len(preguntas_aprendidas)):
        preguntas_almacenadas.append(preguntas_aprendidas[i]) # Agrega al final de preguntas_almacenadas la pregunta-respuesta aprendida

nombre_chatbot = "Periferic"

print(f"Hola mi nombre es {nombre_chatbot}, se mucho sobre perifericos y me encataria resolver cualquier duda que tengas relacionada a este tema.")
print()

print("Antes de empezar, ¿como es tu nombre?")
print("Ingrese su nombre acá: ", end="")
nombre = input()

print()

print(f"Ahora si {nombre}, en que puedo ayudarte hoy?")
print("Ingrese su pregunta (o escriba 'salir' si ya no tiene mas preguntas): ", end="")
pregunta_usuario = input()
pregunta_usuario = normalizar(pregunta_usuario)

while pregunta_usuario != "salir":
    pregunta_encontrada=0
    for i in range (0, len(preguntas_almacenadas)):
        if pregunta_usuario == preguntas_almacenadas[i][0]:
            print(f"Respuesta de {nombre_chatbot}: " + preguntas_almacenadas[i][1])
            pregunta_encontrada=1

    if pregunta_encontrada==0:
        print(f"Respuesta de {nombre_chatbot}: Disculpame, no tengo respuesta a tu pregunta.")
        print()
        aprender = input("¿Querés enseñarmela? (si/no): ").strip().lower()
        if aprender == "si":
            nueva_respuesta = input("Por favor, escribí la respuesta: ")
            
            # Guardar en el archivo CSV
            if agregarPreguntaRespuestaAprendida(pregunta_usuario, nueva_respuesta): # Devuelve True si no hay fallas
                # También actualizar la lista en memoria
                preguntas_almacenadas.append((pregunta_usuario, nueva_respuesta + "\n"))              
        else:
            print("Está bien, no hay problema. Si más adelante querés enseñarmela, avisame :)\n")
            
    print("Ingrese su pregunta (o escriba 'salir' si ya no tiene mas preguntas): ", end="")
    pregunta_usuario = input()

print()
print(f"Gracias {nombre} por utilizar nuestro chatbot.")