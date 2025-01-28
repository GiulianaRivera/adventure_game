
'''
--------------------------
Name: Giuliana Rivera
School: Ehrensvarska Gymnasiet 
Class: TE2A
e-mail: giulianabelen.riverarecinos.e@skola.karlskrona.se
Version: 
Revision:
Module name: Minigames
Latest update: 2025/01/27
--------------------------
'''
#In this module I will put the funtions for the minigames that players need to play to get the key to the rooms. 
#Imports
import random

#Defining a funtion to a mini game of guess the random
def mini_guess_number(health):

    #Color Variables
    RED = "\033[31m"
    LIGHT_BLUE = "\033[94m"
    RESET = "\033[0m"
    #Variables 
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
            return(0,health)
            break
        elif attempt_count == 4:
            print(f"{RED}You failed to get a hold of the key. Get out of here!{RESET}")
            health -= 20
            return (20, health)
        elif guess < random_number:
            print("WRONG!! Too low, guess a higher number ◕_◕")
        elif guess > random_number:
            print("WRONG!! Too high, guess a lower number bro (◔_◔)")
    
        attempt_count += 1


#defining a funtion to rock paper scissor game 
def mini_rock_papper_scissor(health):
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
            return(0,health)
            break
        elif wins_computer == 3:
            print(f"{RED}I win you looser, GET OUT! {RESET} (•-•)⌐")
            health -= 20
            return (20, health)
            break
    
#Defining funtion to mini 21 game
def mini_21(health):

    #Variables
    #Color variables
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


#Defining funtion to hangman game
def mini_hangman(health):
    # Function to randomly choose a word from the list
    def words():
        hangman_list = ["Ergonomi", "Konditionsträning", "Aerob", "Stressorer", "Stretch"]
        return random.choice(hangman_list).lower()

    # Function to show the word with guessed letters revealed
    def show_guesses(word, guessed_letters):
        showing = ""
        for letter in word:
            if letter in guessed_letters:
                showing += letter
            else:
                showing += "_"
        return showing

    # Main game function
    
    #Color variables
    RED = "\033[31m"
    LIGHT_BLUE = "\033[94m"
    RESET = "\033[0m" 

    word = words()
    guessed_letters = set()  # To store unique guessed letters
    wrong_guesses = 0
    max_wrong_guesses = 6

    print("You have now entered the prestigious Aula-D, where thousands of students have failed.")
    print("You will face off against Samuel in a game of hangman")
    print("If you loose you will loose 20 health points, if you win you get the key to this room")

    while wrong_guesses < max_wrong_guesses:
        # Display the current state of the word
        print(f"The word: {show_guesses(word, guessed_letters)}")
        print(f"Wrong guesses left: {max_wrong_guesses - wrong_guesses}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}\n")

        # Player input
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("You have to guess one letter only!")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        # Check if the guess is in the word
        if guess in word:
            print(f"Good guess! The letter '{guess}' is in the word.\n")
        else:
            wrong_guesses += 1
            print(f"Wrong! The letter '{guess}' is not in the word. ({wrong_guesses}/{max_wrong_guesses} wrong guesses)\n")
                

        # Check if the player has guessed the whole word
        if all(letter in guessed_letters for letter in word):
            print(f"{LIGHT_BLUE}You win! You guessed the whole word: {RESET} {word}!")
            print(health)
            return(0,health)
            break

    # If the player runs out of guesses
    print(f"You lose! The word was: {word}.")
    health -= 20
    print(health)
    return (20, health)


def last_quest(health):
    print("Please answer this question in swedish with small letter (iykyk)")
    question= input("What does Atom mean?: ")

    if question == "odelbar":
        print("You won!, nicely done! 🗝")
        return(0,health)

    else:
        print("Try again later, maybe you will be smarter then.")
        health -= 20
        return (20, health)
