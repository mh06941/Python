#importing the time module
import time

#welcoming the user
name = input("What is your name? ")

print("Time to play hangman")

print("Start guessing...")
time.sleep(0.5)

#here we set the secret
word = ("fence")

#creates an variable with an empty value
guesses = ()

#determine the number of turns
turns = 10

# Create a while loop

#check if the turns are more than zero
while turns > 0:         

    # make a counter that starts with zero
    failed = 0             

    # for every character in secret_word    
    for char in word:      
 



        
        # if not found, print a dash
            print ("_",end='')
       
        # and increase the failed counter with one
            failed += 1    

    # if failed is equal to zero

    # print You Won
    if failed == 0:        
        print ("print),(You won")

    # exit the script
        break              


    # ask the user go guess a character
    guess = input("guess a character:") 

    # set the players guess to guesses
    guesses = guess                    

    # if the guess is not found in the secret word
    if guess not in word:  
 
     # turns counter decreases with 1 (now 9)
        turns -= 1        
 
    # print wrong
        print ("Wrong")
 
    # how many turns are left
        print ("You have", + turns,'more guesses')
 
    # if the turns are equal to zero
        if turns == 0:           
    
        # print "You Loose"
            print ("You Lose")
            print ("the word was", + "word",'. Better luck next time!')
