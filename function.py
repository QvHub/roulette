#function.py>
import random

def roulette():
    my_list = [
    ("green", 0),
    ("red", 32),
    ("black", 15),
    ("red", 19),
    ("black", 4),
    ("red", 21),
    ("black", 2),
    ("red", 25),
    ("black", 17),
    ("red", 34),
    ("black", 6),
    ("red", 27),
    ("black", 13),
    ("red", 36),
    ("black", 11),
    ("red", 30),
    ("black", 8),
    ("red", 23),
    ("black", 10),
    ("red", 5),
    ("black", 24),
    ("red", 16),
    ("black", 33),
    ("red", 1),
    ("black", 20),
    ("red", 14),
    ("black", 31),
    ("red", 9),
    ("black", 22),
    ("red", 18),
    ("black", 29),
    ("red", 7),
    ("black", 28),
    ("red", 12),
    ("black", 35),
    ("red", 3),
    ("black", 26),
    ]

    my_result= random.choice(my_list)
    return my_result

def question_end(player_wallet):

    player_wallet = player_wallet 

    if player_wallet < 1:
        validation_game = False
        print("G A M E - O V E R ")
    else:
        print("- - - - - - - - - - - - - -")
        input_question = input("Next one ? y/n")
        print("- - - - - - - - - - - - - -")

        while True:
            if input_question == "y" or input_question == "n":
                break
            else:
                print("No, no, no")
                input_question = input("Plz... y or n: ")

        if input_question  == "y":
            validation_game = True
        
        else:
            print('E N D - G A M E')
            validation_game = False   


    return validation_game

