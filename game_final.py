'''
--------------------------
Name: Giuliana Rivera
School: Ehrensvarska Gymnasiet 
Class: TE2A
e-mail: giulianabelen.riverarecinos.e@skola.karlskrona.se
Version: menu
Revision:
Script namn:
Latest update: 
--------------------------
'''
#Importing phyton modules
import time
import os


#Importing my modules
import intro
import menu
import common

#+ + + + + + + + + + + + 
#- - MAIN GAME START  
#+ + + + + + + + + + + + 

#calling the intro 
intro.game_intro()
time.sleep(3) #The screen for the intro will show for 5 seconds and then the screen will switch to the menu

#clear the screen 
#common.clear( os.system.__name__)
os.system('cls')
#Calling the menu 
first_time = True
menu.game_menu(first_time)

