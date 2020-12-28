""" 
                =====================================
                Modulo para crear la NUBE DE PALABRAS 
                =====================================
                Show which words are the most frequent 
                among the given text

"""

from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
from os import path


""" Clase para crear un wordcloud con mis propios requerimientos"""
class my_wordcloud:
    def __init__(self, text, max_wds):     
        self.text = text
        self.max_words = max_wds
        
    def generate_img(self):
        stopwords = set(STOPWORDS)          # Las palabras que serán eliminadas. Si es None, se utilizará la lista de STOPWORDS incorporada.
        wc = WordCloud( width=360,          # create wordcloud object
                        height=150, 
                        background_color='indigo',
                        colormap='Pastel1', 
                        min_font_size=14,
                        max_words= self.max_words, 
                        stopwords=stopwords).generate(self.text)


        wc.to_file(path.join(currdir, "media/output.png"))  # save wordcloud

### Test Wordcloud ### 

#__file__ es el nombre de la ruta del archivo desde el que se cargó el módulo, si se cargó desde un archivo
currdir = path.dirname(__file__)

a_text = ''' Combine Multiple Errors Into Single Crea una API de bitcoin con NodeJS and GraphQL\n EN DIRECTO EN MINECRAFT!!! 
        UN RATETE EN MINECRAFT!! PASEN Y VEAN!! Minecraft Java javascript mojang risas…  En mi carrera tuve asignaturas donde aprendí 
        y me peleé con la base de javascript html css y estoy muy agradecid…  Convert Decimal to Fraction  Cómo hacer un CRUD paso a 
        paso sin necesitar una base de datos en Angular  Código de JavaScript - Cuenta atras hasta una f '''

new_wordcloud = my_wordcloud(a_text, 8)
new_wordcloud.generate_img()
