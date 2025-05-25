import flet as ft

from interfaces import interfaz_consola
from interfaces.pantallas_interfaz_grafica.chat import iniciar_pantalla_chat

# Pantalla de inicio del programa

def iniciar_pantalla_inicio(page, preguntas_almacenadas, nombre_chatbot):
    page.controls.clear() # Limpia la pantalla anterior

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def cambiar_pantalla_chat(e):
        page.controls.clear() # Limpia la pantalla anterior
        iniciar_pantalla_chat(page, preguntas_almacenadas, nombre_chatbot)
        page.update()

    def inicar_interfaz_consola(e):
        page.window.destroy()  # Se cierra la ventana de flet
        interfaz_consola.ejecutar(preguntas_almacenadas, nombre_chatbot) # Se ejecuta la interfaz de consola

    page.add(
        ft.Text(f"🖥️ Chatbot - {nombre_chatbot}️ 🔌", size=30, weight="bold"),
        
        ft.ElevatedButton(
            "Iniciar una conversacion",
            on_click=cambiar_pantalla_chat,
            width=400,
            height=50,
            style=ft.ButtonStyle(
                text_style=ft.TextStyle(size=22, weight=ft.FontWeight.BOLD)
            )
        ),
        ft.ElevatedButton(
            content=ft.Container( # El container se usa para poder darle un padding al boton
                content=ft.Column(
                    [
                        ft.Text("Usar la interfaz de consola", size=22, weight=ft.FontWeight.BOLD),
                        ft.Text("(Solo recomendada para desarrollo)", size=16, italic=True),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=5,
                ),
                padding=ft.padding.symmetric(vertical=10)
            ),
            on_click=inicar_interfaz_consola,
            width=400,
        )
    )