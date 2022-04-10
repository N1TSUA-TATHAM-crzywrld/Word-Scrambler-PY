import PySimpleGUI as sg
import random
from random_word import RandomWords

r = RandomWords()

def scramble(word): 
    arr = list(word)
    n = len(word)
    for i in range(n):
        j = random.randint(0, n-2)
        element=arr.pop(j)
        arr.append(element)
        output = (" ".join(arr))
        return output
        break
    
given_words1 = r.get_random_word(minCorpusCount=2000, hasDictionaryDef="true")
given_words2 = r.get_random_word(minCorpusCount=2000, hasDictionaryDef="true")
given_words3 = r.get_random_word(minCorpusCount=2000, hasDictionaryDef="true")

stored_words = list()

sg.theme('Dark Black')

def Make_Window3():
    layout = [ [sg.Text(size=(15,1),justification='c',text_color=("DeepPink2"),font=("Segoe Print",17,"bold"), background_color=("plum1"), key="-RAND_ONE-"),sg.VerticalSeparator("yellow"), sg.In(key="-ONE-")],
               [sg.Text(size=(15,1),justification='c',text_color=("DeepPink2"),font=("Segoe Print",17,"bold"), background_color=("plum1"), key="-RAND_TWO-"), sg.VerticalSeparator("yellow") ,sg.In(key="-TWO-")],
               [sg.Text(size=(15,1),justification='c',text_color=("DeepPink2"),font=("Segoe Print",17,"bold"), background_color=("plum1"), key="-RAND_THREE-"),sg.VerticalSeparator("yellow"), sg.In(key="-THREE-")],
               [sg.OK(key='-OK-')],
               [sg.Button("Get", key='-GET-')],
               [sg.Text(key='-ANSWER1-',text_color=("white"))],
               [sg.Text(key='-ANSWER2-',text_color=("white"))],
               [sg.Text(key='-ANSWER3-',text_color=("white"))]]
               
    return sg.Window('Third Window', layout, size=(600,300), finalize=True, element_justification='c')

pre_shuff_1 = (given_words1)
pre_shuff_2 = (given_words2)
pre_shuff_3 = (given_words3)

shuff_output_1 = scramble(pre_shuff_1)
shuff_output_2 = scramble(pre_shuff_2)
shuff_output_3 = scramble(pre_shuff_3)

window3 = Make_Window3()

while True:
    window, event, values = sg.read_all_windows(timeout=10)
    if window == window3:
        if event == '-GET-':
            window3["-RAND_THREE-"].update(shuff_output_3)
            window3["-RAND_TWO-"].update(shuff_output_2)
            window3["-RAND_ONE-"].update(shuff_output_1)
    if window == window3:
        if event == '-OK-':
            window3['-ANSWER1-'].update(pre_shuff_1)
            window3['-ANSWER2-'].update(pre_shuff_2)
            window3['-ANSWER3-'].update(pre_shuff_3)
        elif event == sg.WIN_CLOSED:
            window3.close()
            break

            
                #window3["-RAND_THREE-"].update(pre_shuff_1)






    


