import streamlit as st
import pandas as pd
import openai
from PIL import Image
import pylab as plt
import webbrowser
import base64
import io
import re
import speech_recognition as sr
import pyttsx3
from funciones import *

with open('openai.txt', 'r') as archivo:
    token = archivo.read()

openai.api_key = token
st.set_page_config(page_icon = '🎮', page_title = 'Pixel Sync')


def pagina_principal():  # función primera página
    st.sidebar.image("https://png2.cleanpng.com/sh/159c3b5c0256084944e776162f71b772/L0KzQYm4UcI2N5p6R91yc4Pzfri0jfV1aZR3geZyYz3vf7j2TgBweqVmet5uLX7ohMj2kvsub6NmiNpyY4OwcsPojvQufKMyetN8ZT33cb3yTgJmeKZ5eeZyb36wgrb9ifV4NaVtitdqZD3wc36AUb1xaZhqRaU2NXLpcbW7WMdmOWlne6I3MEO2SYK6UMkyPWU4SagAMEa2SYO6WL5xdpg=/kisspng-metacritic-logo-portable-network-graphics-brand-tr-base-talk-reputation-review-thread-mc-71-page-3-5bfad487e18bc0.0339130915431650639238.png", width=300)
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

def pagina_filtros():  # función segunda página

    st.sidebar.header('Filtros')
    st.title('Busca tu juego ideal')

    if 'df_original' not in st.session_state:
        st.session_state.df_original = pd.read_csv('..\\Proyecto_Final\\data\\metacritic_es.csv')

    df_original = st.session_state.df_original

    # Filtrar por Título
    filtro_titulo = st.sidebar.text_input('Filtrar por Título', '')
    df_filtrado_original = df_original[df_original['Título'].str.contains(filtro_titulo, case=False)]

    # Filtrar por Plataforma
    plataforma_options = ['Por defecto'] + df_filtrado_original['Sección'].unique().tolist()
    plataforma = st.sidebar.selectbox('Filtrar por Plataforma', plataforma_options)
    if plataforma != 'Por defecto':
        df_filtrado_original = df_filtrado_original[df_filtrado_original['Sección'] == plataforma]

    # Filtrar por Género
    genero_options = ['Por defecto'] + df_filtrado_original['Género'].unique().tolist()
    genero = st.sidebar.selectbox('Filtrar por Género', genero_options)
    if genero != 'Por defecto':
        df_filtrado_original = df_filtrado_original[df_filtrado_original['Género'] == genero]

    # Filtrar por Metascore
    metascore_range = st.sidebar.slider('Filtrar por Metascore', min_value=df_filtrado_original['Metascore'].min(), max_value=df_filtrado_original['Metascore'].max(), value=[df_filtrado_original['Metascore'].min(), df_filtrado_original['Metascore'].max()])
    df_filtrado_original = df_filtrado_original[df_filtrado_original['Metascore'].between(metascore_range[0], metascore_range[1])]


    # Mostrar DataFrame original
    columnas_mostrar = ['Metascore', 'Userscore', 'Título', 'Género', 'Sección', 'Lanzamiento', 'Plataformas']
    df_filtrado_original = df_filtrado_original[columnas_mostrar]

    # Mostrar DataFrame original
    st.dataframe(df_filtrado_original, height=500)

    # Guardar el dataframe filtrado en el estado de la sesión

    if 'user_input_area' not in st.session_state:
        st.session_state['user_input_area'] = ""

    if 'respuesta_gpt3' not in st.session_state:
        st.session_state['respuesta_gpt3'] = None


    user_input_area = st.text_area("Ingresa tu consulta y pulsa Obtener recomendación:", st.session_state.get('user_input_area', ''))

    # Dividimos los botones para output de texto, input de voz, output de voz y silenciar

    col1, col2, col3, col4 = st.columns(4)
    if col1.button("Obtener recomendación 💭"): # obtener una recomendación y guardarla en un Session State
        respuesta = gpt3(user_input_area)
        st.session_state.respuesta_gpt3 = respuesta
        st.session_state.user_input_area = user_input_area

   
    if st.session_state.respuesta_gpt3:    # mostrar la respuesta si existe en el estado de la sesión
        st.write("Recomendación:")
        st.write(st.session_state.respuesta_gpt3)

        # Si se ha obtenido una nueva recomendación, procesarla para actualizar el dataframe filtrado
        coincidencias_entrecomilladas = re.findall(r'"([^"]*)"', st.session_state.respuesta_gpt3)
        if coincidencias_entrecomilladas:
            filtro_titulo = coincidencias_entrecomilladas[0]
            st.session_state.df_filtrado_chat = df_original[df_original['Título'].str.contains(filtro_titulo, case=False)]


    if col2.button("Búsqueda por voz 🗣"):  # ingresar texto mediante reconocimiento de voz
        texto_reconocido = reconocer_audio()
        if texto_reconocido is not None:
            st.session_state.user_input_area = texto_reconocido

    if col3.button("Escuchar respuesta 🔊"): # escuchar la respuesta mediante texto a voz
        if st.session_state.get('respuesta_gpt3'):
            reproducir(st.session_state.respuesta_gpt3)
        else:
            st.warning("No hay respuesta para convertir a voz. Obtén una recomendación primero.")
    
    if col4.button("Silenciar 🔇"):
        silenciar()

    # Mostrar el dataframe filtrado a partir de la respuesta del chat, si existe
    if 'df_filtrado_chat' in st.session_state and not st.session_state.df_filtrado_chat.empty:
        st.dataframe(st.session_state.df_filtrado_chat)

def pagina_acerca_de():  # función tercera página
    st.title('Q&A')
    st.write('Aquí encontrarás las preguntas más frecuentes sobre Pixel Sync. Si no encuentras la respuesta a tu pregunta, no dudes en contactarnos.')
    q_a = [
    {
        'Pregunta': "¿Cómo funciona la inteligencia artificial en la plataforma de filtrado de juegos?",
        'Respuesta': "La inteligencia artificial en nuestra plataforma de filtrado de juegos utiliza modelos avanzados de procesamiento de lenguaje natural, como GPT-3.5 Turbo de OpenAI. Estos modelos analizan las descripciones de los juegos y las consultas de los usuarios para proporcionar recomendaciones precisas y personalizadas.",
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
        'Pregunta': "¿Cómo garantizan la privacidad de mis datos al utilizar la plataforma?",
        'Respuesta': "La privacidad y seguridad de los datos son fundamentales. No almacenamos información personal sin tu consentimiento explícito y nos adherimos a estrictas políticas de privacidad para proteger tus datos en todo momento."
    }
    ]

    for q in q_a:
        pregunta = f"**{q['Pregunta']}**"
        st.markdown(pregunta)
        st.write(q['Respuesta'], justify='center')
    

# Sección para navegar entre páginas
pagina_seleccionada = st.sidebar.selectbox("Seleccionar Página", ["¿Qué es Pixel Sync?", "Búsqueda", "Q&A"])

# Mostrar la página correspondiente
if pagina_seleccionada == "¿Qué es Pixel Sync?":
    pagina_principal()
elif pagina_seleccionada == "Búsqueda":
    pagina_filtros()
elif pagina_seleccionada == "Q&A":
    pagina_acerca_de()