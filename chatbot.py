import re
import unicodedata
from manejo_archivo_preguntas import leerArchivoPreguntas

preguntas_almacenadas = leerArchivoPreguntas()

def normalizar(texto):
    texto = texto.lower()
    #La funcion convierte todo el texto a minúsculas.
    
    texto = unicodedata.normalize('NFD', texto).encode('ascii', 'ignore').decode('utf-8')
    #Esta función descompone los caracteres con acento e ignroa todo lo que no sea ASCII para luego volverlo a convertir en str.
    
    
    texto = re.sub(r'[^a-z0-9]', '', texto)
    #Busca todo caracter que no sea una letra minuscula o un numero y lo elimina.
    return texto
pregunta_encontrada=0
print("Buenas, yo soy un chat bot, voy a estar respondiendo tus preguntas sobre perifericos.")
print("Como es tu nombre?")
print("Ingrese su nombre: ", end="")
nombre=input()
print()
print(f"Buenas {nombre}, en que puedo ayudarte hoy?")
print("Escribe 'salir' para finalizar. Cual es tu pregunta: ", end="")
pregunta_usuario = input()
while pregunta_usuario != "salir":
    pregunta_encontrada=0
    for i in range (0, len(preguntas_almacenadas)):
        if normalizar(pregunta_usuario) == normalizar(preguntas_almacenadas[i][0]): # El primer valor de la lista numero i = 0 > es el primer lugar
            print(preguntas_almacenadas[i][1])
            pregunta_encontrada=1
    if pregunta_encontrada==0:
        print()
        print("Disculpame, no tengo respuesta a tu pregunta. Queres enseniarmela?")
        print()
            
    print("Escribe 'salir' para finalizar. Cual es tu pregunta: ", end="")
    pregunta_usuario = input()
print(f"Gracias {nombre} por utilizar nuestro chatbot.")