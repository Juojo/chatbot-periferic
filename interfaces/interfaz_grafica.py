import flet as ft
from interfaces import interfaz_consola

def interfaz_flet_wrapper(preguntas_almacenadas, nombre_chatbot): # Se usa el wrapper para poder pasar los parametros
    def interfaz_flet(page: ft.Page):
        page.title = "Chatbot - Periferic"
        
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        def boton_presionado(e):
            page.snack_bar = ft.SnackBar(content=ft.Text(f"Presionaste: {e.control.text}"))
            page.snack_bar.open = True
            page.update()
            
        def abrir_consola_y_cerrar(e):
            page.window.destroy()  # Se cierra la ventana de flet
            interfaz_consola.ejecutar(preguntas_almacenadas, nombre_chatbot) # Se ejecuta la interfaz de consola

        page.add(
            ft.Text(f"🖥️ Chatbot - {nombre_chatbot}️ 🔌", size=30, weight="bold"),
            
            ft.ElevatedButton(
                "Iniciar una conversacion",
                on_click=boton_presionado,
                width=400,
                height=50,
                style=ft.ButtonStyle(
                    text_style=ft.TextStyle(size=22, weight=ft.FontWeight.BOLD)
                )
            ),
            ft.ElevatedButton(
                content=ft.Column(
                    [
                        ft.Text("Usar la interfaz de consola", size=22, weight=ft.FontWeight.BOLD),
                        ft.Text("(Solo recomendada para desarrollo)", size=16, italic=True),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=5
                ),
                on_click=abrir_consola_y_cerrar,
                width=400,
                height=100
            )
        )
        
    return interfaz_flet # Importante para que funcione el wrapper

def ejecutar(preguntas_almacenadas, nombre_chatbot):
    ft.app(target=interfaz_flet_wrapper(preguntas_almacenadas, nombre_chatbot))