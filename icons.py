def game_emoji( my_face ):

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

    #AWESOME = f'{BOLD}|%%%|\n(o¿o)\n--[]--\n_| |_\n\n{RESET}{GREEN}AWESOME!!\n{RESET}'

    AWESOME = f"{BOLD}\n|%%%|\n(o o)\n--[]--\n_| |_\n\n{RESET}{GREEN}AWESOME!!\n{RESET}"
    WTF = f'{BOLD}|%%%|\n(X X)\n--[]-- \n_| |_\n\n{RESET}{FAIL}WTF!!\n{RESET}'
    UWU = f'{BOLD}|%%%|\n(u u)\n--[]--\n_| |_\n\n{RESET}{GREEN}OH NOO\n{RESET}'
    YOLO = f'{BOLD}|%%%|\n(- -)\n--[]--\n_| |_\n\n{RESET}{WARNING}YOLO\n{RESET}'
    LOL = f'{BOLD}|%%%|\n(C. .)\n--[]--\n_| |_\n\n{RESET}{OKCYAN}LOL\n{RESET}'
    SHEIT = f'{BOLD}|%%%|\n(t t)\n--[]--\n_| |_\n\n{RESET}{FAIL}SHEIT\n{RESET}'  
    BREAD = f"( `^` ))\n|     ||\n|     ||\n'-----'`\n\n"
    CAFE = f"  ( (\n  ) )\n(----)-)\n \\__/-'\n`----'\n\n"
    DOOR = f" __________\n|  __  __  |\n| |  ||  | |\n| |  ||  | |\n| |__||__| |\n|  __  __()|\n| |  ||  | |\n| |  ||  | |\n| |  ||  | |\n| |  ||  | |\n| |__||__| |\n|__________|\n\n"
    SPADE = f"         />_________________________________\n[########[]_________________________________>\n         \\>\n"
    SHIELD = f"|`-._/\\_.-`|\n|    ||    |\n|___o()o___|\n|__((<>))__|\n\\   o\\/o   /\n \\   ||   /\n  \\  ||  /\n   '.||.'\n     ``\n"
    LOBBYPIC = f" _____________________________________________\n|.'',                LOBBY                ,''.|\n|.'.'',                                 ,''.'.|\n|.'.'.'',                             ,''.'.'.|\n|.'.'.'.'',                         ,''.'.'.'.|\n|.'.'.'.'.|                         |.'.'.'.'.|\n|.'.'.'.'.|===;                 ;===|.'.'.'.'.|\n|.'.'.'.'.|:::|',             ,'|:::|.'.'.'.'.|\n|.'.'.'.'.|---|'.|, _______ ,|.'|---|.'.'.'.'.|\n|.'.'.'.'.|:::|'.|'|???????|'|.'|:::|.'.'.'.'.|\n|,',',',',|---|',|'|???????|'|,'|---|,',',',',|\n|.'.'.'.'.|:::|'.|'|???????|'|.'|:::|.'.'.'.'.|\n|.'.'.'.'.|---|','   /%%%\\   ','|---|.'.'.'.'.|\n|.'.'.'.'.|===:'    /%%%%%\\    ':===|.'.'.'.'.|\n|.'.'.'.'.|%%%%%%%%%%%%%%%%%%%%%%%%%|.'.'.'.'.|\n|.'.'.'.','       /%%%%%%%%%\\       ','.'.'.'.|\n|.'.'.','        /%%%%%%%%%%%\\        ','.'.'.|\n|.'.','         /%%%%%%%%%%%%%\\         ','.'.|\n|.','          /%%%%%%%%%%%%%%%\\          ','.|\n|;____________/%%%%%%%%%%%%%%%%%\\____________;|\n\n"

    if my_face == 'LOBBYPIC':
        print(LOBBYPIC)
    if my_face == 'AWESOME':
        print(AWESOME)
    elif my_face == 'WTF':
        print(WTF)
    elif my_face == 'UWU':
        print(UWU)
    elif my_face == 'YOLO':
        print(YOLO)
    elif my_face == 'LOL':
        print(LOL)
    elif my_face == 'SHEIT':
        print(SHEIT)
    elif my_face == 'ENTER':
        print()
    elif my_face == 'SPADE':
        print(SPADE)
    elif my_face == 'SHIELD':
        print(SHIELD)
    elif my_face == 'DOOR':
        print(DOOR)
    elif my_face == 'BREAD':
        print(BREAD)
    elif my_face == 'CAFE':
        print(CAFE)


