#This is a number guessing game that is based on the code from "Inventing with Python" by Al Sweigart
#The code has been modified to add more features such as a restart option, an error messages for certain inputs.
import random
import time
import sys

def displayIntro():
    print ('This is a simple number guessing game, you will have six chances to guess a randomly generated number!')
    print ()

def gameStart():
    guessesTaken = 0
    number = random.randint (1, 25)
    print ('Hello sir or Madem, what is your name?')
    myName = input()
    print()
    print ('Well then, ' + myName + ', I have generated a number between 1 and 25.')
    time.sleep (1)
    print()
    while guessesTaken < 6:
        try:
            guessesTaken = guessesTaken + 1
            guess = int(input('Why don\'t you take a guess?\n'))       
            if guess <= 0 or guess >= 26:
                time.sleep (1)
                print()
                print ('That is not a number between 1 and 25, Try again')
                print()
                
            elif guess < number:
                time.sleep (1)
                print()
                print ('Your guess is too low.')
                print()

            elif guess > number:
                time.sleep (1)
                print()
                print('Your guess is too high.')
                print()

        except ValueError:
            time.sleep(1)
            print()
            print('Uh-Oh that is not a number, please enter a number between 1 and 25')
            print()
            continue

        if guess == number or guessesTaken > 6:
            break
        
    if guess == number:
        time.sleep (1)
        guessesTaken = str(guessesTaken)
        print()
        print('Excellent choice, ' + myName + '! You have guessed my number in ', str(guessesTaken), ' attempts!')

    if guess != number:
        time.sleep(1)
        number = str(number)
        print ()
        print ('I am sorry, but the number I have generated is ' + number + '.')
    return myName

def playAgain():
    playAgain = 'yes'
    yes = ['yes','Yes','y','Y','yep','Yep','yeah','YEs','YeS','YES',]
    no = ['no','No','n','N','Nope','nope','nah','Nah','NO']

    
    while playAgain in yes: 
        time.sleep(1)
        print()
        displayIntro()
        gameStart()
        print()
        print('Would you like to play again?')
        playAgain = input()
        if playAgain in yes:
            print ('Restarting game, please wait...')
        elif playAgain in no:
            print('Thank you for playing friend and have a nice day!')
        else:
            print ('I am afraid I can\'t do that Dave...')



if __name__ == '__main__':
    try:
        playAgain()
    except:
        import sys
        print (sys.exc_info()[0])
        import traceback
        print (traceback.format_exc())
    finally:
        print ("Press Enter to continue ...") 
        input()
        
