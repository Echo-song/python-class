import random
gloria=random.randint(1,9)
andrew=random.randint(1,9)
while gloria==andrew:
    andrew=random.randint(1,9)
g=gloria
a=andrew
print("Welsome to the game Andrew, Gloria or housecats.")
print("U, the great Elizabeth Li is infront of 9 great doors.")
print("Behind one of the doors is Gloria Zhu.")
print("Behind another door is Andrew")
print("There are housevats behind all other doors.")
print("If there is a person behind the door You will marry he/she")
print("Which door #1-9 will you chose?")
x=int(input())

def gloria ():
      print("Gloria is behind the door!")
      print("CONGRADULATIONS!!!U just married Gloria!")
def housecat():
      print("There is a housecat behind the door!")
      print("Nothing Happens!")
      print("Try Again.")
def andrew ():
      print("Andrew is behind the door.")
      print("CONGRADULATIONS!!!!!!U just married Andrew.")


while x!=g and x!=a:
      housecat()
      x=int(input())
if x==g:
    gloria()
      
if x==a:
    andrew()
      




      
      
      

     
