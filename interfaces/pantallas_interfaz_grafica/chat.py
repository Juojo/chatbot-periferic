import flet as ft

from logica.util import *
from logica.buscador_respuestas import obtener_respuesta
from logica.manejo_archivo_preguntas import agregar_pregunta_respuesta_aprendida
from logica.puntaje import *


from logica.manejo_archivo_logs import guardarLog

def iniciar_pantalla_chat(page, preguntas_almacenadas, nombre_chatbot):
    nombre_usuario = "usuario"

    presentacion_chatbot = f"Hola mi nombre es {nombre_chatbot} se mucho sobre perifericos y me encataria resolver cualquier duda que tengas relacionada a este tema."
    advertencia_pregunta_larga = f'''Tu pregunta fue muy larga {nombre_usuario}, si queres podes volver a preguntarmela de una manera mas corta y directa.
Por ejemplo, si queres saber que es un periferico:

Decime: "¿Que es un perifercio?"
No me digas: "Hola ¿como estas? me gustaria saber que es un periferico"'''

    def enviar_mensaje_chatbot(nombre_chatbot, mensaje):
            area_mensajes.controls.append(
            ft.Text(f"{nombre_chatbot}: {mensaje}"
            )
        )
    
    def mostrar_respuesta(respuesta, nombre_chatbot, nombre_usuario, preguntas_almacenadas):
        # Si solo se devolvio una respuesta
        if len(respuesta["respuestas"]) == 1: 
            enviar_mensaje_chatbot(nombre_chatbot, respuesta["respuestas"][0])
            guardarLog("consola", respuesta["respuestas"][0], nombre_usuario, respuesta["porcentajes_similitud"][0]) # Se guarda la respuesta de la consola en el log.
        
        # Si se devolvio mas de una
        else:
            texto_disculpa = "Disculpame, no logre encontrar una respuesta precisa a tu pregunta."
            enviar_mensaje_chatbot(nombre_chatbot, texto_disculpa)

            # Se printea la advertencia de pregunta muy larga
            if respuesta["cantidad_palabras_usuario"] >= 8:
                enviar_mensaje_chatbot(nombre_chatbot, advertencia_pregunta_larga)
                
            # Se muestran el menu con las sugerencias y la opcion de enseñar
            mostrar_ingresar_menu_sugerencias(respuesta["preguntas_sugerencia"], respuesta["porcentajes_similitud"], respuesta["respuestas"], respuesta["enseniar_pregunta_usuario"], preguntas_almacenadas, nombre_chatbot, nombre_usuario)
    
    def mostrar_ingresar_menu_sugerencias(preguntas_sugeridas, porcentajes_similitudes, respuestas_sugeridas, pregunta_usuario, preguntas_almacenadas, nombre_chatbot, nombre_usuario):
        opciones_menu_sugerencia = f'''Pero aca te dejo 3 sugerencias que creo que te pueden servir:

1: ({str(porcentajes_similitudes[0])} % de similitud) {preguntas_sugeridas[0]}
2: ({str(porcentajes_similitudes[1])} % de similitud) {preguntas_sugeridas[1]}
3: ({str(porcentajes_similitudes[2])} % de similitud) {preguntas_sugeridas[2]}

Si ninguna de las sugerencias es adecuada a tu pregunta, tambien me podes enseñar la respuesta

4: Enseñar la respuesta
5: Hacer otra pregunta

Por favor, indicame el numero de la opcion que queres seleccionar'''

        enviar_mensaje_chatbot(nombre_chatbot, "Pero aca te dejo 3 sugerencias que creo que te pueden servir:")

        # Se crean los botones para cada sugerencia
        botones = []
        
        btn_sug1 = ft.ElevatedButton(
                text=f"({str(porcentajes_similitudes[0])} % de similitud) {preguntas_sugeridas[0]}",
                on_click=lambda e, resp=respuestas_sugeridas[0]: (
                    enviar_mensaje_chatbot(nombre_chatbot, resp),
                    guardarLog("consola", ("(Respuesta sugerida) " + respuestas_sugeridas[0]), nombre_usuario, porcentajes_similitudes[0]),

                    setattr(btn_sug1, "disabled", True),
                    setattr(btn_sug2, "disabled", True),
                    setattr(btn_sug3, "disabled", True),
                    setattr(boton_enseniar, "disabled", True),
                    page.update()
                )
            )
        btn_sug2 = ft.ElevatedButton(
                text=f"({str(porcentajes_similitudes[1])} % de similitud) {preguntas_sugeridas[1]}",
                on_click=lambda e, resp=respuestas_sugeridas[1]: (
                    enviar_mensaje_chatbot(nombre_chatbot, resp),
                    guardarLog("consola", ("(Respuesta sugerida) " + respuestas_sugeridas[1]), nombre_usuario, porcentajes_similitudes[1]),

                    setattr(btn_sug1, "disabled", True),
                    setattr(btn_sug2, "disabled", True),
                    setattr(btn_sug3, "disabled", True),
                    setattr(boton_enseniar, "disabled", True),
                    page.update()
                )
            )
        btn_sug3 = ft.ElevatedButton(
                text=f"({str(porcentajes_similitudes[2])} % de similitud) {preguntas_sugeridas[2]}",
                on_click=lambda e, resp=respuestas_sugeridas[2]: (
                    enviar_mensaje_chatbot(nombre_chatbot, resp),
                    guardarLog("consola", ("(Respuesta sugerida) " + respuestas_sugeridas[2]), nombre_usuario, porcentajes_similitudes[2]),

                    setattr(btn_sug1, "disabled", True),
                    setattr(btn_sug2, "disabled", True),
                    setattr(btn_sug3, "disabled", True),
                    setattr(boton_enseniar, "disabled", True),
                    page.update()
                )
            )

        botones.append(btn_sug1)
        botones.append(btn_sug2)
        botones.append(btn_sug3)

        # Se muestran los botones en area_mensajes
        area_mensajes.controls.append(
            ft.Column(botones, spacing=8)
        )

        enviar_mensaje_chatbot(nombre_chatbot, "Si ninguna de las sugerencias es adecuada a tu pregunta, tambien me podes enseñar la respuesta")

        boton_enseniar = ft.ElevatedButton(
                text="Enseñar la respuesta",
                on_click=lambda e: (
                    ingresar_enseniar(pregunta_usuario, preguntas_almacenadas),
                    # deshabilito explicitamente cada botón
                    setattr(btn_sug1, "disabled", True),
                    setattr(btn_sug2, "disabled", True),
                    setattr(btn_sug3, "disabled", True),
                    setattr(boton_enseniar, "disabled", True),
                    page.update()
                )
            )

        # Se muestra el boton enseñar en el area_mensajes
        area_mensajes.controls.append(boton_enseniar)

        enviar_mensaje_chatbot(nombre_chatbot, "Segui escribiendo si no queres seleccionar ninguna opcion")

    def ingresar_enseniar(pregunta_usuario, preguntas_almacenadas):
        # Esta funcion no la pudimos adaptar a flet, funciona desde la consola
        nueva_respuesta = input("Por favor, escribí la respuesta: ")
        
        # Guardar en el archivo CSV
        if agregar_pregunta_respuesta_aprendida(pregunta_usuario, nueva_respuesta): # Devuelve True si no hay fallas
            print("\nNueva pregunta-respuesta guardada correctamente.")
            print("¡Gracias! He aprendido algo nuevo.")
            # También actualizar la lista en memoria
            pregunta_normalizada_stemizada = stemizar(normalizar(pregunta_usuario))
            preguntas_almacenadas.append((pregunta_usuario, nueva_respuesta + "\n", pregunta_normalizada_stemizada, pregunta_normalizada_stemizada.split(), calcular_puntaje_lista_palabra(pregunta_normalizada_stemizada.split())))


    # Eventos de flet

    def enviar_mensaje_usuario(e):
        # Se guarda temporalmente el mensaje del usuario en memoria
        mensaje_usuario = input_pregunta.value
        mensaje_usuario_normalizado_stemizado = stemizar(normalizar(mensaje_usuario))

        # Se guarda el log
        guardarLog("user", mensaje_usuario, nombre_usuario)

        # Se escribe el mensaje del usuario en pantalla
        area_mensajes.controls.append(ft.Text(f"{nombre_usuario}: {mensaje_usuario}"))
        input_pregunta.value = ""

        page.update()

        # Enviar respuesta del chatbot
        respuesta = obtener_respuesta(mensaje_usuario_normalizado_stemizado, preguntas_almacenadas, mensaje_usuario)
        mostrar_respuesta(respuesta, nombre_chatbot, nombre_usuario, preguntas_almacenadas)

        page.update()

    area_mensajes = ft.Column()

    input_pregunta = ft.TextField(
        label="Escribe tu pregunta",
        expand=True
    )

    boton_enviar = ft.ElevatedButton(
        text="Enviar",
        on_click=enviar_mensaje_usuario
    )

    enviar_mensaje_chatbot(nombre_chatbot, presentacion_chatbot)
    enviar_mensaje_chatbot(nombre_chatbot, "¿en que puedo ayudarte hoy?")
    
    page.add(
        ft.Column(
            [
                area_mensajes,
                ft.Row(
                    [
                        input_pregunta,
                        boton_enviar
                    ]
                )
            ]
        )
    )