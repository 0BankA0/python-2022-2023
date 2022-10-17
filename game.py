
import random

GUI_WINDOW_TITLE = "Akmens skeres papirits"
WELCOME_MESSAGE = "izvelies"
GUI_PROMPT_MESSAGE = ""

WIN_MESSAGE = "tu uzvareji"
LOSE_MESSAGE = "tu zaudeji"
TIE_MESSAGE = "neiskirts."

def random_choice(options=["Akmens", "Papirs", "škeres"]):
    return random.choice(options)

def determine_winner(choice1, choice2):

    winners = {
        "Akmens":{
            "Akmens": None,
            "Papirs": "Papirs",
            "škeres": "Akmens",
        },
        "Papirs":{
            "Akmens": "Papirs",
            "Papirs": None, 
            "škeres": "škeres",
        },
        "škeres":{
            "Akmens": "Akmens",
            "škeres": "Akmens",
            "škeres": None, 
        },
    }


    winner = winners[choice1][choice2]

    return winner

if __name__ == "__main__":

    

    options = ["Akmens", "Papirs", "škere"]

    Lietotaja_izvele = input("izvelies 'akmens', 'Papirs', or 'škeres': ")

    if Lietotaja_izvele in options:
        print("Tu izvelejies:", Lietotaja_izvele)
    else:
        print("tu neizvelejies ko vajadzeja")
        exit()

    Datora_izvele = random_choice(options)
    print("Dators izvelejas:", Datora_izvele)
    

    winning_choice = determine_winner(Lietotaja_izvele, Datora_izvele)

    if winning_choice:
        if winning_choice == Lietotaja_izvele:
            print(WIN_MESSAGE)
        elif winning_choice == Datora_izvele:
            print(LOSE_MESSAGE)
    else:
        print(TIE_MESSAGE)

    