import time
import random
name = input("What is your name??")

print ("Welcome," + name , "Time To Play!!")

time.sleep(2)

print("start guessing....")
time.sleep(1)

words=["wordone","wordtwo"]
#here we set the secret
word = random.choice(words)

#Create a variable with an empty value
guesses = " "

#determine number of turns
turn = 10

#check is the turns are more than zero
while(turn >0):

    #make a counter that starts with zero

    failed = 0

    #for every character in secret_word
    for char in words:
        #see if the character is in the player's guess
        if char in guesses:
            print(char)

        else:
            #If not found, print dash
            print("_________")
            failed += 1

    if failed == 0:
        print("You won !!")

        break

    guess = input("guess a characted:")

    #set the players guess to guesses
    guesses += guess

    #if the guess is not found in the secret word
    if guess not in words:

        #turns counter decreases with 1
        turn -=1
        print("wrong")
        #how many turns left
        print("you have", + turn, 'more guuesses')

        #If the turns are equal to zero
        if turn ==0:
            print("you lose")
