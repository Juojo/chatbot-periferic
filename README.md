# Equipo 2 - Copa de algoritmia 2025

# Cambios de la semana 2

Para esta segunda entrega realizamos los siguientes cambios y mejoras:

## Sistema de puntajes y palabras clave

Implementamos un sistema que permite encontrar preguntas que no hayan sido escritas literalmente como las tenemos almacenadas.

Esto quiere decir que si el usuario escribe "Que es periférico?" el chatbot es capaz de interpretarlo como "que es un periférico" y mostrar la respuesta a la pregunta.

### ¿Cómo funciona el sistema de puntajes?

Dividimos la pregunta del usuario y las preguntas almacenadas en elementos de una lista utilizando la función integrada de python `.split()`.

Luego comparamos ambas listas en busca de palabras que coincidan. Si se encuentra una coincidencia:

* Sumamos puntaje (la cantidad varía en si es una palabra de bajo o alto puntaje)
* Eliminamos la palabra que fue encontrada para que no pueda seguir sumando puntos.

Una vez que tenemos el puntaje de la pregunta sumado, calculamos el porcentaje de similitud: Puntaje sumado / Puntaje máximo de la pregunta almacenada.

Se guarda cuál fue la pregunta con el mayor porcentaje, y si está por encima del 75% se printea la respuesta.

* **Palabras de bajo puntaje:** que, es, un, etc.
* **Palabras de alto puntaje:** Son todas las que no sean de bajo puntaje. Por ejemplo: periférico, teclado, etc.

## Estructura del proyecto

* Se creó `util.py` para escribir funciones genéricas que nos faciliten el desarrollo. Un ejemplo de esto es la función `normalizar(texto)`.

* Se creó `puntaje.py` para hacer los cálculos de puntaje y almacenar la cantidad de puntos que representa cada palabra

## Optimización
* Ahora las preguntas se guardan en memoria directamente normalizadas. No era necesario tener la pregunta original.
 
* La pregunta del usuario se normaliza una única vez. Antes se llamaba a la función en cada iteración del for.

## Cambios varios

* Se reestructuró una gran parte de `chatbot.py`. Se agregaron funciones y se modificó el ciclo while principal del programa. Todo esto se hizo con el objetivo de mejorar la legibilidad del código.

* Se muestra un mensaje de advertencia si la pregunta del usuario es muy larga y no se le encontró una respuesta.

* Decidimos seguir utilizando `CSV` y no pasarnos a `JSON` porque este ultimo es mas pesado y realmente no necesitamos las ventajas que ofrece.

<br>

# Comienzo del README original (entregado en la semana 1)

<br>

# Importante!

* El programa debe ejecutarse desde el archivo `chatbot.py`

* No es necesario tener el archivo `preguntas.csv` porque el mismo es generado automáticamente y de forma inteligente al ejecutar el programa.

* El archivo `preguntas.csv` utiliza el encoding: `UTF-8`. Si se abre desde Excel, Bloc de notas, etc se deberá configurar de esta manera para su correcta visualización.

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
