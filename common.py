'''
--------------------------
Namn: Giuliana Rivera
skola: Ehrensvarska Gymnasiet 
Klass: TE2A
e-mail: giulibelenrivera@gmail.com
Version:
Revision:
Module name: Common
Senaste updateringen:
--------------------------
'''
#In this module I will be defining funktions that will be common throughout the project 
#phyton libraries
import os 
import sys


#Defining funktion to clear the screen 
def clear( my_name ):
    # for windows
    if my_name == 'system':
        _ = os.system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')


def myexit():
    sys.exit()


#Defining a funtion to make the name square througout the game 
def ehrensverdska_adventure():
    #The colors for the square
    GREEN = "\033[32m"
    RESET = "\033[0m"
    print(f"{GREEN}|{RESET}                                 _______________________________________________________                              {GREEN}|{RESET}")
    print(f"{GREEN}|{RESET}                                 |                                                      |                             {GREEN}|{RESET}")
    print(f"{GREEN}|{RESET}                                 |               ADVENTURE IN EHRENSVERDSKA             |                             {GREEN}|{RESET}")
    print(f"{GREEN}|{RESET}                                 |______________________________________________________|                             {GREEN}|{RESET}")


#Defining funktion to make the vertical lines of the square
def common_lines_vert():
    GREEN = "\033[32m"
    RESET = "\033[0m"
    MAIN_LINE=f"{GREEN}-{RESET}"
    MY_PIPE=f"{GREEN}|{RESET}"
    MY_SPACE=" "
    #Loop to print the vertical lines of the rectangle 
    for i in range (1,11):
        print(MY_PIPE, end="")
        for j in range(1,119):
            print(MY_SPACE, end="" )
        print(MY_PIPE)

#Defining funktion to make the horizontal lines of the square
def common_lines_hor ():
    GREEN = "\033[32m"
    RESET = "\033[0m"
    MAIN_LINE=f"{GREEN}-{RESET}"
    MY_PIPE=f"{GREEN}|{RESET}"
    MY_SPACE=" "
    #Loop to print the horizontal line at the top of the rectangle
    for i in range(1,119):
        print( MAIN_LINE, end="" )
        if i == 118:
            print(MAIN_LINE)

#Defing an funtion for exiting the progam 
def exit_program():
        sys.exit()

def background_color(color):
    RESET = "\033[49m"
    if color == 1:
        YELLOW="\033[43m"
        print(f"{YELLOW}-----------------------------------------------------------------------------------------------------------------------{RESET}")
    elif color == 2:
        BLUE = "\033[44m"
        print(f"{BLUE}-----------------------------------------------------------------------------------------------------------------------{RESET}")
    elif color == 3:
        MAGENTA="\033[45m"
        print(f"{MAGENTA}-----------------------------------------------------------------------------------------------------------------------{RESET}")
    elif color == 4:
        CYAN = "\033[46m"
        print(f"{CYAN}-----------------------------------------------------------------------------------------------------------------------{RESET}")
    elif color == 5:
        PINK = "\033[105m"
        print(f"{PINK}-----------------------------------------------------------------------------------------------------------------------{RESET}")
    elif color == 6:
        RED = "\033[41m"
        print(f"{RED}-----------------------------------------------------------------------------------------------------------------------{RESET}")

def heath_icon(health):
    #health = 100
    if health == 100:
        my_icon = "AWESOME"
    elif health == 80:
        my_icon = "LOL"
    elif health == 60:
        my_icon= "UWU"
    elif health == 40:
        my_icon = "YOLO"
    elif health == 20:
        my_icon = "SHEIT"
    elif health == 0:
        my_icon = "WTF"
    return(my_icon)

