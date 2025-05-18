# Equipo 2 - Copa de algoritmia 2025

# Cambios de la semana 2

Para esta segunda entrega realizamos los siguientes cambios y mejoras:

* Se creo un archivo `util.py` para escribir funciones genericas que nos faciliten el desarrolo. Un ejemplo de esto es la funcion `normalizar(texto)`.

## Optimizacion
* Ahora las preguntas se guardan en memoria directamente normalizadas. No era necesario tener la pregunta original.
* La pregunta del usuario se normaliza una unica vez

# Importante!

* El programa debe ejecutarse desde el archivo `chatbot.py`

* No es necesario tener el archivo `preguntas.csv` porque el mismo es generado automáticamente y de forma inteligente al ejecutar el programa.

## ¿Qué quiere decir que el archivo .csv se genera "de forma inteligente"?

Al correr el script principal del programa, el mismo verifica que el usuario cuente con el archivo `preguntas.csv` en su computadora. En el caso de no ser así, se genera automáticamente en el directorio donde esté ubicado el programa.

Otra posibilidad sería que el archivo exista pero su contenido no sea el correcto. Este caso también está contemplado, si ocurriera se sobreescribe el contenido incorrecto con el correcto (de acuerdo al código del programa).

# Estructura del programa

Para esta primera entrega utilizamos dos scripts en python y dos archivos .csv para almacenar datos. Los .csv se generan automáticamente en el caso de ser necesario.

## chatbot.py
Es el punto de inicio del programa, se encarga de la interacción con el usuario y el matcheo de preguntas con sus respuestas.

También hace uso de la matriz `preguntas_almacenadas` para almacenar en memoria las preguntas y respuestas originales + las nuevas respuestas enseñadas por el usuario. Esto es importante para no depender del archivo `preguntas.csv` durante la ejecución. Hacer una lectura a memoria es más rápido y eficiente que estar leyendo repetidas veces un archivo por cada vez que se realiza una consulta.

Por último, cuenta con la función `normalizar(texto)` para eliminar cualquier tipo de carácter que pueda dificultar el matcheo de preguntas entre lo que escriba el usuario y lo que tenga almacenado el programa.

## manejo_archivo_preguntas.py

Se encarga de leer y escribir los archivos `./preguntas.csv` y `./preguntasAprendidas.csv`. También cuenta con la matriz `datos` donde se encuentra la lista de preguntas con sus respuestas.

Se utiliza el hash sha256 para detectar si el contenido del archivo es incorrecto. El programa llama a la función `calcularSha256(ruta_archivo)` sobre el archivo .csv que tenga el usuario en su computadora y lo compara con el sha256 que consideramos correcto (se encuentra almacenado en la variable `sha256_correcto`).

La lectura y escritura se hace con sus respectivas funciones y para el caso de querer agregar una nueva pregunta-respuesta, se usa `agregarPreguntaRespuestaAprendida(pregunta, respuesta)`. A estas las consideramos "Preguntas aprendidas" y se almacenan en un archivo aparte para evitar conflictos con el hash sha256.

# Almacenamiento de datos

Se hizo uso de archivos .csv para almacenar las preguntas y las respuestas del chatbot. Utilizamos el siguiente formato:

```
Pregunta;Respuesta
¿Qué es un periférico?;Es un dispositivo que se conecta a una computadora para enviar o recibir datos.
```

Primero se colocan, a modo de referencia, los campos del contenido a almacenar. Cada columna se separa por un `;` y cada fila por un salto de línea `\n`.

## Uso de matrices

Como se mencionó anteriormente, utilizamos matrices para almacenar en memoria los datos a utilizar. Las matrices cuentan con la siguiente estructura:

```py
preguntas_almacendas = [
    ["¿Qué es un periférico?", "Es un dispositivo que se conecta a una computadora para enviar o recibir datos."]
]
```

> Aclaración: El chatbot depende del archivo `./preguntas.csv` para funcionar, pero no de `./preguntasAprendidas.csv`. Este último solo se crea para guardar las preguntas aprendidas entre sesiones y se manejan de la misma forma.
