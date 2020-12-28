""" Análisis de Textos con TextBlob """

from textblob import TextBlob
from os import path
import time
""" leyendo texto de irrelevantes """
#__file__ es el nombre de la ruta del archivo desde el que se cargó el módulo
currdir = path.dirname(__file__)

f = open('data/irrelevante.txt', "r")
content_file = f.read()
f.close()
file_words = content_file.split(", ")
print("hay {0} palabras".format(len(file_words)), file_words)

file_words.sort()
g = open("data/excluir.txt", 'w')
for w in file_words:
    g.write(w)
g.close()

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
c = """ No me gusta la pasta
 """
testing_tb = TextBlob(c)
# Extrayendo polaridad y subjetividad
analisis = testing_tb.sentiment
polarity = testing_tb.sentiment.polarity
subjetivity = testing_tb.sentiment.subjectivity
print('ANALISIS es ', analisis, 'Polarity es ', polarity, 'Subjetividad es ', subjetivity)

# Extrayenfo tags
tb_tags = testing_tb.tags
print("TAGS :", tb_tags, "\n")

# Extrayendo Noun phrases / frases nominales
tb_phrases = testing_tb.noun_phrases
# print("FRASES NOMINALES :", tb_phrases, "\n")

# Extrayendo oraciones. Reconoce oraciones por el punto. No es necesario que esté en inglés
tb_sentences = testing_tb.sentences
# print("ORACIONES :", tb_sentences, "\n")

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
    """ Estandariza y analiza el texto y devuelve la polaridad y subjetividad en una tupla
        (polarity, subjetivity)
    """
    t = standardize_lang(text)
    polarity = TextBlob(t).sentiment.polarity
    subjetivity = TextBlob(t).sentiment.subjectivity
    return (polarity, subjetivity)

#### TEST- análisis del lenguaje ###
test_04 = get_analysis(testing_text)
print("type of text song:", type(testing_text), "\n", test_04, "\n")
print(test_04[0])