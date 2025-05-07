# pregunta1 = "Como es tu nombre"
# respuesta1 = "Mi nombre es chatbot"
# 
# preguntaUsuario = input("Cual es tu pregunta?")
#

# if preguntaUsuario == pregunta[0]:
#     print(respuesta1)
# else:
#     print("Perdon, no se la respuesta a tu pregunta")
#     
# datos = [
#     ["Como es tu nombre", "Mi nombre es chatbot"],
#     ["2", "Mi nombre es chatbot"],
#     ["Como es tu nombre", "Mi nombre es chatbot"],
#     ["Como es tu nombre", "Mi nombre es chatbot"],
#     ["Como es tu nombre", "Mi nombre es chatbot"],
# ]

pregunta_usuario = input("Cual es tu pregunta?")

preguntas_almacenadas = [
    ["preGunta 1", "respuesta 1"],
    ["pregunta 2", "respuesta 2"]
]

for i in range (0, len(preguntas_almacenadas)):
    if pregunta_usuario.lower() == preguntas_almacenadas[i][0].lower(): # El primer valor de la lista numero i = 0 > es el primer lugar
        print(preguntas_almacenadas[i][1])