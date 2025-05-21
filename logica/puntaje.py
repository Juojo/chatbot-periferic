puntaje_bajo = 1
puntaje_alto = 3
puntaje_negativo = -1

palabras_bajo_puntaje = ["a", "que", "el", "la", "los", "las", "un", "una", "de", "en", "o", "y", "para", "con", "sin", "se"]

def calculcarPuntajePalabra(palabra):
    puntaje_total = 0
    
    k = 0
    palabra_bajo_puntaje_encontrada = False
    
    while palabra_bajo_puntaje_encontrada == False and k < len(palabras_bajo_puntaje):
        if palabra == palabras_bajo_puntaje[k]:
            palabra_bajo_puntaje_encontrada = True
            puntaje_total += puntaje_bajo
        k += 1
            
    if palabra_bajo_puntaje_encontrada == False:
        puntaje_total += puntaje_alto
        
    return puntaje_total
            
def calcularPuntajeListaPalabras(listaPalabrasClave):
    puntaje_total = 0
    
    for i in range(len(listaPalabrasClave)):
        puntaje_total += calculcarPuntajePalabra(listaPalabrasClave[i])
            
    return puntaje_total