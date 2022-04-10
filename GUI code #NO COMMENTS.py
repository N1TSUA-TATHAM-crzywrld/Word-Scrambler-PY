import PySimpleGUI as sg
import random 

sg.theme('Dark Purple 1')

layout = [ [sg.Txt('Enter the word you would like to scramble')],
           [sg.In(size=(50,5), key='-TXT_INPUT-')],
           [sg.Txt('_'  * 100)],
           [sg.Txt(size=(50,2), font='Verdana', key='-OUTPUT-')  ],
           [sg.Button('Scramble', bind_return_key=True,size=(35,2))],
           [sg.Txt(' ' * 100)],
           [sg.CloseButton('EXIT',size=(35,2))]]

window = sg.Window('Word Scrambler', layout, font='Verdana', element_justification='c', size=(600,300))
 
while True:
    event, values = window.read()

    if event != sg.WIN_CLOSED:
           try:
            txt = values['-TXT_INPUT-']
            arr = list(txt)
            n = len(arr)
            for i in range(n):
                j = random.randint(0, n-2)
                element=arr.pop(j)
                arr.append(element)
            output = (" ".join(arr))
           except:
            output = 'Invalid'
            
           window['-OUTPUT-'].update(output)
    else:
        break