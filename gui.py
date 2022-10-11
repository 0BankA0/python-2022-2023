import rekins
from rekins import Rekins
import PySimpleGUI as sg

sg.theme('DarkAmber')
  
layout = [
    [sg.Text('Ievadi datus')],
    [sg.Text('Vards', size =(27, 1)), sg.Input(key='klients')],
    [sg.Text('veltijums', size =(27, 1)), sg.Input(key='veltijums')],
    [sg.Text('izmēru (platums,garums,augstums)', size =(27, 1)), sg.Input(key='izmers')],
    [sg.Text('Ievadi materiāla cenu EUR/m2', size =(27, 1)), sg.Input(key='materials')],
    [sg.Button('Submit'), sg.Button('Exit')]
]  

window= sg.Window('Dati ievade', layout)

while True:
    event, values = window.read()
    if event == 'Exit':
        break
    elif event == 'Submit':
        data= Rekins(values['klients'], values['veltijums'], values['izmers'], values['materials'])
        sg.popup (data.izdrukat())


window.close()
