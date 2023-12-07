# Funciones a exportar


def traducir_texto(texto, destino='en'):     # Función para traducir texto
    translator = Translator()
    traduccion = translator.translate(texto, dest=destino)
    return traduccion.text


def apply_genre_mapping(genre):
    return genre_mapping.get(genre)       # Función para mapear géneros


def categorize(column):                   # Función para categorizar columnas
    if pd.api.types.is_numeric_dtype(column):
        return pd.Categorical(column)
    return column