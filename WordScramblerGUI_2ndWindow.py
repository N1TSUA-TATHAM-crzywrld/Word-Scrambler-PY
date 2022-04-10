import tkinter
from PIL import ImageFont
from tkinter.font import Font
import PySimpleGUI as sg
import random 

sg.theme('Dark Purple 1')

def Make_Window1():
    layout1 = [ [sg.Button('Word-Scrambler', font="Constantia", size=(50,3))],
         [sg.Txt(' ' * 100)],
         [sg.Button('You need a word scrambled', key='-SCRAMBLER-', size=(50,3))],
         [sg.Button('Un-Scramble', key='-UNSCRAMBLE-',size=(50,3))]]
    return sg.Window('Word-Scrambler', layout1, element_justification='c', size=(600,300),finalize=True)


def Make_Window2():
    layout = [ [sg.Txt('Enter the word you would like to scramble')],
           [sg.In(size=(50,5), key='-TXT_INPUT-')],
           [sg.Txt('_'  * 100)],
           [sg.Txt(size=(50,2), key='-OUTPUT-')  ],
           [sg.Button('Scramble', bind_return_key=True,size=(35,2))],
           [sg.Txt(' ' * 100)],
           [sg.CloseButton('EXIT',size=(35,2))]]
    return sg.Window('Word Scrambler', layout, font='Roboto', element_justification='c', size=(600,300), finalize=True)


def main():
    window2 = None
    window1 = Make_Window1()
    
    while True:
        window, event, values = sg.read_all_windows()
        if event == sg.WIN_CLOSED and window == window1:
            break

        elif event == '-SCRAMBLER-' and not window2:
            window1.Hide()
            window2 = Make_Window2()

        if window == window2 and event != sg.WIN_CLOSED:
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
                output1 = 'Invalid'
            
                window2['-OUTPUT-'].update(output)
        else:
            break
    
    #if window == window2 and event == 'EXIT':
     #   window2.Close()
      #  window2 = None
       # window1.un_hide()
  #  window1.Close()

if __name__ == '__main__':
    main()



#def window2_funct():
#    while True:
#        event2, values2 = Make_Window2()
#        if event2 != sg.WIN_CLOSED:
#           try:
 #           txt = values2['-TXT_INPUT-']
 #           arr = list(txt)
 #           n = len(arr)
 #           for i in range(n):
 #               j = random.randint(0, n-2)
 #               element=arr.pop(j)
 #               arr.append(element)
 #           output = (" ".join(arr))
 #          except:
 #           output = 'Invalid'
  #          window2['-OUTPUT-'].update(output)
  #      else:
  #          break
  #      return window2['-OUTPUT-'].update(output)
  #   

#while True:
 #   event1, values1 = window1.read()
  #  if event1 == sg.WIN_CLOSED:
   #     break
    #if event1 == '-SCRAMBLER-':
     #   try:
      #      window2_active = window2_funct()
       #     window1.Close()
        #except:
         #   window1.close()
            
        



#while True:
 #   event2, values2 = window2.read()
  #  if event2 != sg.WIN_CLOSED:
   #        try:
    #        txt = values2['-TXT_INPUT-']
     #       arr = list(txt)
      #      n = len(arr)
       #     for i in range(n):
        #        j = random.randint(0, n-2)
         #       element=arr.pop(j)
          #      arr.append(element)
           # output = (" ".join(arr))
         #  e#xcept:
            #o#utput = 'Invalid'
            
       #    window2['-OUTPUT-'].update(output)
    #else:
     #   break 
#window2.read()
