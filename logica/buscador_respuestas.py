from logica.puntaje import *
from logica.util import *

def obtener_respuesta(pregunta, preguntas_almacenadas, pregunta_original):
    respuesta = buscar_pregunta_exacta(pregunta, preguntas_almacenadas)
    
    if respuesta["respuestas"] == False:
        respuesta = buscar_pregunta_similar(pregunta, preguntas_almacenadas, pregunta_original)
    
    return respuesta

def buscar_pregunta_exacta(pregunta, preguntas_almacenadas):
    # Busca la pregunta pasada por parametros
    # Devuelve el String con la respuesta si la encuentra
    # Si no la encuentra devuelve False
    
    for i in range (0, len(preguntas_almacenadas)):
        if pregunta == preguntas_almacenadas[i][2]:
            return {
                "respuestas":
                [
                    preguntas_almacenadas[i][1]
                ],
                "pregunta_usuario": False,
                "porcentajes_similitud": 1*100,
                "cantidad_palabras_usuario": False, # No se utiliza
            }
        else:
            return {
                "respuestas": False,
                "pregunta_usuario": False,
                "porcentajes_similitud": 0*100,
                "cantidad_palabras_usuario": False # No se utiliza
            }
        
def buscar_pregunta_similar(pregunta, preguntas_almacenadas, pregunta_original):
    # Busca la pregunta que mas se asemeje a la pasada por parametros
    # Devuelve el String con la respuesta si la encuentra y esta sobre el minimo permitido
    # Si no la encuentra devuelve False
    
    palabras_clave_usuario = pregunta.split()
    
    # Calcula puntaje de cada palabra del usuario y lo guarda en puntaje_palabras_usuario
    # Se hace por afuera del siguiente for porque la pregunta del usuario no cambia,
    # solo lo hace la pregunta almacenada con la que esta siendo comparada
    puntaje_palabras_usuario = [] 
    for i in range (0, len(palabras_clave_usuario)):
        puntaje_palabras_usuario.append(calcular_puntaje_palabra(palabras_clave_usuario[i]))
    
    porcentaje_actual = 0.0
    porcentajes_mayores = [0.0, 0.0, 0.0]
    index_porcentajes_mayores = [-1, -1, -1]
    
    # Itera sobre todas las preguntas almacenadas y calcula el porcentaje de similitud para cada una
    for i in range (0, len(preguntas_almacenadas)):
        puntaje = 0
        palabras_clave_pregunta_almacenada = preguntas_almacenadas[i][3][:] # [:] -> crea una copia identica de la lista original (No copia elementos mutables)             
        
        # Itera sobre la lista de palabras clave del usuario
        for j in range(0, len(palabras_clave_usuario)):               
            k = 0
            similitud_encontrada = False
            
            # Itera sobre lista palabras claves almacenadas, siempre y cuando no se haya encontrado una similitud
            while k < len(palabras_clave_pregunta_almacenada) and similitud_encontrada == False:
                # Se busca que la palabra sea identica o que pase el calculo de difflib
                if palabras_clave_usuario[j] == palabras_clave_pregunta_almacenada[k] or calcular_difflib(palabras_clave_usuario[j], palabras_clave_pregunta_almacenada[k]):
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
            porcentaje_actual = puntaje / preguntas_almacenadas[i][4] # Devuelve un valor entre 0.0 y 1.0
            
            # Actualiza los porcentajes_mayores y sus respectivos index
            if porcentaje_actual > porcentajes_mayores[0]:
                porcentajes_mayores[0] = porcentaje_actual
                index_porcentajes_mayores[0] = i
                
            elif porcentaje_actual > porcentajes_mayores[1]:
                porcentajes_mayores[1] = porcentaje_actual
                index_porcentajes_mayores[1] = i
                
            elif porcentaje_actual > porcentajes_mayores[2]:
                porcentajes_mayores[2] = porcentaje_actual
                index_porcentajes_mayores[2] = i
                
    # Solo se considera que la pregunta fue encontrada si supera este valor
    if porcentajes_mayores[0] >= 0.75: # Si el porcentaje mayor supera el minimo permitido
        return {
            "respuestas":
            [
                preguntas_almacenadas[index_porcentajes_mayores[0]][1]
            ],
            "pregunta_usuario": False,
            "porcentajes_similitud": [round(porcentajes_mayores[0]*100, 2)],
            "cantidad_palabras_usuario": len(palabras_clave_usuario)
        }
    else:
        return {
            # Lista de las 3 mejores respuestas sugeridas
            "respuestas":
            [
                preguntas_almacenadas[index_porcentajes_mayores[0]][1],
                preguntas_almacenadas[index_porcentajes_mayores[1]][1],
                preguntas_almacenadas[index_porcentajes_mayores[2]][1]
            ],
            # Se usan para el print de preguntas sugeridas
            "preguntas_sugerencia":
            [
                preguntas_almacenadas[index_porcentajes_mayores[0]][0],
                preguntas_almacenadas[index_porcentajes_mayores[1]][0],
                preguntas_almacenadas[index_porcentajes_mayores[2]][0]
            ],
            # Se usan para el print de preguntas sugeridas
            "porcentajes_similitud":
            [
                round(porcentajes_mayores[0]*100, 2),
                round(porcentajes_mayores[1]*100, 2),
                round(porcentajes_mayores[2]*100, 2)
            ],
            # Se usa para guardar la pregunta del usuario en caso de ser aprendida
            "enseniar_pregunta_usuario": pregunta_original,
            # Se usa para mostrar advertencia en caso de escribir muchas palabras y no encontrar respuesta
            "cantidad_palabras_usuario": len(palabras_clave_usuario)
        }