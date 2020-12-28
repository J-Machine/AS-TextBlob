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
        f = open('data/irrelevante.txt', "r")
        content_file = f.read()
        f.close()
        file_words = content_file.split(", ")
        # print("******", file_words)

        stopwords = set(STOPWORDS)          # Las palabras que serán eliminadas. Si es None, se utilizará la lista de STOPWORDS incorporada.
        stopwords.update(file_words)
        wc = WordCloud( width=360,          # create wordcloud object
                        height=150, 
                        background_color='indigo',
                        colormap='Pastel1', 
                        min_font_size=14,
                        max_words= self.max_words, 
                        stopwords=stopwords).generate(self.text)

        #__file__ es el nombre de la ruta del archivo desde el que se cargó el módulo
        currdir = path.dirname(__file__)
        wc.to_file(path.join(currdir, "media/output.png"))  # guardar imagen generadas
