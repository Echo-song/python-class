import random

door =9

livesLeft=3
x=300

def intro ():
    print("Welcome to the game Andrew, Gloria or housecats.")
    print("U, the great Elizabeth Li is infront of 9 great doors.")
    print("Behind one of the doors is Gloria Zhu.")
    print("After marrying Gloria each time, you will lose a life.")
    print("Behind another door is Andrew Chen")
    print("After marrying Andrew each time, you will earn a life.")
    print("There are housecats behind all other doors.")
    print("YOu have three lives.")
    print("If there is a person behind the door You will marry he/she")
    print("Which door #1-9 will you chose?")


def gloria ():
      print("Gloria is behind the door!")
      print("CONGRADULATIONS!!!U just married Gloria!")
      print("You have " + str(livesLeft) + " lives left")
def housecat():
      print("There is a housecat behind the door!")
      print("Nothing Happens!") 
      
def andrew ():
      print("Andrew is behind the door.")
      print("CONGRADULATIONS!!!!!!U just married Andrew.")
      print("You have " + str(livesLeft) + " livesleft")

def end_the_game():
        print("Oh no!You are dead.")
        print("Fin.")
def try_again():
    print("Try Again.")
    return int(input())
    
intro()
while livesLeft!=0:
    g=random.randint(1,door)
    a=random.randint(1,door)
    while g==a:
        a=random.randint(1,door)
    x=int(input())
    
    while x!=g and x!=a: 
        housecat()
        x=try_again()
    
    
    
    if x==g:
        livesLeft=livesLeft-1
        gloria()        
      
    if x==a:
        livesLeft=livesLeft+1
        andrew()

    

end_the_game()

      




      
      
      

     
