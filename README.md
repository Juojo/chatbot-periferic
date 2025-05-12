# Importante!

* El programa debe ejecutarse desde el archivo `chatbot.py`

* No se entrega el archivo .csv con las preguntas y respuestas porque el mismo es generado automaticamente y de forma inteligente al ejecutar el programa.

## ¿Que quiere decir que el archivo .csv se genera "de forma inteligente"?

Al correr el script prinicpal del programa, el mismo verifica que el usuario cuente con el archivo `preguntas.csv` en su computadora. En el caso de no ser así, se genera automaticamente en el directorio donde esté ubicado el programa.

Otra posibilidad seria que el archvio exista pero su contenido no sea el correcto. Este caso tambien esta contemplado, si ocurriera se sobreescribe el contenido incorrecto con el correcto (de acuedo al codigo del programa).

# Estructura del programa

Para esta primer entrega utilizamos dos scripts en python y dos archivos .csv para almacenar datos. Los .csv se generan automaticamente en el caso de ser necesario.

## chatbot.py
Es el punto de inicio del programa, se encarga de la interaccion con el usuario y el matcheo de preguntas con sus respuestas.

Tambien hace uso de la matriz `preguntas_almacenadas` para almacenar en memoria las preguntas y respuestas. Esto es importante para no depender del archivo `preguntas.csv` durante la ejecucion. Hacer una lectura a memoria es más rapido y eficiente que estar leyendo repetidas veces un archivo por cada vez que se realice una consulta.

Por ultimo, cuenta con la función `normalizar(texto)` para eliminar cualquier tipo de caracter que pueda dificultar el matcheo de preguntas entre lo que escriba el usuario y lo que tenga almacenado el programa.

## manejo_archivo_preguntas.py

Se encarga de leer y escribir los archivos `./preguntas.csv` y `./preguntasAprendidas.csv`. Tambien cuenta con la matriz `datos` donde se encuentra la lista de preguntas con sus respuestas.

