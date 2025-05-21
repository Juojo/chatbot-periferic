import re
import unicodedata

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


