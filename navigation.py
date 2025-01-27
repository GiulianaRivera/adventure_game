'''
--------------------------
Name: Giuliana Rivera
School: Ehrensvarska Gymnasiet 
Class: TE2A
e-mail: giulianabelen.riverarecinos.e@skola.karlskrona.se
Version: 
Revision:
Module name: Navigation
Latest update: 
--------------------------
'''

import common
import game_over
import icons
import time
import door
import menu
import os 
import food 
def game_navigation(first_time):

    GREEN = "\033[32m"
    RESET = "\033[0m"
    MAIN_LINE=f"{GREEN}-{RESET}"
    MY_PIPE=f"{GREEN}|{RESET}"
    MY_SEPARATOR= F"{GREEN} > {RESET}"
    MY_SPACE=" "

    GREEN = "\033[32m"
    RESET = "\033[0m"
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    #AWESOME = '\n|%%%|\n(o¿o)\n--[]--\n_| |_\n\nAWESOME!!\n'
    #WTF = '|%%%|\n(X¿X)\n--[]-- \n_| |_\n\nWTF!!\n'
    #UWU = '|%%%|\n(u¿u)\n--[]--\n_| |_\n\nUwwU\n'
    #YOLO = '|%%%|\n(-¿-)\n--[]--\n_| |_\n\nYOLO\n'
    #LOL = '|%%%|\n(C.¿.)\n--[]--\n_| |_\n\nLOL\n'
    #SHEIT = '|%%%|\n(t¿t)\n--[]--\n_| |_\n\nSHEIT\n'

    AWESOME = f"{BOLD}\n|%%%|\n(o¿o)\n--[]--\n_| |_\n\n{RESET}{GREEN}AWESOME!!\n{RESET}"
    WTF = f'{BOLD}|%%%|\n(X¿X)\n--[]-- \n_| |_\n\n{RESET}{FAIL}WTF!!\n{RESET}'
    UWU = f'{BOLD}|%%%|\n(u¿u)\n--[]--\n_| |_\n\n{RESET}{GREEN}UwwU\n{RESET}'
    YOLO = f'{BOLD}|%%%|\n(-¿-)\n--[]--\n_| |_\n\n{RESET}{WARNING}YOLO\n{RESET}'
    LOL = f'{BOLD}|%%%|\n(C.¿.)\n--[]--\n_| |_\n\n{RESET}{OKCYAN}LOL\n{RESET}'
    SHEIT = f'{BOLD}|%%%|\n(t¿t)\n--[]--\n_| |_\n\n{RESET}{FAIL}SHEIT\n{RESET}'

    #Rooms = ( name, navigation_key )
    aula_d = ("AULA D",'w')
    selma = ("SELMA ROOM",'q')
    matsal = ("CAFETERIA",'e')
    expedition = ("EXPEDITION",'a')
    d048 = ("D048", 's')
    d017 = ("D017", 'd')
    lobby = ("LOBBY", 'h')

    #Initial values
    #Floor = [rooms]
    floor_name_default = "ENTRANCE"
    floor = [lobby, matsal, expedition, aula_d, selma, d048, d017 ]
    if first_time == True:
        rendering = 1
  
        #Live 100%
        #health = 100
        #health = 100
        #When the game starts the health will be 100
        health = 100
        #health_dif_selma = 0

        #if the player has the key it will be True but if they dont all of them are false 
        #All the keys give you the key to the final room 
        keys = [False, False, False, False, False ]

        #Weapons = [ sword, shield ]
        weapons = [ ("SWORD", False), ("SHIELD",False) ]
        first_time = False

        #Food
        food_0 = True # Bread
        food_1 = True #Cafe
    while True:
        #Dead routine
        if health <= 0:
            print("You died.")
            time.sleep(2)
            game_over.game_over()
        #START LOBBY
        if rendering == 1:
            #Where i am: lobby
            my_navigation = [lobby] 

            #Floor name
            floor_name = floor_name_default
            #print(floor_name)

            #Room
            for i in my_navigation:
                current_room, room_key = i
                #print(current_room)

            #Health
            my_health = health 

            #Update keys
           # if health_dif_selma == 0:
              #  keys[0] = True
            #else:
             #   keys[0] = False 

            #Weapons
            my_weapons = weapons
            for i in enumerate(my_weapons):
                numero, tuppletemp = i
                if numero == 0:
                    sword,sword_enable = tuppletemp
                if numero == 1:
                    shield,shield_enable = tuppletemp

            #print("shield")
            #print(shield)
            #print("shield_enable")
            #print(shield_enable)

            #print("sword")
            #print(sword)
            #print("sword_enable")
            #print(sword_enable)

            #Current place
            for i in  my_navigation:
                room,key = i
                #print(room)
                #print(key)

            _my_key_count= 0
            for i in keys:
                if i == True: 
                    _my_key_count +=1
            
            _my_keys = str(_my_key_count) + "🗝"


            my_string = floor_name + MY_SEPARATOR + current_room + MY_SEPARATOR +  str(my_health) + MY_SEPARATOR + str(weapons) + MY_SEPARATOR + _my_keys
            #print(my_string)

            loobypic = True
            is_chef = False
            #Room color
            room_color = 1

        elif rendering == 2:

            #Where i am: AULA D
            my_navigation = [aula_d]

            #Floor name
            floor_name = floor_name_default
            #print(floor_name)

            #Room
            for i in my_navigation:
                current_room, room_key = i
                #print(current_room)

            #Health
            my_health = health


            #Weapons
            my_weapons = weapons
            for i in enumerate(my_weapons):
                numero, tuppletemp = i
                if numero == 0:
                    sword,sword_enable = tuppletemp
                if numero == 1:
                    shield,shield_enable = tuppletemp

            #print("shield")
            #print(shield)
            #print("shield_enable")
            #print(shield_enable)

            #print("sword")
            #print(sword)
            #print("sword_enable")
            #print(sword_enable)

            #Current place
            for i in  my_navigation:
                room,key = i
                #print(room)
                #print(key)

            _my_key_count= 0
            for i in keys:
                if i == True: 
                    _my_key_count +=1
            
            _my_keys = str(_my_key_count) + "🗝"


            my_string = floor_name + MY_SEPARATOR + current_room + MY_SEPARATOR +  str(my_health) + MY_SEPARATOR + str(weapons) + MY_SEPARATOR + _my_keys
            #print(my_string)

            loobypic = False
            is_chef = False
            #Room color
            room_color = 1

        elif rendering == 3:

            #Where i am: selma
            my_navigation = [selma] 

            #Floor name
            floor_name = floor_name_default
            #print(floor_name)

            #Room
            for i in my_navigation:
                current_room, room_key = i
                #print(current_room)

            #Health
            my_health = health 
            
            #Update keys
            '''
            if health_selma == 0:
                keys[0] = True
            else:
                keys[0] = False 
                '''
            #Weapons
            my_weapons = weapons
            for i in enumerate(my_weapons):
                numero, tuppletemp = i
                if numero == 0:
                    sword,sword_enable = tuppletemp
                if numero == 1:
                    shield,shield_enable = tuppletemp

            #print("shield")
            #print(shield)
            #print("shield_enable")
            #print(shield_enable)

            #print("sword")
            #print(sword)
            #print("sword_enable")
            #print(sword_enable)

            #Current place
            for i in  my_navigation:
                room,key = i
                #print(room)
                #print(key)

            _my_key_count= 0
            for i in keys:
                if i == True: 
                    _my_key_count +=1
            
            _my_keys = str(_my_key_count) + "🗝"


            my_string = floor_name + MY_SEPARATOR + current_room + MY_SEPARATOR +  str(my_health) + MY_SEPARATOR + str(weapons) + MY_SEPARATOR + _my_keys
            #print(my_string)

            loobypic = False
            is_chef = False

            #Room color
            room_color = 2

        if rendering == 4:

            #Where i am: matsal 
            my_navigation = [matsal] 

            #Floor name
            floor_name = floor_name_default
            #print(floor_name)

            #Room
            for i in my_navigation:
                current_room, room_key = i
                #print(current_room)

            #Health
            my_health = health

            #Weapons
            my_weapons = weapons
            for i in enumerate(my_weapons):
                numero, tuppletemp = i
                if numero == 0:
                    sword,sword_enable = tuppletemp
                if numero == 1:
                    shield,shield_enable = tuppletemp

            #print("shield")
            #print(shield)
            #print("shield_enable")
            #print(shield_enable)

            #print("sword")
            #print(sword)
            #print("sword_enable")
            #print(sword_enable)

            #Current place
            for i in  my_navigation:
                room,key = i
                #print(room)
                #print(key)

            _my_key_count= 0
            for i in keys:
                if i == True: 
                    _my_key_count +=1
            
            _my_keys = str(_my_key_count) + "🗝"


            my_string = floor_name + MY_SEPARATOR + current_room + MY_SEPARATOR +  str(my_health) + MY_SEPARATOR + str(weapons) + MY_SEPARATOR + _my_keys
            #print(my_string)

            loobypic = False
            is_chef = True
            #Room color
            room_color = 3

        if rendering == 5:

            #Where i am: expedition 
            my_navigation = [expedition] 

            #Floor name
            floor_name = floor_name_default
            #print(floor_name)

            #Room
            for i in my_navigation:
                current_room, room_key = i
                #print(current_room)

            #Health
            my_health = health

            #Weapons
            my_weapons = weapons
            for i in enumerate(my_weapons):
                numero, tuppletemp = i
                if numero == 0:
                    sword,sword_enable = tuppletemp
                if numero == 1:
                    shield,shield_enable = tuppletemp

            #print("shield")
            #print(shield)
            #print("shield_enable")
            #print(shield_enable)

            #print("sword")
            #print(sword)
            #print("sword_enable")
            #print(sword_enable)

            #Current place
            for i in  my_navigation:
                room,key = i
                #print(room)
                #print(key)

            _my_key_count= 0
            for i in keys:
                if i == True: 
                    _my_key_count +=1
            
            _my_keys = str(_my_key_count) + "🗝"


            my_string = floor_name + MY_SEPARATOR + current_room + MY_SEPARATOR +  str(my_health) + MY_SEPARATOR + str(weapons) + MY_SEPARATOR + _my_keys
           
            #print(my_string)

            loobypic = False
            is_chef = False

            #Room color
            room_color = 6

        if rendering == 6:

            #Where i am: d048
            my_navigation = [d048] 

            #Floor name
            floor_name = floor_name_default
            #print(floor_name)

            #Room
            for i in my_navigation:
                current_room, room_key = i
                #print(current_room)

            #Health
            my_health = health

            #Weapons
            my_weapons = weapons
            for i in enumerate(my_weapons):
                numero, tuppletemp = i
                if numero == 0:
                    sword,sword_enable = tuppletemp
                if numero == 1:
                    shield,shield_enable = tuppletemp

            #print("shield")
            #print(shield)
            #print("shield_enable")
            #print(shield_enable)

            #print("sword")
            #print(sword)
            #print("sword_enable")
            #print(sword_enable)

            #Current place
            for i in  my_navigation:
                room,key = i
                #print(room)
                #print(key)

            _my_key_count= 0
            for i in keys:
                if i == True: 
                    _my_key_count +=1
            
            _my_keys = str(_my_key_count) + "🗝"


            my_string = floor_name + MY_SEPARATOR + current_room + MY_SEPARATOR +  str(my_health) + MY_SEPARATOR + str(weapons) + MY_SEPARATOR + _my_keys
            #print(my_string)

            loobypic = False
            is_chef = False
            #Room color
            room_color = 4

        if rendering == 7:

            #Where i am: d017 
            my_navigation = [d017] 

            #Floor name
            floor_name = floor_name_default
            #print(floor_name)

            #Room
            for i in my_navigation:
                current_room, room_key = i
                #print(current_room)

            #Health
            my_health = health

            #Weapons
            my_weapons = weapons
            for i in enumerate(my_weapons):
                numero, tuppletemp = i
                if numero == 0:
                    sword,sword_enable = tuppletemp
                if numero == 1:
                    shield,shield_enable = tuppletemp

            #print("shield")
            #print(shield)
            #print("shield_enable")
            #print(shield_enable)

            #print("sword")
            #print(sword)
            #print("sword_enable")
            #print(sword_enable)

            #Current place
            for i in  my_navigation:
                room,key = i
                #print(room)
                #print(key)

            _my_key_count= 0
            for i in keys:
                if i == True: 
                    _my_key_count +=1
            
            _my_keys = str(_my_key_count) + "🗝"


            my_string = floor_name + MY_SEPARATOR + current_room + MY_SEPARATOR +  str(my_health) + MY_SEPARATOR + str(weapons) + MY_SEPARATOR + _my_keys
            #print(my_string)

            loobypic = False
            is_chef = False

            #Room color
            room_color = 5

        common.common_lines_hor()
        common.ehrensverdska_adventure()
        common.common_lines_hor()
        common.background_color(room_color)
        print()
        print(my_string)
        print()
        
        if loobypic == True:
            icons.game_emoji('LOBBYPIC')
            #print()
        if is_chef == True:
            my_chef =food.game_chef(health, food_0,food_1)
            my_chef_health, my_chef_food_0, my_chef_food_1 = my_chef
            health = my_chef_health
            food_0 = my_chef_food_0
            food_1 = my_chef_food_1 

        health_icon = common.heath_icon(health)
        #print(health_icon)
        icons.game_emoji(health_icon)

        common.background_color(room_color)
        common.common_lines_hor()
    
        #Floor menu
        print("AVAILABLE ROOMS ARE:")
        print()
        for i in floor:
            room_name,menu_key = i
            if room_name != current_room:
                _my_string = "[ " + menu_key + " ]  ⚀  " + room_name
                print(_my_string)
                print()

        _my_string = "[ m ]  ⚀  GO TO HOME MENU"
        print(_my_string)
        print()
        _my_option = input( "WHERE DO YOU WANT TO GO: " )
        print()
        if _my_option  == 'h':
            print("LOBBY")
            rendering = 1
            os.system('cls')
            door.game_door_animation('LOBBY',1,True,health)
            time.sleep(1)
            os.system('cls')
        elif _my_option == 'w':
            print("AULA D")
            os.system('cls')
            main_result_aulad= door.game_door_animation('AULA D',1,keys[1],health) #(0 or 20, health-0 or health-20)(0,100)
            if keys[1]== False:
                #print(main_result_aulad)
                
                aulad_result, health_aulad = main_result_aulad
                health = health_aulad

                if aulad_result == 0:
                    keys[1]=True
                    rendering = 2
                else:
                    rendering = 1
            else:
                rendering = 2

            time.sleep(1)
            os.system('cls')
            
        elif _my_option == 'q':
            print("SELMA ROOM")
            os.system('cls')
            main_result_selma= door.game_door_animation('SELMA ROOM',2,keys[0], health) #(0 or 20, health-0 or health-20)(0,100)
            if keys[0]== False:
                selma_result, health_selma = main_result_selma
                health = health_selma

                if selma_result == 0:
                    keys[0]=True
                    rendering = 3
                else:
                    rendering = 1
            else:
                rendering = 3

            time.sleep(1)
            os.system('cls')
        elif _my_option == 'e':
            print("CAFETERIA")
            os.system('cls')
            main_result_cafeteria= door.game_door_animation('CAFETERIA',6,True, health) #(0 or 20, health-0 or health-20)(0,100)
            rendering = 4
            
            time.sleep(1)
            os.system('cls')

           
        elif _my_option == 'a':
            print("EXPEDITION")
            '''
            os.system('cls')
            main_result_d048= door.game_door_animation('D048',4,keys[2], health) #(0 or 20, health-0 or health-20)(0,100)
            if keys[2]== False:
                d048_result, health_d048 = main_result_d048
                health = health_d048

                if d048_result == 0:
                    keys[2]=True
                    rendering = 6
                else:
                    rendering = 1
            else:
                rendering = 6
            time.sleep(1)
            os.system('cls')

            '''
            '''
            print('EXPEDITION')
            rendering = 5
            os.system('cls')
            door.game_door_animation('EXPEDITION',6,True)
            time.sleep(1)
            os.system('cls')
            '''
        elif _my_option == 's':
            print("D048")
            os.system('cls')
            main_result_d048= door.game_door_animation('D048',4,keys[2], health) #(0 or 20, health-0 or health-20)(0,100)
            if keys[2]== False:
                d048_result, health_d048 = main_result_d048
                health = health_d048

                if d048_result == 0:
                    keys[2]=True
                    rendering = 6
                else:
                    rendering = 1
            else:
                rendering = 6
            time.sleep(1)
            os.system('cls')

            '''
            print('D048')
            rendering = 6
            '''
        elif _my_option == 'd':
            print("D017")
            os.system('cls')
            main_result_d017= door.game_door_animation('D017',3,keys[3], health) #(0 or 20, health-0 or health-20)(0,100)
            if keys[3]== False:
                d017_result, health_d017 = main_result_d017
                health = health_d017

                if d017_result == 0:
                    keys[3]=True
                    rendering = 7
                else:
                    rendering = 1
            else:
                rendering = 7
            time.sleep(1)
            os.system('cls')

        elif _my_option == 'm':
            os.system('cls')
            menu.game_menu()
            time.sleep(1)
            os.system('cls')
        else:
            print('INCORRECT  OPTION')
            
            time.sleep(1)
            os.system('cls')

