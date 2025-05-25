import flet as ft

from interfaces.pantallas_interfaz_grafica.inicio import iniciar_pantalla_inicio

def interfaz_flet_wrapper(preguntas_almacenadas, nombre_chatbot): # Se usa el wrapper para poder pasar los parametros de ejecutar()
    def interfaz_flet(page: ft.Page):
        page.title = "Chatbot - Periferic"

        iniciar_pantalla_inicio(page, preguntas_almacenadas, nombre_chatbot)
    return interfaz_flet # Importante para que funcione el wrapper

def ejecutar(preguntas_almacenadas, nombre_chatbot):
    ft.app(target=interfaz_flet_wrapper(preguntas_almacenadas, nombre_chatbot))