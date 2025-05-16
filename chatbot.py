from util import *
from manejo_archivo_preguntas import leerArchivoPreguntas, agregarPreguntaRespuestaAprendida
from manejo_archivo_preguntas import ruta_archivo_preguntas, ruta_archivo_preguntas_aprendidas

preguntas_almacenadas = leerArchivoPreguntas(ruta_archivo_preguntas) # Guarda en memoria las preguntas originales

# Intenta agregar preguntas aprendidas en sesiones anteriores
preguntas_aprendidas = leerArchivoPreguntas(ruta_archivo_preguntas_aprendidas) # Matriz de preguntas aprendidas
if preguntas_aprendidas != False: # Solo puede ser falso en caso de que no se haya encontrado el archivo con preguntas aprendidas
    for i in range (0, len(preguntas_aprendidas)):
        preguntas_almacenadas.append(preguntas_aprendidas[i]) # Agrega al final de preguntas_almacenadas la pregunta-respuesta aprendida

# Palabras clave
for i in range(0, len(preguntas_almacenadas)):
    palabras_clave = preguntas_almacenadas[i][0].split()
    preguntas_almacenadas[i].append(palabras_clave)

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
    calculo_porcentaje_actual = 0.0
    porcentaje_mayor = 0.0
    index_porcentaje_mayor = 0
    palabras_clave_usuario = pregunta_usuario.split()
    
    for i in range (0, len(preguntas_almacenadas)): # Itera sobre todas las pregunta-respuesta
        
        if pregunta_usuario == preguntas_almacenadas[i][0]: # Compara si la pregunta del usuario es identica a la pregunta almacenda
            print(f"Respuesta de {nombre_chatbot}: " + preguntas_almacenadas[i][1])
            pregunta_encontrada=1
        else:
            # Si no es identica, se calcula el porcentaje de similitud entre las palabras clave de la pregunta del usuario y la almacenada
            cont_similitud = 0
            palabras_clave_pregunta_almacenada = preguntas_almacenadas[i][2][:] # [:] -> crea una copia identica de la lista original (No copia elementos mutables)
            len_palabras_clave_pregunta_almacenada = len(palabras_clave_pregunta_almacenada)
            
            for j in range(0, len(palabras_clave_usuario)): # Itera sobre lista de PC usuario
                k = 0
                similitud_encontrada = False
                while similitud_encontrada == False and k < len(palabras_clave_pregunta_almacenada): # Itera sobre lista PC almacenadas, siempre y cuando no se haya encontrado una similitud
                    if palabras_clave_usuario[j] == palabras_clave_pregunta_almacenada[k]:
                        cont_similitud += 1
                        palabras_clave_pregunta_almacenada.pop(k) # Elimina el elemento encontrado para que no matchee otra vez
                        similitud_encontrada = True
                    k += 1
            
            # Calculo de porcentaje
            if cont_similitud != 0:
                calculo_porcentaje_actual = cont_similitud / len_palabras_clave_pregunta_almacenada # 1=100%, 0.5=50%, etc
                
                if calculo_porcentaje_actual > porcentaje_mayor:
                    porcentaje_mayor = calculo_porcentaje_actual
                    index_porcentaje_mayor = i
    
    print(porcentaje_mayor)
    if porcentaje_mayor >= 0.70:
        print(f"Respuesta de {nombre_chatbot}: " + preguntas_almacenadas[index_porcentaje_mayor][1])
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
    pregunta_usuario = normalizar(pregunta_usuario)

print()
print(f"Gracias {nombre} por utilizar nuestro chatbot.")