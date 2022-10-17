
import PySimpleGUI as sg

from game import *
sg.theme('Dark')
layout = [
    [ sg.Text(GUI_PROMPT_MESSAGE) ],
    [ sg.Listbox(values=("Akmens", "Papirs", "škeres"), size=(30, 3), select_mode="single") ],
    [ sg.Submit() ]
]


window = sg.Window(GUI_WINDOW_TITLE).Layout(layout)

button, values = window.Read()

Lietotaja_izvele = values[0][0]
Datora_izvele = random_choice()
winning_choice = determine_winner(Lietotaja_izvele, Datora_izvele)

message = "-------------------"
message += f"\nTu izvelejies: {Lietotaja_izvele}"
message += f"\nDators izvelejas: {Datora_izvele}"
message += "\n-------------------"

if winning_choice:
    if winning_choice == Lietotaja_izvele:
        message += f"\n{WIN_MESSAGE}"
    elif winning_choice == Datora_izvele:
        message += f"\n{LOSE_MESSAGE}"
else:
    message += f"\n{TIE_MESSAGE}"


sg.Popup("Rezultats", message)
