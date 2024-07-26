import PySimpleGUI as sg
import random
from random_word import Wordnik

r = Wordnik()

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

given_words1 = r.get_random_word(maxLength=8, excludePartOfSpeech="noun", minCorpusCount=2000, hasDictionaryDef="true")
given_words2 = r.get_random_word(maxLength=8, excludePartOfSpeech="noun", minCorpusCount=2000, hasDictionaryDef="true")
given_words3 = r.get_random_word(maxLength=8, excludePartOfSpeech="noun", minCorpusCount=2000, hasDictionaryDef="true")

sg.theme('Dark Purple 1')

def Make_Window1():
    layout = [ [sg.Button('Word-Scrambler',button_color= ("plum1", "black"), font=("Gabriola",21,"bold"), size=(20,1))],
         [sg.Txt(' ' * 100, background_color=("thistle3"))],
         [sg.Button('Scramble a word',button_color= ("plum1", "black"), key='-SCRAMBLER-',font=("Segoe Print",15,"bold"), enable_events=True, size=(25,1))],
         [sg.Button('Un-Scramble',button_color= ("plum1", "black"), font=("Segoe Print",15,"bold"), key='-UNSCRAMBLE-',size=(25,1))]]
    
    return sg.Window('Word-Scrambler',layout, background_color=("thistle3") ,element_justification='c', size=(600,300),finalize=True)


def Make_Window2():
    layout1 = [ [sg.Txt('Enter the word you would like to scramble')],
           [sg.In(size=(50,5), key='-TXT_INPUT-')],
           [sg.Txt('_'  * 100)],
           [sg.Txt(size=(50,2), key='-OUTPUT-')  ],
           [sg.Button('Scramble', key='-FUNCTION-', bind_return_key=True,size=(35,2))],
           [sg.Txt(' ' * 100)],
           [sg.Button('EXIT', key='-EXIT-', size=(35,2))]]
    
    return sg.Window('Word Scrambler', layout1, font='Roboto', element_justification='c', size=(600,300), finalize=True)

def Make_Window3():
    layout = [ [sg.Text(size=(15,1),justification='c',text_color=("DeepPink2"),font=("Segoe Print",17,"bold"), background_color=("plum1"), key="-RAND_ONE-"),sg.VerticalSeparator("yellow"), sg.In(key="-ONE-")],
               [sg.Text(size=(15,1),justification='c',text_color=("DeepPink2"),font=("Segoe Print",17,"bold"), background_color=("plum1"), key="-RAND_TWO-"), sg.VerticalSeparator("yellow") ,sg.In(key="-TWO-")],
               [sg.Text(size=(15,1),justification='c',text_color=("DeepPink2"),font=("Segoe Print",17,"bold"), background_color=("plum1"), key="-RAND_THREE-"),sg.VerticalSeparator("yellow"), sg.In(key="-THREE-")],
               [sg.OK(key='-OK-')],
               [sg.Button("Get", key='-GET-')],
               [sg.Button("New Wordset", key='-NEW-')],
               [sg.Text(key='-ANSWER1-',text_color=("white"))],
               [sg.Text(key='-ANSWER2-',text_color=("white"))],
               [sg.Text(key='-ANSWER3-',text_color=("white"))]]
               
    return sg.Window('Third Window', layout, size=(630,330), finalize=True, element_justification='c')



window1, window2, window3 = Make_Window1(), None, None

given_words1 = r.get_random_word(maxLength=8, excludePartOfSpeech="noun", minCorpusCount=2000, hasDictionaryDef="true")
given_words2 = r.get_random_word(maxLength=8, excludePartOfSpeech="noun", minCorpusCount=2000, hasDictionaryDef="true")
given_words3 = r.get_random_word(maxLength=8, excludePartOfSpeech="noun", minCorpusCount=2000, hasDictionaryDef="true")

pre_shuff_1 = (given_words1)
pre_shuff_2 = (given_words2)
pre_shuff_3 = (given_words3)

shuff_output_1 = scramble(pre_shuff_1)
shuff_output_2 = scramble(pre_shuff_2)
shuff_output_3 = scramble(pre_shuff_3)

def Word_Refresh():
    global given_words1, given_words2, given_words3, pre_shuff_1, pre_shuff_2, pre_shuff_3, shuff_output_1, shuff_output_2, shuff_output_3


    given_words1 = r.get_random_word(maxLength=8, excludePartOfSpeech="noun", minCorpusCount=2000, hasDictionaryDef="true")
    given_words2 = r.get_random_word(maxLength=8, excludePartOfSpeech="noun", minCorpusCount=2000, hasDictionaryDef="true")
    given_words3 = r.get_random_word(maxLength=8, excludePartOfSpeech="noun", minCorpusCount=2000, hasDictionaryDef="true")
    
    pre_shuff_1 = (given_words1)
    pre_shuff_2 = (given_words2)
    pre_shuff_3 = (given_words3)
    
    NewWords = "invalid"
    
    while NewWords != "valid":
        try:
            shuff_output_1 = scramble(pre_shuff_1)
            shuff_output_2 = scramble(pre_shuff_2)
            shuff_output_3 = scramble(pre_shuff_3)
        except Exception:
            break
        else:
            NewWords = "valid"
            return shuff_output_1, shuff_output_2, shuff_output_3


while True:
    window, event, values = sg.read_all_windows(timeout=20)
    if window == window1:
        if event == sg.WIN_CLOSED or event == 'EXIT':
            window.close()
            break
        elif event == '-SCRAMBLER-':
            window1.close()
            window2 = Make_Window2()
    if window == window1:    
        if event == '-UNSCRAMBLE-':
            window1.close()
            window3 = Make_Window3()
    if window == window2:
        if event == '-FUNCTION-':
            try:
                txt = values['-TXT_INPUT-']
                arr = list(txt)
                n = len(arr)
                for i in range(n):
                    j = random.randint(0, n-2)
                    element=arr.pop(j)
                    arr.append(element)
                output = (" ".join(arr))
                window2['-OUTPUT-'].update(output)
            except:
                output1 = 'Invalid'
    if window == window2:
        if event == '-EXIT-':
            window2.close()
            break
    if window == window3:
        if event == '-OK-':
            window3["-RAND_THREE-"].update(shuff_output_3)
            window3["-RAND_TWO-"].update(shuff_output_2)
            window3["-RAND_ONE-"].update(shuff_output_1)
    if window == window3:
        if event == '-GET-':
            window3['-ANSWER1-'].update(pre_shuff_1)
            window3['-ANSWER2-'].update(pre_shuff_2)
            window3['-ANSWER3-'].update(pre_shuff_3)
    if window == window3:
        if event == '-NEW-':
            Word_Refresh()
            window3["-RAND_THREE-"].update(shuff_output_3)
            window3["-RAND_TWO-"].update(shuff_output_2)
            window3["-RAND_ONE-"].update(shuff_output_1)
            #event == '-OK-'
        elif event == sg.WIN_CLOSED:
            window3.close()
            break
        
        


            
            #window2['-OUTPUT-'].update(output)
    

