'''
--------------------------
Name: Giuliana Rivera
School: Ehrensvarska Gymnasiet
Class: TE2A
e-mail: giulianabelen.riverarecinos.e@skola.karlskrona.se
Version: menu
Revision:
Script namn: Game_over 
Latest update: 2025/01/27 23:06
--------------------------
'''
import time 
import os

import common

#import menu 


def game_over ():
    #Color variables 
    GREEN = "\033[32m"
    RED = "\033[31m"

    RESET = "\033[0m"

    MAIN_LINE=f"{GREEN}-{RESET}"
    MY_PIPE=f"{GREEN}|{RESET}"
    MY_SPACE=" "
    for i in range(1,115):
        print( MAIN_LINE, end="" )
        if i == 114:
            print(MAIN_LINE)
            
    for i in range (1,11):
        print(MY_PIPE, end="")
        for j in range(1,115):
            print(MY_SPACE, end="" )
        print(MY_PIPE)
        
    
    #Printing the games intro
    print(f"{GREEN}|{RESET}  {RED}  ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗                                      {RESET}{GREEN}|{RESET}")             
    print(f"{GREEN}|{RESET}  {RED} ██╔════╝ ██╔══██╗████╗ ████║██╔════╝   ██╔═══██╗██║   ██║██╔════╝██╔══██╗                                      {RESET}{GREEN}|{RESET}")           
    print(f"{GREEN}|{RESET}{RED}   ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝                                     {RESET}{GREEN}|{RESET}")             
    print(f"{GREEN}|{RESET}  {RED} ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗                                     {RESET}{GREEN}|{RESET}")              
    print(f"{GREEN}|{RESET}  {RED} ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║                                     {RESET}{GREEN}|{RESET}")
    print(f"{GREEN}|{RESET}  {RED} ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝      ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝                                     {RESET}{GREEN}|{RESET}")
    
                                    
    
    for i in range (1,11):
        print(MY_PIPE, end="")
        for j in range(1,115):
            print(MY_SPACE, end="" )
        print(MY_PIPE)
    
    for i in range(1,115):
        print( MAIN_LINE, end="" )
        if i == 114:
            print(MAIN_LINE)
    time.sleep(5)
    os.system('cls')
    common.exit_program()
   

