'''
--------------------------
Name: Giuliana Rivera
School: Ehrensvarska Gymnasiet 
Class: TE2A
e-mail: giulianabelen.riverarecinos.e@skola.karlskrona.se
Version: 
Revision:
Module name: History 
Latest update: 2025/01/19 18:43
--------------------------
'''
#Importing my modules
import navigation
import common

import os
import time 
#Creating a funktion to print the logo of the name, the intro. 
def game_history(first_time):

    GREEN = "\033[32m"
    RESET = "\033[0m"
    MAIN_LINE=f"{GREEN}-{RESET}"
    MY_PIPE=f"{GREEN}|{RESET}"
    MY_SPACE=" "

    #Calling my line functions 
    common.common_lines_hor()
    common.common_lines_vert()

    #Printing the games intro
    print(f"{GREEN}|{RESET}   SOME BACKGROUND INFORMATION, PLAY ATTENTION.                                                                       {GREEN}|{RESET}") 
    print(f"{GREEN}|{RESET}   For thousands of years, several generations of people have walked through the walls of Ehensverdska high.          {GREEN}|{RESET}")             
    print(f"{GREEN}|{RESET}   Millions of people have failed the missions provided to them and have gone out of there with no sucess.            {GREEN}|{RESET}")           
    print(f"{GREEN}|{RESET}   A hanfull of them have been close to fining the prestigious gold hat but not one of them have had                  {GREEN}|{RESET}")             
    print(f"{GREEN}|{RESET}   the abilities to complete it.  There have been big prospects that have walked through this halls,                  {GREEN}|{RESET}")              
    print(f"{GREEN}|{RESET}   great players that did everything in their power to complete the imposible until proven otherwise task.            {GREEN}|{RESET}")
    print(f"{GREEN}|{RESET}   This year we have a school full of students but you Shorty are the biggest prospect this school has seen in        {GREEN}|{RESET}")
    print(f"{GREEN}|{RESET}   the modern era. You got people counting on you. No pressure | (• ◡•) |                                             {GREEN}|{RESET}")
    print(f"{GREEN}|{RESET}                                                                                                                      {GREEN}|{RESET}")
    print(f"{GREEN}|{RESET}   My name is Kate and I will be following you and helping you along the way :)                                       {GREEN}|{RESET}")
    print(f"{GREEN}|{RESET}   To begin your adventure press enter.                                                                               {GREEN}|{RESET}")
  
  
    _choice=input( )
    os.system('cls')
    navigation.game_navigation(first_time)
        
    #Calling my line functions 
    common.common_lines_vert()
    common.common_lines_hor()





