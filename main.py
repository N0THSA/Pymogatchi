import random

from colorama import *
from time import *
import threading
import keyboard

def newline(amount):
    for i in range(amount):
        print("")

print(Fore.CYAN + "=====================================")
newline(1)
print("  o  " + "      This is Bob.")
print(" /|\ " + "      Bob is homeless.")
print("  |  " + "      Bob is your pet now.")
print(" / \ " + "      Don't let him die.")
newline(1)
print("=====================================")
input("Press enter to continue...")

def controlQuestion():

    print("Would you like to see the controls?")
    userinput = input("Y/N: ")
    userinput.lower()
    if userinput == "y":
        newline(1)
        print("======[Controls]======")
        print("Figure it out yourself.")
        print("======================")
        input("Press enter to continue...")
    elif userinput == "n":
        newline(1)
    else:
        print("Oops! You didn't enter correct information. Returning...")
        sleep(5)
        controlQuestion()

controlQuestion()

name = "Bob"
hunger = 100
game_over = False
time = 0

def hungerTick():
    global hunger, game_over, name, time
    while hunger > 0:
        sleep(1)
        hunger-=1
    if hunger == 0:
        game_over = True  # set game_over flag to True

def timeTick():
    global hunger, game_over, name, time
    while True:
        sleep(1)
        time+=1

def gameplayLoop(alert):
    global hunger, game_over, name, time
    newline(1000)
    while not game_over:
        sleep(0.2)
        print("  o  " + f"STATS:")
        print(" /|\ " + f"    NAME: {name}")
        print("  |  " + f"    FOOD: {hunger}")
        print(" / \ " + f"    TIME: {time}")
        print("     " + f"")
        print("     " + f"{alert}")
        print("     " + f"")
        print("=====[OPTIONS]=====")
        print("R: REFRESH")
        print("F: FEED")
        print("N: NAME")
        key = keyboard.read_key()
        if key == "r":
            gameplayLoop("")
        elif key == "f":
            hunger = 100
            gameplayLoop(f"Gave {name} some expired ramen!")
        elif key == "n":
            newline(1)
            name = input("What do you name him?: ")
            gameplayLoop(f"You changed his name to {name}!")
        else:
            gameplayLoop("")

    print(f"{name} is dead. You monster.")

    #if keyboard.read_key() == "r":
    #    gameplayLoop()



if __name__ =="__main__":
    t1 = threading.Thread(target=hungerTick)
    t1.start()
    t2 = threading.Thread(target=gameplayLoop(""))
    t2.start()
