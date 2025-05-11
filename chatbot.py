import re
import unicodedata
from manejo_archivo_preguntas import leerArchivoPreguntas, agregarPreguntaRespuestaAprendida
from manejo_archivo_preguntas import ruta_archivo_preguntas, ruta_archivo_preguntas_aprendidas

preguntas_almacenadas = leerArchivoPreguntas(ruta_archivo_preguntas) # Guarda en memoria las preguntas originales

# Intenta agregar preguntas aprendidas en sesiones anteriores
preguntas_aprendidas = leerArchivoPreguntas(ruta_archivo_preguntas_aprendidas) # Matriz de preguntas aprendidas
if preguntas_aprendidas != False: # Solo puede ser falso en caso de que no se haya encontrado el archivo con preguntas aprendidas
    for i in range (0, len(preguntas_aprendidas)):
        preguntas_almacenadas.append(preguntas_aprendidas[i]) # Agrega al final de preguntas_almacenadas la pregunta-respuesta aprendida

def normalizar(texto):
    texto = texto.lower()
    #La funcion convierte todo el texto a minúsculas.
    
    texto = unicodedata.normalize('NFD', texto).encode('ascii', 'ignore').decode('utf-8')
    #Esta función descompone los caracteres con acento e ignroa todo lo que no sea ASCII para luego volverlo a convertir en str.
    
    
    texto = re.sub(r'[^a-z0-9]', '', texto)
    #Busca todo caracter que no sea una letra minuscula o un numero y lo elimina.
    return texto

print("Hola mi nombre es CHATBOT, se mucho sobre perifericos y me encataria resolver cualquier duda que tengas relacionada a este tema.")
print()

print("Antes de empezar, ¿como es tu nombre?")
print("Ingrese su nombre acá: ", end="")
nombre = input()

print()

print(f"Ahora si {nombre}, en que puedo ayudarte hoy?")
print("Ingrese su pregunta (o escriba 'salir' si ya no tiene mas pregutas): ", end="")
pregunta_usuario = input()

while pregunta_usuario != "salir":
    pregunta_encontrada=0
    for i in range (0, len(preguntas_almacenadas)):
        if normalizar(pregunta_usuario) == normalizar(preguntas_almacenadas[i][0]): # El primer valor de la lista numero i = 0 > es el primer lugar
            print("Respuesta de CHATBOT: " + preguntas_almacenadas[i][1])
            pregunta_encontrada=1

    if pregunta_encontrada==0:
        print("Respuesta de CHATBOT: Disculpame, no tengo respuesta a tu pregunta.")
        print()
        aprender = input("¿Querés enseñarmela? (si/no): ").strip().lower()
        if aprender == "si":
            nueva_respuesta = input("Por favor, escribí la respuesta: ")
            
            # Guardar en el archivo CSV
            if agregarPreguntaRespuestaAprendida(pregunta_usuario, nueva_respuesta): # Devuelve True si no hay fallas
                # También actualizar la lista en memoria
                preguntas_almacenadas.append((pregunta_usuario, nueva_respuesta))              
        else:
            print("Está bien, no hay problema. Si más adelante querés enseñarmela, avisame :)\n")
            
    print("Ingrese su pregunta (o escriba 'salir' si ya no tiene mas pregutas): ", end="")
    pregunta_usuario = input()

print()
print(f"Gracias {nombre} por utilizar nuestro chatbot.")