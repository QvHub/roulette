from function import *

player_wallet = 100

validation_game = True
result = 0
print("")
print("///////////////////////////")
print("             *             ")
print("C A E S A R S - P A L A C E")
print("             *             ")
print("      R O U L E T T E"      )
print("             *             ")
print("///////////////////////////")
print("")

#                  #
#                  #
# F E A T U R  - 1 #
#                  #
#                  #

#loop for play multiple round 
while validation_game == True :
    #*** C O L O R ***
    #-----Initialisation of choose Color, Bet and Wallet after Bet-----
    player_bet_color = input("Choose betwin red or black or no \n")

    # You can jump color bet 
    if player_bet_color != "no":
        # Choose color
        while True:
            if player_bet_color == "red" or player_bet_color == "black":
                break
            else:
                print("No, no, no")
                player_bet_color = input("Plz bet red or black or no !")

        # Bet money
        while True:
            try:
                player_bet_money_color = int(input("Bet money color :"))
                player_bet_money_color == int
                break
            except:
                player_bet_money_color = input("Just a number Plz: ")       
          
        # Verify if Bet is no more player wallet
        if player_bet_money_color >  player_wallet:
            print("No bro")
            player_bet_money_color = int(input("Bet color :"))

        player_wallet -= player_bet_money_color
        print(f"Your wallet is now: {player_wallet}")  

    #*** N U M B E R ***
    #-----Initialisation of choose Number, Bet and Wallet after Bet-----

    # Verification if the wallet isn't = 0 
    if player_wallet < 1:
        print("You can't bet on number betwin 1 and 36")
        player_bet_number = "Nan"
    else: 
        player_bet_number = input("Choose a number betwin 1 and 36 or no \n")
        # You can jump color bet
        if player_bet_number != "no":
            player_bet_number = int(player_bet_number)

            # Choose Number
            while True:
                if player_bet_number < 37:
                    break
                else:
                    print("No, no, no")
                    player_bet_number = int(input("Choose a number betwin 1 and 36: "))

            # Bet money
            while True:
                try:
                    player_bet_money_number = int(input("Bet money number :"))
                    player_bet_money_number == int
                    break
                except:
                    player_bet_money_number = input("Just a number Plz: ")


            # Verify if Bet is no more player wallet
            if player_bet_money_number >  player_wallet:
                print("No bro")
                player_bet_money_number = int(input("Bet money number :"))

            player_wallet -= player_bet_money_number
            print(f"Your wallet is now: {player_wallet}")

    #*** E V E N  ***
    #-----Initialisation of choose Even or Odd, Bet and Wallet after Bet-----
    # Verification if the wallet isn't = 0 
    if player_wallet < 1:
        print("You can't bet even or odd number")
        player_bet_even = "NaN"
    else:    
        player_bet_even = input("Choose an even or odd number or no \n")
        # You can jump color bet 
        if player_bet_even != "no":


            # Choose Even or Odd Number
            while True:
                if player_bet_even == "even" or player_bet_even == "odd":
                    break
                else:
                    print("No, no, no")
                    player_bet_even = input("Plz bet even or odd !")  

            # Bet money
            
            player_bet_money_even = int(input("Bet money number :"))
            while True:
                try:
                    player_bet_money_even == int
                    break
                except:
                    player_bet_money_even = input("Just a number Plz: ") 

            # Verify if Bet is no more player wallet
            if player_bet_money_even >  player_wallet:
                print("No bro")
                player_bet_money_even = int(input("Bet money even :"))
                while True:
                    try:
                        player_bet_money_even == int()
                        break
                    except:
                        player_bet_money_even = input("Just a number Plz: ")               

            player_wallet -= player_bet_money_even
            print(f"Your wallet is now: {player_wallet}") 

    # Roulette round 
    result_roulette = roulette()    
  
    # Roulette result 
    print("------------------")
    print("R E S U L T")
    print(result_roulette[0])
    print(result_roulette[1])
    print("------------------")    

    if result_roulette[0] == player_bet_color:
        print("Color win")
        player_wallet += player_bet_money_color*2
        print("+", player_bet_money_color*2)
    else:
        print("Color loose")
        

    if int(result_roulette[1]) == player_bet_number:
        print("Number Win")
        player_wallet += player_bet_money_number*2
        print("+", player_bet_money_number*2)
    else:
        print("Number loose")

    if int(result_roulette[1])%2 == 0:
        if player_bet_even == "even": 
            print("Even Win")
            player_wallet += player_bet_money_even*2
            print("+", player_bet_money_even*2)
        else:
            print("Even loose")
    else:
        if player_bet_even == "odd":
            print("Odd Win")
            player_wallet += player_bet_money_even*2
            print("+", player_bet_money_even*2)
        else:
            print("Odd loose")           

    print(f"The last wallet: {player_wallet}")
    
    validation_game = question_end(player_wallet)

