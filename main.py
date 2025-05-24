from logica.manejo_archivo_preguntas import leer_archivo_preguntas
from logica.manejo_archivo_preguntas import ruta_archivo_preguntas, ruta_archivo_preguntas_aprendidas
from logica.puntaje import *

from interfaces import interfaz_grafica, interfaz_consola

def almacenar_preguntas_en_memoria(ruta_archivo_preguntas, ruta_archivo_preguntas_aprendidas):
    # Guarda en memoria las preguntas originales
    preguntas_almacenadas = leer_archivo_preguntas(ruta_archivo_preguntas)

    # Intenta agregar preguntas aprendidas en sesiones anteriores
    preguntas_aprendidas = leer_archivo_preguntas(ruta_archivo_preguntas_aprendidas) # Matriz de preguntas aprendidas
    if preguntas_aprendidas != False: # Solo puede ser falso en caso de que no se haya encontrado el archivo con preguntas aprendidas
        for i in range (0, len(preguntas_aprendidas)):
            preguntas_almacenadas.append(preguntas_aprendidas[i]) # Agrega al final de preguntas_almacenadas la pregunta-respuesta aprendida

    # Crea el split de palabras clave y calcula el puntaje
    for i in range(0, len(preguntas_almacenadas)):
        palabras_clave = preguntas_almacenadas[i][0].split()
        preguntas_almacenadas[i].append(palabras_clave)
        preguntas_almacenadas[i].append(calcular_puntaje_lista_palabra(palabras_clave))
        
    return preguntas_almacenadas
    
    # preguntas_almacenadas es una lista de elementos, su tamaño es relativo a la cantidad de preguntas.
    # Cada elemento de esta lista, es otra lista que almacena:
    
    # (0) Pregunta normalizada,
    # (1) Respuesta,
    # (2) Lista de palabras clave,
    # (3) Puntaje numerico total de la lista de palabras clave
    # (4) Pregunta original
    
    # Entonces, si se quiere saber cual es la respuesta de la tercer preguta se hace: preguntas_almacenadas[2][1]
    # Y si se quisiera obtener la primer palabra de la lista de palabras claves: preguntas_almacenadas[2][2][0]

def main():
    nombre_chatbot = "Periferic"

    preguntas_almacenadas = almacenar_preguntas_en_memoria(ruta_archivo_preguntas, ruta_archivo_preguntas_aprendidas)
    
    #interfaz_grafica.ejecutar(preguntas_almacenadas, nombre_chatbot)
    interfaz_consola.ejecutar(preguntas_almacenadas, nombre_chatbot)

#     print("Seleccione la interfaz que quiera utilizar:\n")
#     print("1. Interfaz gráfica")
#     print("2. Interfaz por consola (Recomendada solo para desarrollo)")
#     print("\nOpcion seleccionada: ", end="")
# 
#     interfaz_seleccionada = int(input())
# 
#     while interfaz_seleccionada < 1 or interfaz_seleccionada > 2:
#         print("La opcion seleccionada es incorrecta.")
#         interfaz_seleccionada = int(input("Seleccione otra opcion: "))
#         
#     if interfaz_seleccionada == 1:
#         interfaz_grafica.ejecutar(preguntas_almacenadas, nombre_chatbot)
#     elif interfaz_seleccionada == 2:
#         interfaz_consola.ejecutar(preguntas_almacenadas, nombre_chatbot)
    
if __name__ == "__main__":
    main()
    