""" 
        =====================================================
        PROGRAMA PARA ANALIZAR SENTIMIENTOS EN TEXTOS CORTOS 
        =====================================================
        Programa que analiza la polaridad y la subjetividad de 
        un texto, al mismo tiempo que devuelve una etiqueta 
        con las palabras mas recurrentes.
"""

import PySimpleGUI as sg
import os.path

# Modulos propios
from cloud_words import my_wordcloud
import text_analisis


##-----VARIABLES ----------------------------------##
txt_color = '#023e8a'
labels = ["Etiqueta1", "Etiqueta2", "Etiqueta3"]
list_themes = ['LightBrown9','BrightColors','LightBrown5','LightBlue5', 'Material1', 'SystemDefault' ]

##-----DEFAULT SETTINGS----------------------------------##
sg.theme(list_themes[-2])

##-----WINDOW AND LAYOUT---------------------------------##
input_column = [
    [sg.Text('¡BIENVENIDO(A)!', size=(65, 2), justification='center', font=('bold'))],
    [sg.Text('Nuestra herramienta de análisis de sentimientos te permitirá tener una medida de polaridad y subjetividad de tu texto.')],
    [sg.Text('A continuación coloca el texto que deseas analizar. Se permite un máximo de 300 caracteres.')],
    [sg.Text('El texto puede estar en español o en inglés.')],
    [sg.Multiline(size=(100, 15), key='-MLINE-')],  # identify the multiline via key option
    [sg.Button('Analizar', key='-SUBMIT-')],
]
result_column = [
    [sg.Text('Resultado:', font=('bold'), text_color=txt_color)],
    [sg.Text('- Polaridad', key='-POL-', size=(100, 1))],
    [sg.Text('- Subjetividad', key='-SUB-', size=(100, 1))],
    [sg.Text('Etiquetas:', font=('bold'),text_color=txt_color )],
    [sg.Text(labels[0], key='-TAG-', size=(100, 2))],
    [sg.Text('Nube de etiquetas: ', font=('bold'), text_color=txt_color)],
    [sg.Text(labels[1])],
    [sg.Image(key='-IMAGE-')],
]

layout = [
    [sg.Column(input_column)],
    [sg.Column(result_column)],
]

# Creación de la ventana
window = sg.Window('Analizador simple de sentimientos', layout ).Finalize()
print(sg.Window.get_screen_size())
print(layout)


##----HELPER FUNCTIONS-------------------------------##

 
def update_result(text):
    result = text_analisis.get_analysis(text)       #Función de otro módulo
    if result[0] == 0:
        window['-POL-'].update( "- Polaridad: Neutra. En el texto no existe carga emotiva." )
    if -1 <= result[0] < 0:
        window['-POL-'].update( "- Polaridad: Negativa. Los sentimientos en el texto tienen una connotación negativa." )
    if 0 < result[0] <= 1:
        window['-POL-'].update( "- Polaridad: Positiva. Los sentimientos en el texto tienen una connotación positiva." )
    
    if result[1] == 0:
        window['-SUB-'].update( "- Sujetividad: Objetivo. Es probable que se hable de hechos." )
    if 0 < result[1] < 0.5:
        window['-SUB-'].update( "- Subjetividad: Casi objetiva. Más cercano a tratarse de hechos que de opiniones o creencias" )
    if 0.5 <= result[1] <= 1:
        window['-SUB-'].update( "- Subjetividad: Subjetivo. Existe un grado de subjetividad varible en el texto." )


#-----MAIN EVENT LOOP------------------------------------##
# Como interfaz gráfica, debe ejecutarse dentro de un bucle y esperar que el usuario haga algo
# Este es un ciclo/bucle que procesa "eventos" y obtiene los valores del input
while True:
    event, values = window.read()
    print(event, values)

    if event == sg.WIN_CLOSED:
        break
    if event == '-SUBMIT-':
        
        input_text = values['-MLINE-']

        # Determinando la cantidad de palabras para las etiquetas
        # De acuerdo a la extención del mismo
        lenght_text = len(input_text)
        print(lenght_text)
        if 0 < lenght_text < 10:
            n_words = lenght_text
        elif 10 < lenght_text <= 100:
            n_words = 10
        elif 100 < lenght_text <= 200:
            n_words = 20
        elif 200 < lenght_text <= 300:
            n_words = 30

        #Show result
        update_result(input_text)
        print(values['-MLINE-'])  # get the content of multiline via its unique key
        
        #Etiquetas
        window['-TAG-'].update()

        # Generar WordCloud - (Módulo externo)
        cw = my_wordcloud(input_text, n_words)
        cw.generate_img()
        window['-IMAGE-'].update(filename="media/output.png")

window.close()





