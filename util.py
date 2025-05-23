import re
import unicodedata
import difflib
from main.py import preguntas_almacenadas

def normalizar(texto):
    texto = texto.lower()
    texto = unicodedata.normalize('NFD', texto).encode('ascii', 'ignore').decode('utf-8')
    texto = re.sub(r'[^a-z0-9 ]', '', texto)      # Conserva letras, números y espacios
    texto = re.sub(r'\s+', ' ', texto)            # Reemplaza múltiples espacios por uno solo
    texto = texto.strip()                         # Elimina espacios al principio y final
    return texto

def corregir_texto(texto):
    vocabulario = preguntas_almacenadas[2]

    texto_palabras = re.findall(r'\b\w+\b', texto.lower())
    correcciones = {}

    for i in range(len(texto_palabras)):
        palabra = texto_palabras[i]
        if palabra not in vocabulario:
            sugerencias = difflib.get_close_matches(palabra, vocabulario, n=1, cutoff=0.6)
            if sugerencias:
                correcciones[palabra] = sugerencias[0]

    texto_corregido = texto
    for incorrecta, sugerencia in correcciones.items():
        texto_corregido = re.sub(rf'\b{incorrecta}\b', sugerencia, texto_corregido, flags=re.IGNORECASE)

    return texto