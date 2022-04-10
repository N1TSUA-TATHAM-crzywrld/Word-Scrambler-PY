
import PySimpleGUI as sg
import random

# Refer the the pysimpleGUI cookbook = **** 

sg.theme('Dark Purple 1')

# Choose the contents that will make up your Window
layout = [ [sg.Txt('Enter the word you would like to scramble')],
           [sg.In(size=(50,5), key='-TXT_INPUT-')],
           [sg.Txt('_'  * 100)],
           [sg.Txt(size=(50,1), key='-OUTPUT-')  ],
           [sg.Button('Scramble', bind_return_key=True,size=(40,2))],
           [sg.Txt(' ' * 100)],
           [sg.CloseButton('EXIT',size=(40,2))]]

# Remember to assign '-KEYS-' to be called later

# Assemble your window || window = sg.Window('chosen message',layout)

# ****Use different parameters for customization such as {font, size, ETC...}****

window = sg.Window('Word Scrambler', layout, font='Roboto', size=(600,300))
 
# Create the loop body for your window, notice how we call the TXT_INPUT key
# Compare this code(GUI) with the original code(No GUI) to learn how to take any function, and with a few changes, add a GUI

while True:
    event, values = window.read()

    if event != sg.WIN_CLOSED:
           try:
            txt = values['-TXT_INPUT-']
            arr = list(txt)
            n = len(arr)
            for i in range(n):
                j = random.randint(0, n-3)
                element=arr.pop(j)
                arr.append(element)
            output = (" ".join(arr))
           except:
            output = 'Invalid'
            
           window['-OUTPUT-'].update(output) 
    
    else:
        break