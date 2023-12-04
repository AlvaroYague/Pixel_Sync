import streamlit as st
import pandas as pd
import openai
from PIL import Image
import pylab as plt
import webbrowser
import base64
import io
import re

with open('openai.txt', 'r') as archivo:
    token = archivo.read()

openai.api_key = token  

st.set_page_config(page_icon = '🎮', page_title = 'Pixel Sync')

def pagina_principal():
  
    st.title("¿Qué es Pixel Sync?")

    columna_derecha_1, columna_derecha_2 = st.columns(2)

    texto_derecha = """
    <p style="text-align: justify;">
        En el fascinante universo de Pixel Sync, tu viaje comienza explorando las vastas dimensiones del gaming. Nuestra herramienta revolucionaria te invita a sumergirte en un mundo donde cada click es una puerta a nuevas experiencias. Descubre juegos emocionantes, encuentra joyas ocultas y personaliza tu experiencia de juego de una manera única.
        Pixel Sync no solo se limita a recomendarte juegos basados en géneros convencionales, sino que se sumerge en la esencia de tus preferencias. Imagina un asistente virtual que entiende tus emociones y gustos como un amigo de confianza. ¿Buscas aventuras épicas? ¿O quizás preferirías un desafío estratégico? Con Pixel Sync, la inteligencia artificial ChatGPT abre un mundo de posibilidades para adaptarse a tus deseos y llevarte a nuevos horizontes de juego.
    </p>
    """
    columna_derecha_1.markdown(texto_derecha, unsafe_allow_html=True)
    columna_derecha_2.image("https://png2.cleanpng.com/sh/13a62083569ffe7d87cba41d9adceee5/L0KzQYm3U8MyN6duiZH0aYP2gLBuTfZqdpJxRdhqboTkg8q0lvlqNaNqhdN0ZT3necT6ifRqaV41SaQ2Znnxcb20hvFvfJJ4RdhybnHvPbfojwRie6oyTdNsMEC3RLKBWcRkPmQzS6YAMUi3QIW4VcIzPWQ4TKc5NUa1RHB3jvc=/kisspng-final-fantasy-vii-remake-dissidia-012-final-fantas-final-fantasy-5ac0044a894c63.3451840415225334505624.png", use_column_width=True)
    
    st.write("---")  

    columna_izquierda_1, columna_izquierda_2 = st.columns(2)

    texto_izquierda = """
    <p style="text-align: justify;">
        Nuestro extenso catálogo incluye desde clásicos atemporales hasta las últimas tendencias del mundo gaming. Pero Pixel Sync va más allá, permitiéndote personalizar tus recomendaciones como nunca antes. ¿Te apasionan los mundos de fantasía? ¿O prefieres competir en entornos futuristas? Define tu búsqueda y deja que Pixel Sync te lleve directo a la acción.
        Con Pixel Sync, tu búsqueda del juego perfecto es más que una búsqueda, es una aventura personalizada. Prepárate para descubrir, jugar y disfrutar al máximo con la herramienta que cambia la forma en que encuentras tus próximos juegos favoritos: ¡Pixel Sync, donde la sincronización y la diversión se encuentran en cada píxel!"
    </p>
    """
    columna_izquierda_1.image("https://png2.cleanpng.com/sh/48d8a45269f81de7c40111292e54e460/L0KzQYm3VMAyN6ttj5H0aYP2gLBuTf10NaFme592YX6wg8b3hgIue55mi9o2YoLyg37tjCIudppzjNd3ZHAwQ7X6TfFvbF51edV2YX6wRbLqUPM2OmdqUagBYUWxR4GCU8AzQWE2TaQ7NUi1SIO5WcU3NqFzf3==/kisspng-ms-pac-man-super-smash-bros-for-nintendo-3ds-and-pacman-5ac0c526e966a5.709302901522582822956.png", use_column_width=True)
    columna_izquierda_2.markdown(texto_izquierda, unsafe_allow_html=True)

