""" Análisis de Textos con TextBlob """

from textblob import TextBlob
# import os  # para poder leer archivos del sistema
import time
""" 
    Leyendo archivo desde un archivo txt 
"""
file_text = open('data/song_murallaverde.txt', 'r')
content_file = file_text.read()
print(content_file + "\n")

# TextBlob
# text = str(content_file)
text_song = content_file
analysis = TextBlob(text_song)
print(analysis)

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
test_02 = standardize_lang("Como ramen todos los dias")
print(test_02, "\n")


def get_analysis(text):
    """ Estandariza y analiza el texto y devuelve la polaridad y subjetividad en una tupla """
    t = standardize_lang(text)
    polarity = TextBlob(t).sentiment.polarity
    subjetivity = TextBlob(t).sentiment.subjectivity
    return (polarity, subjetivity)

#### TEST- análisis del lenguaje ###
test_04 = get_analysis(text_song)
print("type of text song:", type(text_song), test_04, "\n")