from datetime import datetime

fecha_hora = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

ruta_archivo_logs = f"./informacion_almacenada/logs_historial/conversacion_{fecha_hora}.log";

def generarArchivoLog():
    print("Se esta generando el archivo '" + ruta_archivo_logs + "'")

    try:
        with open(ruta_archivo_logs, "w", encoding="utf-8", newline="\n") as archivo: # Crea el archivo con permisos de escritura
            fecha_hora_mostrada = fecha_hora
            archivo.write(f"Log creado el {fecha_hora_mostrada}\n\n")
    except Exception as e:
        print("\nError con la generación de conversacion.log:", e)

def guardarLog(emisor, texto, nombre_usuario):
    nombre = nombre_usuario
    prefix_log = datetime.now().strftime("[%d-%m-%Y %H:%M:%S]")
    if emisor == "consola":
        registro_txt = str(prefix_log) + " [Consola] " + texto
        try:
            with open(ruta_archivo_logs, "a", encoding="utf-8") as archivo: # Abre el archivo en append mode (Escribe al final del arhivo)
                archivo.write(registro_txt + "\n")
            return True
        except Exception as e:
            print("\nError con la generacion de conversacion.log:", e)
        return False
    elif emisor == "user":
        registro_txt = str(prefix_log) + f" [Usuario: {nombre}] " + texto
        try:
            with open(ruta_archivo_logs, "a", encoding="utf-8") as archivo: # Abre el archivo en append mode (Escribe al final del arhivo)
                archivo.write(registro_txt + "\n")
            return True
        except Exception as e:
            print("\nError con la generacion de conversacion.log:", e)
    else:
        return print("\nError con la generacion de conversacion.log (emisor incorrecto).")
