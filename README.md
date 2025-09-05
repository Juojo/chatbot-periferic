# Chatbot Periferic

Periferic es un chatbot que responde preguntas sobre periféricos. El proyecto se desarrolló para la competencia *"Copa de algoritmia" 2025*. Está programado en python y cuenta con interfaz gráfica en flet.

# Estructura del programa

El programa se encuentra dividió en tres partes: **Lógica**, **interfaces** e **información almacenada**.

```
chatbot-periferic/
├── main.py
├── logica/
│   ├── buscador_respuestas.py
│   ├── manejo_archivo_logs.py
│   ├── manejo_archivo_preguntas.py
│   ├── puntaje.py
│   └── util.py
├── interfaces/
│   ├── interfaz_consola.py
│   ├── interfaz_grafica.py
│   └── pantallas_interfaz_grafica/
│       ├── chat.py
│       └── inicio.py
├── informacion_almacenada/
│   ├── log.txt
│   ├── preguntas.csv
│   └── preguntasAprendidas.csv
```

# Lógica del programa

## Escritura del archivo CSV con las preguntas y respuestas

El chatbot cuenta con una lista de preguntas y respuestas que son almacenadas en un archivo `preguntas.csv`. No es necesario contar con el mismo porque este es generado automáticamente y de forma inteligente al ejecutar el programa.

#### ¿Qué quiere decir que preguntas.csv se genera "de forma inteligente"?

Al correr el script principal del programa, el mismo verifica que el usuario cuente con el archivo `preguntas.csv` en su computadora. En el caso de no ser así, se genera automáticamente en el directorio donde esté ubicado el programa.

Otra posibilidad sería que el archivo exista pero su contenido no sea el correcto. Este caso también está contemplado, si ocurriera se sobreescribe el contenido incorrecto con el correcto (de acuerdo al código del programa).

#### ¿Cómo se detecta que el contenido del archivo no es correcto?

Se utiliza el hash sha256 para detectar si el contenido del archivo es incorrecto. El programa llama a la función `calcularSha256(ruta_archivo)` sobre el archivo .csv que tenga el usuario en su computadora y lo compara con el sha256 que consideramos correcto.

## Almacenamiento en memoria de preguntas y respuestas

Trabajamos con información en memoria para no depender del archivo `preguntas.csv` durante la ejecución. Hacer una lectura a memoria es más rápido y eficiente que estar leyendo repetidas veces un archivo por cada vez que se realiza una consulta.

Utilizamos matrices para almacenar los datos a utilizar. Las matrices cuentan con la siguiente estructura y su tamaño es relativo a la cantidad de preguntas.

```py
preguntas_almacendas = [
   [
       "¿Qué es un periférico?", # (0) Pregunta
       "Es un dispositivo que se conecta a una computadora para enviar o recibir datos.", # (1) Respuesta
       "que es un perifer", # (2) Pregunta normalizada y stemizada
       ['que', 'es', 'un', 'perifer'], # (3) Lista de palabras clave
       8 # (4) Puntaje numérico total de la lista de palabras clave
   ],
   [
       # Siguiente pregunta-respuesta
   ]
]
```

Entonces, si se quiere saber cual es la respuesta de la tercer pregunta se hace: `preguntas_almacenadas[2][1]`. Y si se quisiera obtener la primer palabra de la lista de palabras claves: `preguntas_almacenadas[2][2][0]`.

## Normalización de texto

Antes de empezar con la búsqueda de preguntas, el texto escrito por el usuario pasa por un proceso de normalización y stemming. Esto se hace con el objetivo de facilitar el matcheo de palabras, eliminando cualquier carácter que no sea necesario.

## Búsqueda de preguntas idénticas

Se realiza una búsqueda entre la pregunta del usuario y las preguntas almacenadas con el objetivo de encontrar un String idéntico. Esto se hace por una cuestión de optimización, esta búsqueda es mucho más sencilla y rápida que la siguiente.

## Búsqueda de preguntas por sistema de puntajes

En el caso de no encontrar una pregunta idéntica, se realiza una búsqueda utilizando el sistema de puntajes. Este sistema permite encontrar preguntas que no hayan sido escritas literalmente como están almacenadas.

#### ¿Cómo funciona el sistema de puntajes?

Se divide la pregunta del usuario y las preguntas almacenadas en elementos de una lista.

Luego se comparan ambas listas en busca de palabras que coincidan. Si se encuentra una coincidencia:

* Se suma puntaje (la cantidad varía en si es una palabra de bajo o alto puntaje)
* Se elimina la palabra que fue encontrada para que no pueda seguir sumando puntos.

Una vez que se itero por todas las palabras de la pregunta del usuario, se calcula el porcentaje de similitud: Puntaje sumado / Puntaje máximo de la pregunta almacenada.

Esto se repite para todas las preguntas almacenadas y se guarda el índice de las tres preguntas con mayor coincidencia. Si la mejor está por encima del 75%, se considera como una pregunta "idéntica" y se muestra la respuesta al usuario. Si ninguna supera este porcentaje, se considera como respuesta no encontrada.

> **Palabras de bajo puntaje:** que, es, un, etc.

> **Palabras de alto puntaje:** Son todas las que no sean de bajo puntaje. Por ejemplo: periférico, teclado, etc.

## ¿Qué pasa si no se encuentra una respuesta?

Si no se encuentra respuesta, se muestra un mensaje explicando al usuario que el chatbot no logró encontrar una respuesta precisa a su pregunta.

Luego de hacer esto, se muestran tres sugerencias de preguntas que podrían llegar a coincidir pero que no pasaron el porcentaje de similitud establecido por el sistema de puntajes.

Además de mostrar las sugerencias se le da la opción al usuario de hacer otra pregunta o enseñarle la respuesta a la pregunta realizada.

#### Aprendizaje de preguntas

El usuario tiene la posibilidad de enseñarle preguntas y respuestas al chatbot. Como se mencionó anteriormente, esta opción solo se habilita en caso de no haber encontrado una respuesta.

La *pregunta-respuesta* que haya sido enseñada por el usuario se almacena en memoria y también dentro del archivo `preguntasAprendidas.csv` (para poder conservarlas en próximas sesiones).

# Interfaces

El programa se ejecuta utilizando la interfaz gráfica desarrollada en Flet, también cuenta con la posibilidad de utilizar la interfaz de consola. Esta última es la recomendada para la implementación de nuevas funciones, ya que es más cómoda y sencilla para el desarrollo.

# Almacenamiento de información

Se hizo uso de archivos .csv para almacenar las preguntas y las respuestas del chatbot. Utilizamos el siguiente formato:

```
Pregunta;Respuesta
¿Qué es un periférico?;Es un dispositivo que se conecta a una computadora para enviar o recibir datos.
```

Primero se colocan, a modo de referencia, los campos del contenido a almacenar. Cada columna se separa por un `;` y cada fila por un salto de línea `\n`.

> Aclaración: El chatbot depende del archivo ./preguntas.csv para funcionar, pero no de ./preguntasAprendidas.csv. Este último solo se crea para guardar las preguntas aprendidas entre sesiones y se manejan de la misma forma.