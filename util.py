import re
import unicodedata

def normalizar(texto):
    texto = texto.lower()
    texto = unicodedata.normalize('NFD', texto).encode('ascii', 'ignore').decode('utf-8')
    texto = re.sub(r'[^a-z0-9 ]', '', texto)      # Conserva letras, números y espacios
    texto = re.sub(r'\s+', ' ', texto)            # Reemplaza múltiples espacios por uno solo
    texto = texto.strip()                         # Elimina espacios al principio y final
    return texto