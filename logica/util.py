import re
import unicodedata
import snowballstemmer
import difflib

stemmer = snowballstemmer.stemmer('spanish');

def normalizar(texto):
    texto = texto.lower()
    texto = unicodedata.normalize('NFD', texto).encode('ascii', 'ignore').decode('utf-8')
    texto = re.sub(r'[^a-z0-9 ]', '', texto)      # Conserva letras, números y espacios
    texto = re.sub(r'\s+', ' ', texto)            # Reemplaza múltiples espacios por uno solo
    texto = texto.strip()                         # Elimina espacios al principio y final
    return texto

def cambiarColor(texto, color):
    codigo_color = 0
    if color == "rojo":
        codigo_color = 31
    elif color == "verde":
        codigo_color = 32
    elif color == "amarillo":
        codigo_color = 33
    elif color == "azul":
        codigo_color = 34
    elif color == "blanco":
        codigo_color = 37
    else:
        codigo_color = 39

    return ("\033[" + str(codigo_color) + "m" + texto + "\033[0m")

def stemizar(texto):
    palabras_stemizadas = stemmer.stemWords(texto.split()); # Aplica stemizacion al texto y lo separa con split
    return " ".join(palabras_stemizadas) # Junta las palabras y las devuelve como un texto stemizado

def calcular_difflib(palabra1, palabra2):
    longitud_palabra = len(palabra1)
    
    if longitud_palabra <= 3:
        similitud_minima = 0.65
    elif longitud_palabra <= 6:
        similitud_minima = 0.75
    elif longitud_palabra <= 9:
        similitud_minima = 0.80
    else:
        similitud_minima = 0.85
    
    
    similitud_palabra = difflib.SequenceMatcher(None, palabra1, palabra2).ratio() # Calcula que tan parecidas son las palabras
    
    if similitud_palabra > similitud_minima:
        return True
    else:
        return False
