""" Análisis de Textos con TextBlob """

from textblob import TextBlob
# import os  # para poder leer archivos del sistema
import time

""" 
    Leyendo archivo desde un archivo txt 
"""
# canción
file_song = open('data/song_murallaverde.txt', 'r') # Spanish
content_song = file_song.read()

#comentario en twitter
file_twt = open('data/twitter_comment_en.txt', 'r') # English
content_twt = file_twt.read()

# definiendo con que texto trabajar
testing_text = content_twt # Alias 

""" 
    Probando TEXTBLOB
"""
# Creando un objeto textBlob (instanciando)
testing_tb = TextBlob(content_song)

# Extrayenfo tags
tb_tags = testing_tb.tags
print("TAGS :", tb_tags, "\n")

# Extrayendo Noun phrases / frases nominales
tb_phrases = testing_tb.noun_phrases
print("FRASES NOMINALES :", tb_phrases, "\n")

# Extrayendo oraciones. Reconoce oraciones por el punto. No es necesario que esté en inglés
tb_sentences = testing_tb.sentences
print("ORACIONES :", tb_sentences, "\n")

""" 
    Creando la función principal que analisará el texto 
"""

def standardize_lang(a_text):
    """ Detecta el idioma inicial del texto(str) para devolver su traducción (str)al inglés de ser necesario .
    """
    t = TextBlob(a_text)
    if t.detect_language() == 'en':
        return str(t)
    
    # Si el idioma inicial no es el ingles, entonces devolver el texto traducido
    native = t.detect_language()
    t_translated = str(t.translate(from_lang = native, to = 'en'))  #c ambia de un objeto textBlob a str
    return t_translated

    # El texto esta en inglés y no fue necesario traducirlo
    

#### TEST- estandarizacion del lenguaje ###
test_02 = standardize_lang(testing_text)
print(test_02, "\n")


def get_analysis(text):
    """ Estandariza y analiza el texto y devuelve la polaridad y subjetividad en una tupla """
    t = standardize_lang(text)
    polarity = TextBlob(t).sentiment.polarity
    subjetivity = TextBlob(t).sentiment.subjectivity
    return (polarity, subjetivity)

#### TEST- análisis del lenguaje ###
test_04 = get_analysis(testing_text)
print("type of text song:", type(testing_text), "\n", test_04, "\n")