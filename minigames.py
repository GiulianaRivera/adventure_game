
'''
--------------------------
Name: Giuliana Rivera
School: Ehrensvarska Gymnasiet 
Class: TE2A
e-mail: giulianabelen.riverarecinos.e@skola.karlskrona.se
Version: 
Revision:
Module name: Minigames
Latest update: 
--------------------------
'''

#Imports
import random

def mini_guess_number():

    #Variabler 
    RED = "\033[31m"
    LIGHT_BLUE = "\033[94m"
    RESET = "\033[0m"
    INTRO_GAME = "To enter this room you will have to guess a number between 1 and 20, you have five attempts. You needing luck is an understatement"
    random_number = random.randint(1,20)
    #print(random_number)
    attempts_number = 4
    attempt_count = 0

    print(INTRO_GAME)
    while attempt_count <= attempts_number:
        guess = int(input("Insert a number between 1 - 20: "))
        #print(guess)
        if guess == random_number:
            print(f"{LIGHT_BLUE} You guessed it rigth you may enter. Here you go {RESET}🗝")
            break
        elif attempt_count == 4:
            print(f"{RED}You failed to get a hold of the key. Get out of here!{RESET}")
        
        elif guess < random_number:
            print("WRONG!! Too low, guess a higher number ◕_◕")
        elif guess > random_number:
            print("WRONG!! Too high, guess a lower number bro (◔_◔)")
    
        attempt_count += 1

def mini_rock_papper_scissor():
    #Variables 
    RED = "\033[31m"
    LIGHT_BLUE = "\033[94m"
    RESET = "\033[0m"

    INTRO_GAME = "To enter this room you will play rock papper scissor. I hope you know how to play it because I dont got time to explain it. The game id best of five"
    random_item = random.randint(1,3)
    #1=rock, 2= papper, 3= scissor
    #print(random_number)
    
    wins_computer = 0
    wins_person = 0


    print(INTRO_GAME)
    print()
    print("[1] ☆ stone")
    print()
    print("[2] [̲̅$̲̅(̲̅ιο̲̅̅)̲̅$̲̅] paper")
    print()
    print("[3] ⚔︎ scissor") 
    print()
    while True:
    
        random_item = random.randint(1,3)
    
        guess = int(input("Choose a number above: "))
        #print(guess)
        if guess == random_item :
            print("we are tied, no points |(◉‿◉)|")
        elif guess == 1 and random_item == 2:
            print("Bagged a point, try to keep up.")
            wins_computer += 1        
            
        elif guess == 1 and random_item == 3:
            print("You got it! You got lucky.")
            wins_person += 1
            
        elif guess == 2 and  random_item == 1:
            print("You got it! You got lucky.")
            wins_person += 1
            
        elif guess == 2 and random_item == 3:
            print("Bagged a point, try to keep up.")
            
            wins_computer += 1
            
        elif guess == 3 and random_item == 1:
            print("Bagged a point, try to keep up.")
           
            wins_computer += 1
            
        elif guess == 3 and random_item == 2:
            print("You got it! You got lucky.")
            wins_person += 1

        print( "I got option", random_item)
        score="The score is " + str(wins_computer) + "(me)  - " + str(wins_person) + "(you)"    
        print(score)
        print()
        if wins_person == 3:
            print (f"{LIGHT_BLUE}You win, it wasnt terrible. Here you go {RESET}🗝")
            break
        elif wins_computer == 3:
            print(f"{RED}I win you looser, GET OUT! {RESET} (•-•)⌐")
            break
    

def mini_21(health):

    #Variables
    RED = "\033[31m"
    LIGHT_BLUE = "\033[94m"
    RESET = "\033[0m" 
    INTRO_GAME = "You can add one or two to the inital score which is 0, then is my turn. The first one to get to 21 wins."
    random_item = random.randint(1,3)
    #1=rock, 2= papper, 3= scissor
    #print(random_number)
    
    count = 0
    guess = 0
    random_item = 0

    print(INTRO_GAME)
   
    while True:
        guess = input("Choose a number(interger) between 1 and 2: ")
        if guess == "1" or guess == "2":
            flag = "person"
            count = count + int(guess)
            print("The count is : ", str(count))

            if count == 21 and flag == "person":
                print(f"{LIGHT_BLUE}YOU GOT IT!, here you go {RESET}◕_◕ 🗝 ")
                
                return(0,health)
            
                break
            else:
                flag = "computer"
            if count == 20:
                random_item = 1
            elif count == 19:
                random_item = 2
            else: 
                random_item = random.randint(1,2)
            count = count + random_item

        else:
            print("Choose between one and two, stop trying to hack the system.")
        if count < 21:
            print("(⊙＿⊙') I pick",random_item)
            print("The count is : ", str(count))
            print()
        elif count == 21 and flag == "computer":
            print(f"{RED}YOU LOOSE! {RESET}*holding my hand with an L ")
            health -= 20
            return (20, health)
            break           

