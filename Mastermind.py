
#setting up variables
range=5
import random
answer1=random.randint(1,range)
answer2=random.randint(1,range)
while answer1==answer2:
    answer2=random.randint(1,range)

# the funtions
def intro():
    print("Welcome to mastermind........avec le numerique.")
    print("I have two numbers raging from 1 to 10.")
    print("When you guess, I will tell you wether both are wrong, one is wrong, or both are right!.")
    print("Begin Guessing!")
def bothwrong():
    print("Both of the numbers are wrong!")
    print("Guess again!")
def onewrong():
    print("Only one of your answers are wrong.")
    print("Try Again.")
def entering():
    print("Please enter the first number below.")
    guess1=int(input())
    print("Please enter the second number below.")
    guess2=int(input())
def youwon():
    print("Congrats! You won!")
#the code
intro()
print("The first number is" + str(answer1) + " the second number is" + str(answer2) + ".")
print("Please enter the first number below.")
guess1=int(input())
print("Please enter the second number below.")
guess2=int(input())

while guess1!=answer1 and guess2!=answer2:
    while (guess1!=answer1 and guess2) or (guess1!=answer2 and guess2!=answer1):
        bothwrong()
        print("Please enter the first number below.")
        guess1=int(input())
        print("Please enter the second number below.")
        guess2=int(input())

    while guess1==answer1 or guess2==answer2:
        onewrong()
        print("Please enter the first number below.")
        guess1=int(input())
        print("Please enter the second number below.")
        guess2=int(input())

if guess1==answer1 and guess2==answer2:
    youwon()

    
    
    
    
    