def pagina_filtros():

    st.image("https://png2.cleanpng.com/sh/8f37e6e2ef1d3a03b10b795e60125e8a/L0KzQYm3UsA3N5ttiZH0aYP2gLBuTgRpbV5xfdlubnSwf7e0mvVtbJIyjNpuLX3sfrr6iL1kaaEyjNpuLXzod7b1hL1wbl5Bfd5tYT3vebByTgBvb15rgd5uLUXkR4qBVslnOGRpS6Y9Lke1Roa7VcM3OWY2T6s6M0e4SYG4VccveJ9s/kisspng-the-legend-of-zelda-the-minish-cap-the-legend-of-zelda-link-png-file-5a79869f03d344.7265453615179137590157.png", use_column_width=False, width=200)
    st.sidebar.header('Filtros')

    df = pd.read_csv('..\\Proyecto_Final\\data\\metacritic_es.csv')

    # Filtro por columna
    columna_filtro = st.sidebar.selectbox('Seleccionar columna para filtrar', ['Por defecto'] + df.columns.tolist())

    # Filtro por valor en la columna seleccionada
    if columna_filtro != 'Por defecto':
        valor_filtro = st.sidebar.text_input(f'Filtrar por {columna_filtro}', '')
    else:
        valor_filtro = None

    # Aplicar filtro al DataFrame original
    df_filtrado = df.copy()

    if valor_filtro is not None and columna_filtro != 'Por defecto':
        df_filtrado = df_filtrado[df_filtrado[columna_filtro].astype(str).str.contains(valor_filtro, case=False)]

    st.write(df_filtrado)

   # Filtrar por Título
    filtro_titulo = st.text_input('Filtrar por Título', '')
    df_filtrado = df_filtrado[df_filtrado['Title'].str.contains(filtro_titulo, case=False)]

# Filtrar por Plataforma con opción "Por defecto"
    plataforma_options = ['Por defecto'] + df_filtrado['Section'].unique().tolist()
    plataforma = st.selectbox('Filtrar por Plataforma', plataforma_options)
    if plataforma != 'Por defecto':
        df_filtrado = df_filtrado[df_filtrado['Section'] == plataforma]

    # Filtrar por Género con opción "Por defecto"
    genero_options = ['Por defecto'] + df_filtrado['Genres'].unique().tolist()
    genero = st.selectbox('Filtrar por Género', genero_options)
    if genero != 'Por defecto':
        df_filtrado = df_filtrado[df_filtrado['Genres'] == genero]

    # Filtrar por Metascore
    metascore_range = st.slider('Filtrar por Metascore', min_value=df_filtrado['Metascore'].min(), max_value=df_filtrado['Metascore'].max(), value=[df_filtrado['Metascore'].min(), df_filtrado['Metascore'].max()])
    df_filtrado = df_filtrado[df_filtrado['Metascore'].between(metascore_range[0], metascore_range[1])]

        # Botón para restablecer filtros
    if st.button('Restablecer Filtros'):
            df_filtrado = df.copy()

    # Mostrar DataFrame filtrado
    st.write('DataFrame Filtrado:', df_filtrado)

    user_input = st.text_area("Ingresa tu búsqueda:", " ")

# Botón para procesar la entrada del usuario
    if st.button("Generar respuesta"):
        # Llama a la API de OpenAI con el texto del usuario
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres un experto en videojuegos"},
            {"role": "user", "content": user_input}
        ],
        max_tokens=3000,
        temperature=0.5
    )


        # Muestra la respuesta de OpenAI
        st.write("Recomendación:")
        st.write(response['choices'][0]['message']['content'])

        # Utilizar expresiones regulares para encontrar el contenido entrecomillado
        coincidencias_entrecomilladas = re.findall(r'"([^"]*)"', response['choices'][0]['message']['content'] )

        # Autocompletar el filtro de Título con el primer contenido entrecomillado encontrado
        filtro_titulo = st.text_input('Filtrar por Título', value=coincidencias_entrecomilladas[0] if coincidencias_entrecomilladas else "")

        # Filtrar el DataFrame por Título
        df_filtrado = df[df['Title'].str.contains(filtro_titulo, case=False)]

        # Mostrar el DataFrame filtrado
        st.write('DataFrame Filtrado:', df_filtrado)

