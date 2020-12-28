""" 
Creando una interfaz gráfica que reciba la información del usuario 
"""
import PySimpleGUI as sg
import os.path
from cloud_words import my_wordcloud
#Temas
list_themes = ['LightBrown9','BrightColors','LightBrown5','LightBlue5', 'Material1', 'SystemDefault' ]
sg.theme(list_themes[-2])

#Variables
labels = ["Etiqueta1", "Etiqueta2", "Etiqueta3"]

#Contenido por columnas
input_column = [
    [sg.Text('¡BIENVENIDO(A)!')],
    [sg.Text('Nuestra herramienta de análisis de sentimientos le permitirá tener una medida de polaridad y subjetividad de su texto.    ')],
    [sg.Text('A continuación coloque el texto que desea analizar. Se permite un máximo de 140 caracteres.')],
    [sg.Text('El texto puede estar en español o en inglés.')],
    [sg.Multiline(size=(100, 20), key='-MLINE-')],  # identify the multiline via key option
    [sg.Button('Analizar', key='-SUBMIT-')],
]
result_column = [
    # [sg.Text('Etiquetas:' + labels[0], key='-TAG-')],
    [sg.Text('Etiquetas:' )],
    [sg.Text(labels[0], key='-TAG-', size=(100, 2))],
    [sg.Text('Nube de etiquetas: ' + labels[1])],
    [sg.Image(key='-IMAGE-')],
    [sg.Text('Gráfico:' + labels[2])],
]

""" Clase para construir la interfaz """
#Dibujo del Layout por filas
layout = [
    [sg.Column(input_column)],
    [sg.Column(result_column)],
]

# Crea la ventana
window = sg.Window('Analizador simple de sentimientos', layout ).Finalize()
print(sg.Window.get_screen_size())
print(layout)



### Probando clase function
test_text = '''As a footnote, you should use lowercase for method names, and Capital words for classes as you're doing now. It's a good convention. I greatly recommend it.
You should simply construct the object once in display.py and call all the methods.'''






# Como interfaz gráfica, debe ejecutarse dentro de un bucle y esperar que el usuario haga algo
# Este es un ciclo/bucle que procesa "eventos" y obtiene los valores del imput
while True:
    event, values = window.read()
    print(event, values)

    if event == sg.WIN_CLOSED:
        break
    if event == '-SUBMIT-':
        cw_test = my_wordcloud(test_text, 3)
        cw_test.generate_img()
        window['-IMAGE-'].update(filename="media/output.png")

    print('You entered in the textbox:')
    print(values['-MLINE-'])  # get the content of multiline via its unique key
    window['-TAG-'].update(values['-MLINE-'])

window.close()










""" sg.Popup('Title',
         'The results of the window.',
         'The button clicked was "{}"'.format(event),
         'The values are', values) """

"""
    Demonstrates the new change_submits parameter for inputtext elements
    It ONLY submits when a button changes the field, not normal user input
    Be careful on persistent forms to not clear the input
"""
""" layout = [[sg.Text('Test of reading input field')],
          [sg.Text('This input is normal'), sg.Input()],
          [sg.Text('This input change submits'),
           sg.Input(change_submits=True)],
          [sg.Text('This multiline input change submits'),
           sg.ML('', change_submits=True)],
          [sg.Text('This input is normal'),
           sg.Input(), sg.FileBrowse()],
          [sg.Text('File Browse submits'),
           sg.Input(change_submits=True,
                key='-in1-'), sg.FileBrowse()],
          [sg.Text('Color Chooser submits'),
           sg.Input(change_submits=True,
                key='-in2-'), sg.ColorChooserButton('Color...', target=(sg.ThisRow, -1))],
          [sg.Text('Folder Browse submits'),
           sg.Input(change_submits=True,
                key='-in3-'), sg.FolderBrowse()],
          [sg.Text('Calendar Chooser submits'),
           sg.Input(change_submits=True,
                key='-in4-'), sg.CalendarButton('Date...', target=(sg.ThisRow, -1))],
          [sg.Text('Disabled input submits'),
           sg.Input(change_submits=True,
                disabled=True,
                key='_in5'), sg.FileBrowse()],
          [sg.Text('This input clears after submit'),
           sg.Input(change_submits=True, key='-in6-'), sg.FileBrowse()],
          [sg.Button('Read')]]

window = sg.Window('Demonstration of InputText with change_submits',
           layout, auto_size_text=False, default_element_size=(22, 1),
                   text_justification='right')

while True:     # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break

window.close() """