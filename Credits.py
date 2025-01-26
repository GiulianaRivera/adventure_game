'''
--------------------------
Name: Giuliana Rivera
School: Ehrensvarska Gymnasiet
Class: TE2A
e-mail: giulianabelen.riverarecinos.e@skola.karlskrona.se
Version: menu
Revision:
Script namn:
Latest update: 2025/01/14 09:31
--------------------------
'''
import time 
import os 

import menu 


def game_credits ():
    #Color variables 
    GREEN = "\033[32m"
    RESET = "\033[0m"

    MAIN_LINE=f"{GREEN}-"
    MY_PIPE=f"{GREEN}|"
    MY_SPACE=" "
    for i in range(1,126):
        print( MAIN_LINE, end="" )
        if i == 125:
            print(MAIN_LINE)
    for i in range (1,11):
        print(MY_PIPE, end="")
        for j in range(1,126):
            print(MY_SPACE, end="" )
        print(MY_PIPE)
    
    #Printing the games intro
    print(f"{GREEN}|{RESET}   ░█████╗░██████╗░██╗░░░██╗███████╗███╗░░██╗████████╗██╗░░░██╗██████╗░███████╗  ██╗███╗░░██╗                                {GREEN}|{RESET}")             
    print(f"{GREEN}|{RESET}   ██╔══██╗██╔══██╗██║░░░██║██╔════╝████╗░██║╚══██╔══╝██║░░░██║██╔══██╗██╔════╝  ██║████╗░██║                                {GREEN}|{RESET}")           
    print(f"{GREEN}|{RESET}   ███████║██║░░██║╚██╗░██╔╝█████╗░░██╔██╗██║░░░██║░░░██║░░░██║██████╔╝█████╗░░  ██║██╔██╗██║                                {GREEN}|{RESET}")             
    print(f"{GREEN}|{RESET}   ██╔══██║██║░░██║░╚████╔╝░██╔══╝░░██║╚████║░░░██║░░░██║░░░██║██╔══██╗██╔══╝░░  ██║██║╚████║                                {GREEN}|{RESET}")              
    print(f"{GREEN}|{RESET}   ██║░░██║██████╔╝░░╚██╔╝░░███████╗██║░╚███║░░░██║░░░╚██████╔╝██║░░██║███████╗  ██║██║░╚███║                                {GREEN}|{RESET}")
    print(f"{GREEN}|{RESET}   ╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚══════╝  ╚═╝╚═╝░░╚══╝                                {GREEN}|{RESET}")
    
    print(f"{GREEN}|{RESET}   ███████╗██╗░░██╗██████╗░███████╗███╗░░██╗░██████╗██╗░░░██╗███████╗██████╗░██████╗░░██████╗██╗░░██╗░█████╗░                {GREEN}|{RESET}")
    print(f"{GREEN}|{RESET}   ██╔════╝██║░░██║██╔══██╗██╔════╝████╗░██║██╔════╝██║░░░██║██╔════╝██╔══██╗██╔══██╗██╔════╝██║░██╔╝██╔══██╗                {GREEN}|{RESET}")
    print(f"{GREEN}|{RESET}   █████╗░░███████║██████╔╝█████╗░░██╔██╗██║╚█████╗░╚██╗░██╔╝█████╗░░██████╔╝██║░░██║╚█████╗░█████═╝░███████║                {GREEN}|{RESET}")
    print(f"{GREEN}|{RESET}   ██╔══╝░░██╔══██║██╔══██╗██╔══╝░░██║╚████║░╚═══██╗░╚████╔╝░██╔══╝░░██╔══██╗██║░░██║░╚═══██╗██╔═██╗░██╔══██║                {GREEN}|{RESET}")
    print(f"{GREEN}|{RESET}   ███████╗██║░░██║██║░░██║███████╗██║░╚███║██████╔╝░░╚██╔╝░░███████╗██║░░██║██████╔╝██████╔╝██║░╚██╗██║░░██║                {GREEN}|{RESET}")
    print(f"{GREEN}|{RESET}   ╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝                {GREEN}|{RESET}")   
    

    print(f"{GREEN}|{RESET}    _____ _                              _   _         _     _                                                 _      _      {GREEN}|{RESET}")
    print(f"{GREEN}|{RESET}   | ____| |__  _ __ ___ _ __  _____   _(_)_(_)_ __ __| |___| | ____ _    __ _ _   _ _ __ ___  _ __   __ _ ___(_) ___| |_    {GREEN}|{RESET}")
    print(f"{GREEN}|{RESET}   |  _| | '_ \| '__/ _ \ '_ \/ __\ \ / // _` | '__/ _` / __| |/ / _` |  / _` | | | | '_ ` _ \| '_ \ / _` / __| |/ _ \ __|   {GREEN}|{RESET}")
    print(f"{GREEN}|{RESET}   | |___| | | | | |  __/ | | \__  \\ V /| (_| | | | (_| \__ \   < (_| | | (_| | |_| | | | | | | | | | (_| \__ \ |  __/ |     {GREEN}|{RESET}")
    print(f"{GREEN}|{RESET}   |_____|_| |_|_|  \___|_| |_|___/ \_/  \__,_|_|  \__,_|___/_|\_\__,_|  \__, |\__, |_| |_| |_|_| |_|\__,_|___/_|\___|\__|   {GREEN}|{RESET}")
    print(f"{GREEN}|{RESET}                                                                         |___/ |___/                                         {GREEN}|{RESET}")
    print(f"{GREEN}|{RESET}   giulianabelen.riverarecinos.e@skola.karlskrona.se                                                                         {GREEN}|{RESET}")
    
    for i in range (1,11):
        print(MY_PIPE, end="")
        for j in range(1,126):
            print(MY_SPACE, end="" )
        print(MY_PIPE)
    
    for i in range(1,126):
        print( MAIN_LINE, end="" )
        if i == 125:
            print(MAIN_LINE)
    time.sleep(5)
    os.system('cls')
    menu.game_menu()