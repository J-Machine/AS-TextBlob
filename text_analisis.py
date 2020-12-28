""" 
                =====================================
                    Modulo para ANALISIS DE TEXTOS
                =====================================
                Uso de TextBlob y otras funciones 
                para limpiar y usar el texto
"""

from textblob import TextBlob
import os 
import time


""" 
    FUNCIONES 
"""
## #LIMPIEZA DEl TEXTO ##
def ignore_words():
    """ Crea una lista con las palabras a ignorar a partir de un archivo"""
    
    # Leyendo archivo
    f = open('data/irrelevante.txt', "r")
    content_file = f.read()
    f.close()
    file_words = content_file.split(", ")
    print("hay {0} palabras".format(len(file_words)), file_words)

    file_words.sort()

    # Creando el archivo con las palabras a ignorar
    g = open("data/excluir.txt", 'w')
    for w in file_words:
        g.write(w)
    g.close()

## LIMPIAR EL TEXTO ##
def clean_text_to_words(text):
    """ return a list of words with all punctuation removed,
        and all in lowercase.
    """
    my_substitutions = text.maketrans(
      # Remplazar el texto por minusculas y remover puntuación
      "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
      "abcdefghijklmnopqrstuvwxyz                                          ")

    # Traduciendo el texto
    cleaned_text = text.translate(my_substitutions)
    words = cleaned_text.split()
    return words

## ESTANDARIZAR EL LENGUAJE DE ANÁLISIS ##
def standardize_lang(text):
    """ Detecta el idioma inicial del texto(str) para devolver su traducción (str)al inglés de ser necesario .
    """
    t = TextBlob(text)
    if t.detect_language() == 'en':
        return str(t)
    
    # Si el idioma inicial no es el ingles, entonces devolver el texto traducido
    native = t.detect_language()
    t_translated = str(t.translate(from_lang = native, to = 'en'))  #cambia de un objeto textBlob a str
    return t_translated


## FUNCIÓN ANALISIS DE SENTIMIENTOS##
def get_analysis(text):
    """ Estandariza y analiza el texto y devuelve la polaridad y subjetividad en una tupla
        (polarity, subjetivity)
    """
    t = standardize_lang(text)
    polarity = TextBlob(t).sentiment.polarity
    subjetivity = TextBlob(t).sentiment.subjectivity
    return (polarity, subjetivity)
