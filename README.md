![Alt Img](https://github.com/AlvaroYague/Pixel_Sync/blob/main/images/juegos.gif)

<div style="text-align: justify;">

# ¿QUÉ ES PIXEL SYNC?
**Pixel Sync es una plataforma de búsqueda y filtrado de videojuegos** que nace de la idea de acabar con esos largos períodos de búsqueda por culpa filtros superficiales que apenas nos dejan profundizar en nuestras búsquedas cuando tenemos clara un idea. Bebiendo directamente desde la base de datos de [Metacritic](https://www.metacritic.com/game/), Pixel Sync ofrece un amplio catálogo de videojuegos que abarcan todas las generaciones de consolas, desde los 90's hasta la actualidad, para garantizar que encuentres tu juego ideal.

## ¿Qué nos diferencia de otras plataformas?

Pixel Sync cuenta con la implementación de **inteligencia artificial** como motor de búsqueda, con la finalidad de recomendarte el juego que más encaje con tus gustos y descripciones, llevándote directo a los juegos que se alinean perfectamente con tus preferencias.

La **inteligencia artificial** de Pixel Sync analiza no solo las características básicas de un juego, como su título, plataforma y género, sino que también profundizan en tus preferencias individuales. Este enfoque permite a Pixel Sync entender tus gustos y descripciones de una manera más holística, llevándote directamente a los juegos que realmente se alinean con tus preferencias únicas.

## Características destacadas:
- 🕹 **Búsqueda Inteligente**: Descubre nuevos juegos adaptados a tus gustos.

- 🎭 **Filtrado Avanzado**: Personaliza tus preferencias por título, plataforma y género.

- 🚀 **Asesoramiento IA**: Deja que la inteligencia artificial te guíe hacia experiencias de juego emocionantes.

## ¿Cómo funciona la plataforma?

El motor de búsqueda es muy sencillo. En la página **"Búsqueda"** podrás encontrar la base de datos con una serie de filtros tales como **"Título"**, **"Plataforma"**, **"Género"** o **"Metascore"**, por si quieres explorar los datos con filtros un poco más superficiales.

Por otro lado, en el cuadro de texto podrás escribir una descripción tan detallada como requieras, y pulsando el botón **"Obtener recomendación"**, la IA te devolverá el juego que más se adecúe a tu descripción, generando un breve resumen del mismo y todos los datos de dicho juego en nuestra base de datos.

A continuación, adjunto un vídeo para que tengas una referencia más visual:

https://github.com/AlvaroYague/Pixel_Sync/assets/145923518/bf43e676-1fc1-4923-86cc-edb0e0d76ebd 
  
------------------------------------------------------------- 

### Por último, queda adjunto todo el proceso que se ha seguido para obtener la base de datos de Pixel Sync :

<details style="padding: 10px; border: 1px solid #ddd; border-radius: 5px;">
  <summary style="font-size: 18px; font-weight: bold;">ETL - Extracción, Transformación y Carga de Datos</summary>
<br>

**Todos los archivos de datos se encuentran en la carpeta *"data"***

**En la carpeta *"notebooks"* encontrarás cómo se realizó cada proceso:**

### 🌐 Extracción de Datos de Metacritic:

En la fase de extracción, obtuve los datos de [Metacritic](https://www.metacritic.com/game/) a través de una llamada a la **API externa** de [Apify](https://apify.com/). La base de datos, posteriormente, fue exportada a un archivo .CSV ("metacritic.csv") para proceder a su tranformación y limpieza.

### 🧹 Transformación con Pandas:

Una vez recabados los datos, utilizamos la librería **Pandas** de Python para transformar y limpiar los mismos, empezando por una buena *exploración del dato, así como la utilización de herramientas tales como limpieza de duplicados, agrupaciones y transformación de valores únicos, tratamiento de nulos*...etc. Exportar el resultado nos dará como resultado  "metacritic_transform.csv".


### 🚚 Carga en la Base de Datos SQL:

Finalmente, con los datos ya transformados, estos son importados a una **base de datos en SQL** creada y exportada desde Python, con la finalidad de tener un acceso sencillo a los mismo a la hora de modificarlos y actualizarlos.

### Extra: Traducción de los datos

Como extra, se ha realizado una pequeña *transformación de datos y aplicación de la librería GoogleTrans para traducir toda la base de datos al español*, ya que en primera instancia esta se encuentra en inglés. Como resultado, obtenermos el archivo "metacritic_es.csv".

</details>

</div>

