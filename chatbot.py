from util import *
from manejo_archivo_preguntas import leerArchivoPreguntas, agregarPreguntaRespuestaAprendida
from manejo_archivo_preguntas import ruta_archivo_preguntas, ruta_archivo_preguntas_aprendidas
from puntaje import *

nombre_chatbot = "Periferic"

# <-- Funciones de chatbot.py -->

def almacenarPreguntasEnMemoria():
    # Guarda en memoria las preguntas originales
    preguntas_almacenadas = leerArchivoPreguntas(ruta_archivo_preguntas)

    # Intenta agregar preguntas aprendidas en sesiones anteriores
    preguntas_aprendidas = leerArchivoPreguntas(ruta_archivo_preguntas_aprendidas) # Matriz de preguntas aprendidas
    if preguntas_aprendidas != False: # Solo puede ser falso en caso de que no se haya encontrado el archivo con preguntas aprendidas
        for i in range (0, len(preguntas_aprendidas)):
            preguntas_almacenadas.append(preguntas_aprendidas[i]) # Agrega al final de preguntas_almacenadas la pregunta-respuesta aprendida

    # Crea el split de palabras clave y calcula el puntaje
    for i in range(0, len(preguntas_almacenadas)):
        palabras_clave = preguntas_almacenadas[i][0].split()
        preguntas_almacenadas[i].append(palabras_clave)
        preguntas_almacenadas[i].append(calcularPuntajeListaPalabras(palabras_clave))
        
    return preguntas_almacenadas
    
    # preguntas_almacenadas es una lista de elementos, su tamaño es relativo a la cantidad de preguntas.
    # Cada elemento de esta lista, es otra lista que almacena:
    
    # (0) Pregunta normalizada,
    # (1) Respuesta,
    # (2) Lista de palabras clave,
    # (3) Puntaje numerico total de la lista de palabras clave
    
    # Entonces, si se quiere saber cual es la respuesta de la tercer preguta se hace: preguntas_almacenadas[2][1]
    # Y si se quisiera obtener la primer palabra de la lista de palabras claves: preguntas_almacenadas[2][2][0]

def preguntarIngresarNombreUsuario():
    print("Antes de empezar, ¿como es tu nombre?")
    print("Ingrese su nombre acá: ", end="")
    nombre = input()
    
    return nombre

def ingresarPreguntaUsuario():
    print("Ingrese su pregunta (o escriba 'salir' si ya no tiene mas preguntas): ", end="")
    pregunta = input()
    pregunta = normalizar(pregunta)
    
    return pregunta

# <-- Inicio del programa -->

# Lee los archivos .csv con las preguntas almacenadas y las guarda en memoria
preguntas_almacenadas = almacenarPreguntasEnMemoria()

print(f"Hola mi nombre es {nombre_chatbot}, se mucho sobre perifericos y me encataria resolver cualquier duda que tengas relacionada a este tema.")
print()

nombre_usuario = preguntarIngresarNombreUsuario()
print()

print(f"Ahora si {nombre_usuario}, en que puedo ayudarte hoy?")
pregunta_usuario = ingresarPreguntaUsuario()

# Entra en el ciclo principal del programa
while pregunta_usuario != "salir":
    
    pregunta_encontrada=0
    porcentaje_actual = 0.0
    porcentaje_mayor = 0.0
    index_porcentaje_mayor = 0
    
    palabras_clave_usuario = pregunta_usuario.split()
    
    # Calcula puntaje de cada palabra del usuario y lo guarda en puntaje_palabras_usuario
    puntaje_palabras_usuario = [] 
    for i in range (0, len(palabras_clave_usuario)):
        puntaje_palabras_usuario.append(calculcarPuntajePalabra(palabras_clave_usuario[i]))
    
    # Itera sobre todas las preguntas en busqueda de una coincidencia
    for i in range (0, len(preguntas_almacenadas)):
        
        # Compara si la pregunta del usuario es identica a la pregunta almacenda
        if pregunta_usuario == preguntas_almacenadas[i][0]:
            print(f"Respuesta de {nombre_chatbot}: " + preguntas_almacenadas[i][1])
            pregunta_encontrada=1
            
        # Si no es identica, se calcula el porcentaje de similitud entre las palabras clave de la pregunta del usuario y la almacenada
        else:
            puntaje = 0
            palabras_clave_pregunta_almacenada = preguntas_almacenadas[i][2][:] # [:] -> crea una copia identica de la lista original (No copia elementos mutables)             
            
            # Itera sobre la lista de palabras clave del usuario
            for j in range(0, len(palabras_clave_usuario)):               
                # Itera sobre lista palabras claves almacenadas, siempre y cuando no se haya encontrado una similitud
                k = 0
                similitud_encontrada = False
                while k < len(palabras_clave_pregunta_almacenada) and similitud_encontrada == False:
                    # Si encuentra similitud
                    if palabras_clave_usuario[j] == palabras_clave_pregunta_almacenada[k]:
                        puntaje += puntaje_palabras_usuario[j] # Suma puntaje
                        palabras_clave_pregunta_almacenada.pop(k) # Elimina el elemento encontrado para que no matchee otra vez
                        similitud_encontrada = True # Sale del while
                    k += 1
                # Si no se encontro ninguna similitud para la palabra luego de recorrer todas las palabras_clave_pregunta_almacenada
                if similitud_encontrada == False and k == len(palabras_clave_pregunta_almacenada):
                    puntaje += puntaje_negativo # Resta puntaje
            
            # Se calcula el porcentaje de similitud con la pregunta almacenada (siempre y cuando sea mayor a cero)
            if puntaje > 0:
                # Se divide el puntaje sumado entre el puntaje maximo posible de la pregunta
                porcentaje_actual = puntaje / preguntas_almacenadas[i][3] # Devuelve un valor entre 0.0 y 1.0
                
                # Actualiza porcentaje_mayor e index
                if porcentaje_actual > porcentaje_mayor:
                    porcentaje_mayor = porcentaje_actual
                    index_porcentaje_mayor = i
    
    print(porcentaje_mayor) # Borrar
    if porcentaje_mayor >= 0.75:
        print(f"Respuesta de {nombre_chatbot}: " + preguntas_almacenadas[index_porcentaje_mayor][1], end="")
        print("Estoy un", round(porcentaje_mayor*100, 2), "% seguro de mi respuesta")
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
    
    # Se pide una nueva pregunta para seguir con el ciclo
    pregunta_usuario = ingresarPreguntaUsuario()

# Fin del programa
print()
print(f"Gracias {nombre_usuario} por utilizar nuestro chatbot.")