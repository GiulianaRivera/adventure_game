
'''
--------------------------
Name: Giuliana Rivera
School: Ehrensvarska Gymnasiet 
Class: TE2A
e-mail: giulianabelen.riverarecinos.e@skola.karlskrona.se
Version: 
Revision:
Module name: Menu
Latest update: 2025/01/14 09:31
--------------------------
'''

#Importing my modules
import navigation
import history
import common
import Credits
#improrting python modules
import os
import time 

def game_menu(first_time):
    #Variables for colors
    GREEN = "\033[32m"
    RESET = "\033[0m"
    RED = "\033[41m"

    
    MAIN_LINE="-"
    MAIN_LINE = "\033[32m-\033[0m"
    MY_PIPE = "|"
    MY_PIPE = "\033[32m|\033[0m"
    MY_SPACE = " "


    #Loop to print the horizontal line at the top of the rectangle
    for i in range(1,119):
        print( MAIN_LINE, end="" )
        if i == 118:
            print(MAIN_LINE)

    #Loop to print the vertical lines of the rectangle 
    for i in range (1,3):
        print(MY_PIPE, end="")
        for j in range(1,119):
            print(MY_SPACE, end="" )
        print(MY_PIPE)
    #Printing the games name for aestetic reasons
    common.ehrensverdska_adventure()

    #Loop to print the vertical lines of the rectangle
    for i in range (1,3):
        print(MY_PIPE, end="")
        for j in range(1,119):
            print(MY_SPACE, end="" )
        print(MY_PIPE)

    for i in range(1,119):
        print( MAIN_LINE, end="" )
        if i == 118:
            print(MAIN_LINE)

    for i in range (1,3):
        print(MY_PIPE, end="")
        for j in range(1,119):
            print(MY_SPACE, end="" )
        print(MY_PIPE)
    #Printing menu options 
    print(f"{GREEN}|{RESET}                [ 1 ] ⚀ NEW GAME                                                                                      {GREEN}|{RESET}")
    print(f"{GREEN}|{RESET}                                                                                                                      {GREEN}|{RESET}")
    print(f"{GREEN}|{RESET}                [ 2 ] ⚁ LOAD ONGOING GAME                                                                             {GREEN}|{RESET}")
    print(f"{GREEN}|{RESET}                                                                                                                      {GREEN}|{RESET}")
    print(f"{GREEN}|{RESET}                [ 3 ] ⚂ CREDITS                                                                                       {GREEN}|{RESET}")
    print(f"{GREEN}|{RESET}                                                                                                                      {GREEN}|{RESET}")
    print(f"{GREEN}|{RESET}                [ 4 ] ⚃ EXIT                                                                                          {GREEN}|{RESET}")

    for i in range (1,3):
        print(MY_PIPE, end="")
        for j in range(1,119):
            print(MY_SPACE, end="" )
        print(MY_PIPE)

    for i in range(1,119):
        print( MAIN_LINE, end="" )
        if i == 118:
            print(MAIN_LINE)




    for i in range (1,2):
        print(MY_PIPE, end="")
        for j in range(1,119):
            print(MY_SPACE, end="" )
        print(MY_PIPE)
    #Loop to select an option
    while True:
        #This is where user will insert the option they want
        choice_menu=input(f"{GREEN}|{RESET}                SELECT A CHOICE TO START THE ADVENTURE: " ) 
    
        if choice_menu == "1":
            print(f"{GREEN}|{RESET}                GOOD LUCK, YOU WILL NEED IT.                                                                          {GREEN}|{RESET}")
            #if user selects this option the loop will break
            rendering = 1
            time.sleep(1)
            #To clear the screen 
            os.system('cls')

            #After one second calling the history 

            history.game_history(first_time)
            os.system('cls')
            #Calling navigation module 
            #navigation.game_navigation(first_time) #Transporting fist_time in funtions

            break 
        elif choice_menu == "2":
            print(f"{GREEN}|{RESET}                WELCOME BACK, WE MISSED YOU. (NOT REALLY)                                                             {GREEN}|{RESET}")
            rendering = 2
            print()
            print(f"{GREEN}|{RESET}                {RED}This part is not available yet, it will be implemented in vesion 2.0 of the game.{RESET}                     {GREEN}|{RESET}")
            
        elif choice_menu == "3":
            print(f"{GREEN}|{RESET}                YOU ARE BEEING TAKEN TO THE MASTER ROOM, DONT STEAL ANYTHING.                                         {GREEN}|{RESET}")
            rendering = 3
            time.sleep(3)
            #After one second calling the game credits
            os.system('cls')
            Credits.game_credits()
            os.system('cls')
           
            break
            
        elif choice_menu == "4":
            print(f"{GREEN}|{RESET}                DONT GET TOO ATTACHED TO THE REAL WORLD, WE ARE COMING FOR YOU.                                       {GREEN}|{RESET}")
            time.sleep(2)
            common.exit_program()

        else:
            print(f"{GREEN}|{RESET}                THIS OPTION DOESNT EXIST, CHOOSE A REAL ONE U IDIOT.                                                  {GREEN}|{RESET}") 
            #If user inputs something else other than the four options the loop will continue until a real option is sleelcted 
        
        


