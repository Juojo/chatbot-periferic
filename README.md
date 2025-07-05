# Chatbot Periferic

Periferic es un chatbot que responde preguntas sobre perifericos. El proyecto se origino como parte de la comptencia *"Copa de algoritmia" 2025*. Esta desarrollado en python y cuenta con interfaz grafica en flet.

# Estructura del programa

El programa se encuentra dividio en tres partes: **Logica**, **interfaces** e **información almacenada**.

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

1. # Logica del programa:

## Escritura del arhivo con las preguntas almacenadas

El chatbot cuenta con una lista de preguntas y respuestas que son almacenadas en el archivo `preguntas.csv`. No es necesario contar con el archivo porque el mismo es generado automáticamente y de forma inteligente al ejecutar el programa.

### ¿Qué quiere decir que preguntas.csv se genera "de forma inteligente"?

Al correr el script principal del programa, el mismo verifica que el usuario cuente con el archivo `preguntas.csv` en su computadora. En el caso de no ser así, se genera automáticamente en el directorio donde esté ubicado el programa.

Otra posibilidad sería que el archivo exista pero su contenido no sea el correcto. Este caso también está contemplado, si ocurriera se sobreescribe el contenido incorrecto con el correcto (de acuerdo al código del programa).

### ¿Como se detecta que el contenido del archivo no es correcto?

Se utiliza el hash sha256 para detectar si el contenido del archivo es incorrecto. El programa llama a la función `calcularSha256(ruta_archivo)` sobre el archivo .csv que tenga el usuario en su computadora y lo compara con el sha256 que consideramos correcto.

## Almacenamiento en memoria de preguntas y respuestas

Trabajamos con informacion en memoria para no depender del archivo `preguntas.csv` durante la ejecución. Hacer una lectura a memoria es más rápido y eficiente que estar leyendo repetidas veces un archivo por cada vez que se realiza una consulta.

Utilizamos matrices para almacenar los datos a utilizar. Las matrices cuentan con la siguiente estructura y su tamaño es relativo a la cantidad de preguntas.

```py
preguntas_almacendas = [
    [
        "¿Qué es un periférico?", # (0) Pregunta
        "Es un dispositivo que se conecta a una computadora para enviar o recibir datos.", # (1) Respuesta
        "que es un perifer", # (2) Pregunta normalizada y stemizada
        ['que', 'es', 'un', 'perifer'], # (3) Lista de palabras clave
        8 # (4) Puntaje numerico total de la lista de palabras clave
    ],
    [
        # Siguiente pregunta-respuesta
    ]
]
```

Entonces, si se quiere saber cual es la respuesta de la tercer pregunta se hace: `preguntas_almacenadas[2][1]`. Y si se quisiera obtener la primer palabra de la lista de palabras claves: `preguntas_almacenadas[2][2][0]`.

## Normalizacion de texto

Antes de empezar con la busqueda de preguntas, el texto escrito por el usuario pasa por un proceso de normalizacion y stemming. Esto se hace con el objetivo de facilitar el matcheo de palabras, eliminando cualquier caracter que no sea necesario.

## Busqueda de preguntas identicas

Se realiza una busqueda entre la pregunta del usuario y las preguntas almacenadas con el objetivo de encontrar un String identico. Esto se hace por una cuestion de optimización, esta busqueda es mucho mas sencilla y rapida que la siguiente.

## Busqueda de preguntas por sistema de puntajes

En el caso de no encontrar una pregunta identica, se realiza una busqueda utilizando el sistema de puntajes. Este sistema permite encontrar preguntas que no hayan sido escritas literalmente como estan almacenadas.

### ¿Cómo funciona el sistema de puntajes?

Se divide la pregunta del usuario y las preguntas almacenadas en elementos de una lista.

Luego se comparan ambas listas en busca de palabras que coincidan. Si se encuentra una coincidencia:

* Se suma puntaje (la cantidad varía en si es una palabra de bajo o alto puntaje)
* Se elimina la palabra que fue encontrada para que no pueda seguir sumando puntos.

Una vez que se itero por todas las palabras de la pregunta del usuario, se calcula el porcentaje de similitud: Puntaje sumado / Puntaje máximo de la pregunta almacenada.

Esto se repite para todas las preguntas almacenadas y se guarda el indice de las tres preguntas con mayor coincidencia. Si la mejor esta por encima del 75%, se considera como una pregunta "identica" y se muestra la respuesta al usuario. Si ninguna supera este porcentaje, se considera como respuesta no encontrada.

> **Palabras de bajo puntaje:** que, es, un, etc.

> **Palabras de alto puntaje:** Son todas las que no sean de bajo puntaje. Por ejemplo: periférico, teclado, etc.

## ¿Que pasa si no se encuentra una respuesta?

Si no se encuentra respuesta, se muestra un mensaje explicandole al usuario que el chatbot no logro encontrar una respuesta precisa a su pregunta.

Luego de hacer esto, Se muestran tres sugerencias de preguntas que podrian llegar a coincidir pero que no pasaron el porcentaje de similitud establecido por el sistema de puntajes.

Ademas de mostrar las sugerencias se le da la opcion al usuario de hacer otra pregunta o enseñarle la respuesta a la pregunta realizada.

### Aprendizaje de preguntas

El usuario tiene la posibilidad de enseñarle preguntas y respuestas al chatbot. Como se menciono anteriormente, esta opcion solo se habilita en caso de no haber econtrado una respuesta.

La *pregunta-respuesta* que haya sido enseñada por el usuario se almacena en memoria y tambien dentro del arhivo `preguntasAprendidas.csv` (para poder conservarlas en proximas sesiones).

2. # Interfaces:

El programa se ejecuta utilizando la interfaz grafica desarrollada en Flet, tambien cuenta con la posibilidad de utilizar la interfaz de consola. Esta ultima es la recomendada para la implementacion de nuevas funciones, ya que es mas comoda y sencilla para el desarrollo.

3. # Almacenamiento de informacion:

Se hizo uso de archivos .csv para almacenar las preguntas y las respuestas del chatbot. Utilizamos el siguiente formato:

```
Pregunta;Respuesta
¿Qué es un periférico?;Es un dispositivo que se conecta a una computadora para enviar o recibir datos.
```

Primero se colocan, a modo de referencia, los campos del contenido a almacenar. Cada columna se separa por un `;` y cada fila por un salto de línea `\n`.