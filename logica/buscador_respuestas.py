from logica.puntaje import *

def obtener_respuesta(pregunta, preguntas_almacenadas):
    respuesta = buscar_pregunta_exacta(pregunta, preguntas_almacenadas)
    
    if respuesta["contenido_respuesta"] == False:
        respuesta = buscar_pregunta_similar(pregunta, preguntas_almacenadas)
    
    return respuesta

def buscar_pregunta_exacta(pregunta, preguntas_almacenadas):
    # Busca la pregunta pasada por parametros
    # Devuelve el String con la respuesta si la encuentra
    # Si no la encuentra devuelve False
    
    for i in range (0, len(preguntas_almacenadas)):
        if pregunta == preguntas_almacenadas[i][0]:
            return {
                "contenido_respuesta": preguntas_almacenadas[i][1],
                "porcentaje_similitud": False, # No se utiliza
                "cantidad_palabras_usuario": False # No se utiliza
            }
        else:
            return {
                "contenido_respuesta": False,
                "porcentaje_similitud": False, # No se utiliza
                "cantidad_palabras_usuario": False # No se utiliza
            }
        
def buscar_pregunta_similar(pregunta, preguntas_almacenadas):
    # Busca la pregunta que mas se asemeje a la pasada por parametros
    # Devuelve el String con la respuesta si la encuentra y esta sobre el minimo permitido
    # Si no la encuentra devuelve False
    
    palabras_clave_usuario = pregunta.split()
    
    # Calcula puntaje de cada palabra del usuario y lo guarda en puntaje_palabras_usuario
    # Se hace por afuera del siguiente for porque la pregunta del usuario no cambia,
    # solo lo hace la pregunta almacenada con la que esta siendo comparada
    puntaje_palabras_usuario = [] 
    for i in range (0, len(palabras_clave_usuario)):
        puntaje_palabras_usuario.append(calculcarPuntajePalabra(palabras_clave_usuario[i]))
    
    porcentaje_actual = 0.0
    porcentaje_mayor = 0.0
    index_porcentaje_mayor = 0
    
    # Itera sobre todas las preguntas almacenadas y calcula el porcentaje de similitud para cada una
    for i in range (0, len(preguntas_almacenadas)):
        puntaje = 0
        palabras_clave_pregunta_almacenada = preguntas_almacenadas[i][2][:] # [:] -> crea una copia identica de la lista original (No copia elementos mutables)             
        
        # Itera sobre la lista de palabras clave del usuario
        for j in range(0, len(palabras_clave_usuario)):               
            k = 0
            similitud_encontrada = False
            
            # Itera sobre lista palabras claves almacenadas, siempre y cuando no se haya encontrado una similitud
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
                
    # Solo se considera que la pregunta fue encontrada si supera este valor
    if porcentaje_mayor >= 0.75:
        return {
            "contenido_respuesta": preguntas_almacenadas[index_porcentaje_mayor][1],
            "porcentaje_similitud": round(porcentaje_mayor*100, 2),
            "cantidad_palabras_usuario": len(palabras_clave_usuario)
        }
    else:
        return {
            "contenido_respuesta": False, # False porque no se encontro
            "porcentaje_similitud": round(porcentaje_mayor*100, 2),
            "cantidad_palabras_usuario": len(palabras_clave_usuario) # Cantidad de palabras de la pregunta del usuario
        }