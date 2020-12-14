from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 

from os import path
#__file__ es el nombre de la ruta del archivo desde el que se cargó el módulo, si se cargó desde un archivo
currdir = path.dirname(__file__)

""" 
Creando una función que muestre una nube de palabras 
con las palbras que más nos interesan
"""
def create_wordcloud(text):     
    stopwords = set(STOPWORDS)
 
    # create wordcloud object
    wc = WordCloud( width=360, 
                    height=180, 
                    background_color='indigo',
                    colormap='Pastel1', 
                    min_font_size=10,
                    max_words=10, 
                    stopwords=stopwords).generate(text)
 
    # save wordcloud
    wc.to_file(path.join(currdir, "media/output.png"))

### Test Wordcloud ###
a_text = ''' Combine Multiple Errors Into Single Crea una API de bitcoin con NodeJS and GraphQL\n EN DIRECTO EN MINECRAFT!!! 
        UN RATETE EN MINECRAFT!! PASEN Y VEAN!! Minecraft Java javascript mojang risas…  En mi carrera tuve asignaturas donde aprendí 
        y me peleé con la base de javascript html css y estoy muy agradecid…  Convert Decimal to Fraction  Cómo hacer un CRUD paso a 
        paso sin necesitar una base de datos en Angular  Código de JavaScript - Cuenta atras hasta una f '''


create_wordcloud(a_text)
