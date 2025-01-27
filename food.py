'''
--------------------------
Name: Giuliana Rivera
School: Ehrensvarska Gymnasiet
Class: TE2A
e-mail: giulianabelen.riverarecinos.e@skola.karlskrona.se
Version: menu
Revision:
Script namn: Game_over 
Latest update: 2025/01/27 23:31
--------------------------
'''
import time 

def game_chef(health, food_0, food_1):

    CHEF = f"         .--,--.\n         `.  ,.'\n          |___|\n          :o o:   O    \n         _`~^~'_  |    \n       /'   ^   `\\=)\n     .'  _______ '~|\n     `(<=|     |= /'\n         |     |\n         |_____|\n  ~~~~~~~ ===== ~~~~~~~~\n"

    GET_YOUR_FIKA = "Get your FIKA!!\n"
    NOTHING_TO_EAT = "Sorry young fella, running outa of dunkens, boii!!"
    FULL = "Sorry young fella, you just ate a Semla, come back when you need something grease!"
    WHAT = "What ya mean young fella?"
    WARE = "Gare Boi!!"

    BREAD = f"[ 1 ] FIKA BREAD\n\n( `^` ))\n|     ||\n|     ||\n'-----'`\n 20 HP\n"
    CAFE = f"[ 2 ] CAFE\n\n  ( (\n  ) )\n(----)-)\n \\__/-'\n`----'\n 20 HP\n"

    print(CHEF) 


    print(GET_YOUR_FIKA)

    if health != 100:

        if food_0 == True and food_1 == True:
            print(BREAD)
            print(CAFE)
        elif food_0 == True and food_1 == False:
            print(BREAD)
        elif food_0 == False and food_1 == True:
            print(CAFE)
        elif food_0 == False and food_1 == False:
            print(NOTHING_TO_EAT)
        
        while food_0 == True or food_1 == True:
            want_it = input("WHITCH ONE BOII? ")
            if want_it == '1':
                health += 20
                if health > 100:
                    heatlh = 100
                print(WARE)
                food_0  = False
                break
            elif want_it == '2':
                health += 20
                if health > 100:
                    health = 100
                print(WARE)
                food_1 = False
                break
            else:
                print(WHAT)
    else:
        print(FULL)
        
    
    return(health, food_0,food_1)
        