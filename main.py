from logica.manejo_archivo_preguntas import leer_archivo_preguntas
from logica.manejo_archivo_preguntas import ruta_archivo_preguntas, ruta_archivo_preguntas_aprendidas
from logica.puntaje import *
from logica.util import *

from interfaces import interfaz_grafica, interfaz_consola

def almacenar_preguntas_en_memoria(ruta_archivo_preguntas, ruta_archivo_preguntas_aprendidas):
    # Guarda en memoria las preguntas originales
    preguntas_almacenadas = leer_archivo_preguntas(ruta_archivo_preguntas)

    # Intenta agregar preguntas aprendidas en sesiones anteriores
    preguntas_aprendidas = leer_archivo_preguntas(ruta_archivo_preguntas_aprendidas) # Matriz de preguntas aprendidas
    if preguntas_aprendidas != False: # Solo puede ser falso en caso de que no se haya encontrado el archivo con preguntas aprendidas
        for i in range (0, len(preguntas_aprendidas)):
            preguntas_almacenadas.append(preguntas_aprendidas[i]) # Agrega al final de preguntas_almacenadas la pregunta-respuesta aprendida

    # Guarda las preguntas normalizadas + stemizadas, crea el split de palabras clave y calcula el puntaje
    for i in range(0, len(preguntas_almacenadas)):
        pregunta_normalizada_stemizada = normalizar(preguntas_almacenadas[i][0])
        pregunta_normalizada_stemizada = stemizar(pregunta_normalizada_stemizada)
        preguntas_almacenadas[i].append(pregunta_normalizada_stemizada)

        palabras_clave = preguntas_almacenadas[i][2].split()
        preguntas_almacenadas[i].append(palabras_clave)

        preguntas_almacenadas[i].append(calcular_puntaje_lista_palabra(palabras_clave))
        
    return preguntas_almacenadas
    
    # preguntas_almacenadas es una lista de elementos, su tamaño es relativo a la cantidad de preguntas.
    # Cada elemento de esta lista, es otra lista que almacena:
    
    # (0) Pregunta,
    # (1) Respuesta,
    # (2) Pregunta normalizada y stemizada,
    # (3) Lista de palabras clave,
    # (4) Puntaje numerico total de la lista de palabras clave
    
    # Entonces, si se quiere saber cual es la respuesta de la tercer preguta se hace: preguntas_almacenadas[2][1]
    # Y si se quisiera obtener la primer palabra de la lista de palabras claves: preguntas_almacenadas[2][2][0]

def main():
    nombre_chatbot = "Periferic"

    preguntas_almacenadas = almacenar_preguntas_en_memoria(ruta_archivo_preguntas, ruta_archivo_preguntas_aprendidas)
    
    #interfaz_grafica.ejecutar(preguntas_almacenadas, nombre_chatbot)
    interfaz_consola.ejecutar(preguntas_almacenadas, nombre_chatbot)
    
if __name__ == "__main__":
    main()
    