'''
--------------------------
Name: Giuliana Rivera
School: Ehrensvarska Gymnasiet 
Class: TE2A
e-mail: giulianabelen.riverarecinos.e@skola.karlskrona.se
Version: menu
Revision:
Module name: Intro
Latest update: 2025/01/19 18:43
--------------------------
'''

#Importing my modules
import common

#Creating a funktion to print the logo of the name, the intro. 
def game_intro():

    GREEN = "\033[32m"
    RESET = "\033[0m"
    MAIN_LINE=f"{GREEN}-{RESET}"
    MY_PIPE=f"{GREEN}|{RESET}"
    MY_SPACE=" "
    common.common_lines_hor()
    common.common_lines_vert()

    #Printing the games intro
    print(f"{GREEN}|{RESET}   ░█████╗░██████╗░██╗░░░██╗███████╗███╗░░██╗████████╗██╗░░░██╗██████╗░███████╗  ██╗███╗░░██╗                         {GREEN}|{RESET}")             
    print(f"{GREEN}|{RESET}   ██╔══██╗██╔══██╗██║░░░██║██╔════╝████╗░██║╚══██╔══╝██║░░░██║██╔══██╗██╔════╝  ██║████╗░██║                         {GREEN}|{RESET}")           
    print(f"{GREEN}|{RESET}   ███████║██║░░██║╚██╗░██╔╝█████╗░░██╔██╗██║░░░██║░░░██║░░░██║██████╔╝█████╗░░  ██║██╔██╗██║                         {GREEN}|{RESET}")             
    print(f"{GREEN}|{RESET}   ██╔══██║██║░░██║░╚████╔╝░██╔══╝░░██║╚████║░░░██║░░░██║░░░██║██╔══██╗██╔══╝░░  ██║██║╚████║                         {GREEN}|{RESET}")              
    print(f"{GREEN}|{RESET}   ██║░░██║██████╔╝░░╚██╔╝░░███████╗██║░╚███║░░░██║░░░╚██████╔╝██║░░██║███████╗  ██║██║░╚███║                         {GREEN}|{RESET}")
    print(f"{GREEN}|{RESET}   ╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚══════╝  ╚═╝╚═╝░░╚══╝                         {GREEN}|{RESET}")

    print(f"{GREEN}|{RESET}   ███████╗██╗░░██╗██████╗░███████╗███╗░░██╗░██████╗██╗░░░██╗███████╗██████╗░██████╗░░██████╗██╗░░██╗░█████╗░         {GREEN}|{RESET}")
    print(f"{GREEN}|{RESET}   ██╔════╝██║░░██║██╔══██╗██╔════╝████╗░██║██╔════╝██║░░░██║██╔════╝██╔══██╗██╔══██╗██╔════╝██║░██╔╝██╔══██╗         {GREEN}|{RESET}")
    print(f"{GREEN}|{RESET}   █████╗░░███████║██████╔╝█████╗░░██╔██╗██║╚█████╗░╚██╗░██╔╝█████╗░░██████╔╝██║░░██║╚█████╗░█████═╝░███████║         {GREEN}|{RESET}")
    print(f"{GREEN}|{RESET}   ██╔══╝░░██╔══██║██╔══██╗██╔══╝░░██║╚████║░╚═══██╗░╚████╔╝░██╔══╝░░██╔══██╗██║░░██║░╚═══██╗██╔═██╗░██╔══██║         {GREEN}|{RESET}")
    print(f"{GREEN}|{RESET}   ███████╗██║░░██║██║░░██║███████╗██║░╚███║██████╔╝░░╚██╔╝░░███████╗██║░░██║██████╔╝██████╔╝██║░╚██╗██║░░██║         {GREEN}|{RESET}")
    print(f"{GREEN}|{RESET}   ╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝         {GREEN}|{RESET}")   


    common.common_lines_vert()
    common.common_lines_hor()






