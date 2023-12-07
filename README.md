![Alt Img](images\juegos.gif)

# ¿QUÉ ES PIXEL SYNC?
Pixel Sync es una plataforma de búsqueda y filtrado de videojuegos que nace de la idea de acabar con esos largos períodos de búsqueda por culpa filtros superficiales que apenas nos dejan profundizar en nuestras búsquedas cuando tenemos clara un idea.

## ¿Qué la diferencia de otras plataformas similares?

Pixel Sync cuenta con la implementación de inteligencia artificial como motor de búsqueda, con la finalidad de recomendarte el juego que más encaje con tus gustos y descripciones, llevándote directo a los juegos que se alinean perfectamente con tus preferencias.

## Características destacadas:
🕹 **Búsqueda Inteligente**: Descubre nuevos juegos adaptados a tus gustos.

🎭 **Filtrado Avanzado**: Personaliza tus preferencias por título, plataforma y género.

🚀 **Asesoramiento IA**: Deja que la inteligencia artificial te guíe hacia experiencias de juego emocionantes.

<details>
<summary>ETL - Extracción, Transformación y Carga de Datos</summary>
<br>
Todos los archivos de datos se encuentran en la carpeta "data".

En la carpeta "notebooks" encontrarás cómo se realizó cada proceso:

### 🌐 Extracción de Datos de Metacritic:

En la fase de extracción, obtuve los datos de [Metacritic](https://www.metacritic.com/game/) a través de una llamada a la API externa de [Apify](https://apify.com/). La base de datos, posteriormente, fue exportada a un archivo .CSV ("metacritic.csv") para proceder a su tranformación y limpieza.

### 🧹 Transformación con Pandas:

Una vez recabados los datos, utilizamos la librería Pandas de Python para transformar y limpiar los mismos, empezando por una buena exploración del dato, así como la utilización de herramientas tales como limpieza de duplicados, agrupaciones y transformación de valores únicos, tratamiento de nulos...etc. Exportar el resultado nos dará como resultado  "metacritic_transform.csv".


### 🚚 Carga en la Base de Datos SQL:

Finalmente, dirigí mis datos hacia su nuevo hogar en una base de datos SQL. Gracias a la integración de Pandas con SQL, este proceso fue como construir un puente cósmico directo desde los datos transformados hasta la base de datos, asegurando un viaje suave y sin contratiempos.

### Extra: Traducción de los datos



</details>

