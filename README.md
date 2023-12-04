# Tarea 3: DCCine 🎬

## Consideraciones generales 🐙

1. La tarea tiene énfasis en el paradigma de programación funcional, permitiendo el uso de funciones de orden superior como filter, map y reduce, pero también de bucles dentro de estructuras declaradas mediante comprehension notation, por lo que he elegido adoptar el segundo enfoque permitido, no creo que haya ningún problema porque según leí detenidamente, está permitido explícitamente usar estructuras por comprensión tipo listas para obtener los elementos de un generador y guardarlas en variables, para su posterior manipulación, nada del enunciado dice que no puedo hacer eso. Además de no haber necesitado casi el uso de filter, map y reduce, el enfoque que he adoptado me parece prácticamente igual en términos de legibilidad para esta tarea en específico.

2. He mantenido el import de utilidades al inicio de consultas.py: from utilidades import Funciones, porque me pareció relevante ya que es necesario, aunque no se haya subido el fichero de utilidades al repositorio, porque el enunciado pide excluirlo. No la he comentado porque sin esa línea, no se podría importar Funciones del módulo utilidades, y es necesario para que el código funcione correctamente. Por favor, tener en consideración.

3. Según vi en un issue, es recomendable citar la persona con la que se ha realizado la actividad 5, en mi caso la hice con @flcarvallo.

### Cosas implementadas y no implementadas:
Todos los requisitos de la tarea están suplidos.

#### Programación funcional

Explicar nuevamente lo que hace cada parte del código me parece innecesariamente reiterativo, porque he puesto comentarios en casi todo el código explicando cómo funciona. Espero que sea suficiente, porque según mi criterio, está bastante claro el funcionamiento del código, y hay comentarios en casi todo, para que no haya ambigüedades o confusiones.

### Utiliza 1 generador: 
✅ Completado
### Utiliza 2 generadores: 
✅ Completado
### Utiliza 3 o más generadores: 
✅ Completado

#### API

He realizado todos los métodos solicitados, y como esta parte de la tarea es tan genérica y repetitiva, no siento que sea necesario explicar lo que hace cada cosa, ya que sería explicar lo obvio. Además, el código es muy similar al de la actividad 5. He puesto, igual que en los apartados anteriores, comentarios para clarificar la lectura del código.

### Obtener información: 
✅ Completado
### Modificar información:
✅ Completado

## Ejecución 💻

No hay un módulo principal, sino dos con diferentes funcionalidades:

1. `consultas.py` en `T3`: contiene las funciones de la parte de programación funcional de la tarea.

2. `peli.py` en `T3`: se encarga de la API de la tarea.

## Librerías 📚

Las librerías propias son los dos únicos archivos de la tarea, que corresponden a los archivos `peli.py` y `consultas.py`, para el apartado de programación funcional y API, respectivamente.

### Librerías externas utilizadas

En el fichero `consultas.py` he utilizado:

1. Del módulo `collections`, he usado `Counter`.
2. Del módulo `utilidades`, he usado `Funciones`.
3. Del módulo `typing`, he usado `Generator`.
4. Del módulo `math`, el método `ceil()`.
5. Del módulo `datetime`.
6. Del módulo `datetime`, el método `strptime()`.

En el fichero `peli.py` de la API, he usado:

1. El módulo `json` ya contenido en Python del módulo `json`.
2. El módulo `request` para peticiones http, que debe instalarse. De este último, he utilizado casi todos los verbos http de solicitudes: PATCH, GET, POST, DELETE.

## Supuestos y consideraciones adicionales 🤔

Los supuestos que realicé durante la tarea son los siguientes:

1. En la función `genero_comun`, el enunciado dice que debo considerar los casos para 1, 2 o todos los géneros que más se repiten, por lo que he supuesto que el input sólo entrega casos que se acoplan a lo mencionado.
2. En `peliculas_en_base_al_rating`, he retornado instancias de películas, y no el título como pide el enunciado, ya que eso no permite pasar los tests. Lo he explicado en un comentario en el código. Según lo que vi, es válido lo que hice según un issue.
3. En `personas_reservas`, he asumido que el generador permite generar instancias de objetos que siempre son reservas, y siempre tienen su propiedad `.id_persona` que permite identificar el id único de la persona que realiza la reserva. Por lo tanto, retorno todos esos ids. Espero haber entendido bien este punto. Si lo hago como he mencionado, pasan todos los test.

## Referencias de código externo 📖

No he utilizado código externo.

