'''
--------------------------
Name: Giuliana Rivera
School: Ehrensvarska Gymnasiet
Class: TE2A
e-mail: giulianabelen.riverarecinos.e@skola.karlskrona.se
Version: menu
Revision:
Script namn:door 
Latest update: 2025/01/14 09:31
--------------------------
'''
import common
import icons
import minigames
import time 
import navigation
def game_door_animation( my_room, color , key, health):

    common.common_lines_hor()
    common.ehrensverdska_adventure()
    common.common_lines_hor()

    _my_string = 'ENTERING TO ' + my_room
    print()
    common.background_color(color)
    print( _my_string )
    print()
    icons.game_emoji('DOOR')

    #Mini games

    if my_room == 'SELMA ROOM':
        if key == True:
            print("You are now in Selma Room")
            time.sleep(1)
            return(health)
        else:
            print("Welcome to Selma room to get the key to this room you will face off Kimmy in a game of 21. Good luck!")
            time.sleep(2)
            health_value = minigames.mini_21(health) #(0 o 20, health-0 o healt-20)(0,100)
            return(health_value)
    if my_room == 'AULA D':
        if key == True:
            print("You are now in Aula D")
            return(health)
        else:
            print("To enter this room you will face off against Samuel. Good luck!")
            time.sleep(2)
            health_value =minigames.mini_hangman(health)
            return(health_value)
    if my_room == 'D048':
        if key == True:
            print("You are now in D048")
            return(health)
        else:
            print("To get the key to this room you have to guess a random number that Kajsa is thinking about.")
            time.sleep(2)
            health_value =minigames.mini_guess_number(health)
            return(health_value)
    if my_room == 'D017':
        if key == True:
            print("Welcome to D017, its nice to have you here")
            return(health)
        else:
            print("To enter this room you have to beat Cajed in a game of rock papper scissors")
            time.sleep(2)
            health_value =minigames.mini_rock_papper_scissor(health)
            return(health_value)
    if my_room == 'CAFETERIA':
        return(health)