def pagina_acerca_de():
    st.title('Q&A')
    q_and_a = [
    {
        'Pregunta': "¿Cómo funciona la inteligencia artificial en la plataforma de filtrado de juegos?",
        'Respuesta': "La inteligencia artificial en nuestra plataforma de filtrado de juegos utiliza modelos avanzados de procesamiento de lenguaje natural, como GPT-3.5 Turbo de OpenAI. Estos modelos analizan las descripciones de los juegos y las consultas de los usuarios para proporcionar recomendaciones precisas y personalizadas.",
    },
    {
        'Pregunta': "¿Qué hace que nuestra plataforma sea única en comparación con otras herramientas de filtrado de juegos?",
        'Respuesta': "Lo que nos destaca es nuestra capacidad para comprender no solo los filtros convencionales, como plataforma y género, sino también las descripciones detalladas de los usuarios. Nuestra inteligencia artificial no se limita a palabras clave; puede captar matices y preferencias específicas, ofreciendo recomendaciones realmente personalizadas.",
    },
    {
        'Pregunta': "¿Puedo filtrar por características específicas que no son convencionales?",
        'Respuesta': "¡Absolutamente! Nuestra plataforma permite a los usuarios filtrar juegos por una amplia gama de características, desde la narrativa y los elementos de juego hasta detalles más específicos como la atmósfera del juego, el estilo artístico y la complejidad del argumental",
    },
    {
        'Pregunta': "¿Cómo puedo ajustar la precisión de las recomendaciones?",
        'Respuesta': "Ofrecemos la posibilidad de ajustar la temperatura en la generación de respuestas de la inteligencia artificial. Un valor de temperatura más bajo produce respuestas más centradas y precisas, mientras que un valor más alto permite respuestas más diversas. Esto brinda a los usuarios el control sobre la personalización de sus recomendaciones.",
    },
    {
        'Pregunta': "¿Cómo se actualiza la base de datos de juegos?",
        'Respuesta': "Actualizamos regularmente nuestra base de datos con los últimos lanzamientos y revisiones de juegos. Además, utilizamos retroalimentación de usuarios para mejorar continuamente nuestras recomendaciones y asegurarnos de que estén alineadas con las tendencias y preferencias actuales.",
    },
    {
        'Pregunta': "¿Qué información adicional puedo obtener sobre un juego específico?",
        'Respuesta': "Al seleccionar un juego, nuestra plataforma proporciona información detallada, incluyendo reseñas de usuarios, puntuaciones de críticos, detalles de la trama, y enlaces a recursos externos como trailers y reseñas especializadas.",
    },
    {
        'Pregunta': "¿Hay alguna función para descubrir juegos nuevos y emocionantes?",
        'Respuesta': "¡Sí! Ofrecemos funciones de descubrimiento que sugieren juegos basándose en tus preferencias actuales. Esto te permite explorar títulos que podrían estar fuera de tu radar pero que se ajustan perfectamente a tus gustos.",
    },
    {
        'Pregunta': "¿Cómo garantizan la privacidad de mis datos al utilizar la plataforma?",
        'Respuesta': "La privacidad y seguridad de los datos son fundamentales. No almacenamos información personal sin tu consentimiento explícito y nos adherimos a estrictas políticas de privacidad para proteger tus datos en todo momento."
    }
    ]

    for q_a_pair in q_and_a:
        pregunta = f"**{q_a_pair['Pregunta']}**"
        st.markdown(pregunta)
        st.write(q_a_pair['Respuesta'])
    # Contenido de la página "Acerca de"

# Sección para navegar entre páginas
pagina_seleccionada = st.sidebar.selectbox("Seleccionar Página", ["¿Qué es Pixel Sync?", "Búsqueda", "Q&A"])

# Mostrar la página correspondiente
if pagina_seleccionada == "¿Qué es Pixel Sync?":
    pagina_principal()
elif pagina_seleccionada == "Búsqueda":
    pagina_filtros()
elif pagina_seleccionada == "Q&A":
    pagina_acerca_de()