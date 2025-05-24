from datetime import datetime

ruta_archivo_conversacion = "./informacion_almacenada/log.txt"

def generarArchivoLog():
    try:
        # Intenta crear el archivo solo la primera vez
        with open(ruta_archivo_conversacion, "x", encoding="utf-8", newline="\n") as archivo:
            fecha_hora = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            archivo.write(f"Log de la sesion: {fecha_hora}\n\n")
    except FileExistsError:
        # Si ya existe, abrimos en modo append y escribimos nueva sesión
        with open(ruta_archivo_conversacion, "a", encoding="utf-8", newline="\n") as archivo:
            fecha_hora = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            archivo.write(f"\n\nLog de la sesion: {fecha_hora}\n\n")
    except FileNotFoundError:
        print("El directorio './informacion_almacenada' no existe. Créalo manualmente antes de ejecutar.")
    except Exception as e:
        print("Error al manejar log.txt:", e)

def guardarLog(emisor, texto, nombre_usuario, porcentaje_similitud=0):
    nombre = nombre_usuario
    prefix_log = datetime.now().strftime("[%d-%m-%Y %H:%M:%S]")
    if emisor == "consola":
        registro_txt = str(prefix_log) + " [Periferic] [Porcentaje de similitud: " + str(porcentaje_similitud) + "%] " + texto
        try:
            with open(ruta_archivo_conversacion, "a", encoding="utf-8") as archivo: # Abre el archivo en append mode (Escribe al final del arhivo)
                archivo.write(registro_txt.rstrip() + "\n\n")
            return True
        except Exception as e:
            print("\nError con la generacion de log.txt:", e)
        return False
    elif emisor == "user":
        registro_txt = str(prefix_log) + f" [Usuario: {nombre}] " + texto
        try:
            with open(ruta_archivo_conversacion, "a", encoding="utf-8") as archivo: # Abre el archivo en append mode (Escribe al final del arhivo)
                archivo.write(registro_txt.rstrip() + "\n")
            return True
        except Exception as e:
            print("\nError con la generacion de log.txt:", e)
    else:
        return print("\nError con la generacion de log.txt (emisor incorrecto).")