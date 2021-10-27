import os
from subprocess import call
from time import sleep

import random 


class Board: 
    def build_board(self, player1, player2):
        print("_______________")
        for i in range (0, 3):           
            for j in range(1,4):
                if (j + i * 3) in player1:
                    print("| x |", end="")
                elif (j + i * 3) in player2:
                    print("| o |", end="")
                else:
                    print("|   |", end="")
            print()
            print("|___||___||___|")
class player1(Board):
    def position (self, coordinate1):
        self.coordinate1.append(coordinate1)
        return self.coordinate1
class player2(Board):
    def position (self, coordinate2):
        self.coordinate2.append(coordinate2)
        return self.coordinate2

            
def screen_clear():
    _ = os.system('cls')
def checkwin(player):
    for i in player:
        for num in range(1, 5):
            if i + num in player and i + num * 2 in player:
               return True
    return False
               
    
board = Board()
player1 = []
player2= []
win = False
print("Do you play alone or with your friend?")
numplayer = input("Enter number of player: ")
while win == False:
    position = input("Player 1: ")
  
    while int(position) in player1 or int(position) in player2:
        print("You cannot choose this position")
        position = input("Enter again: ")

    player1.append(int(position))
    screen_clear()
    board.build_board(player1, player2)
    win = checkwin(player1)

    if win == True:
        print("Congratulation player 1")
        break
    if int(numplayer) == 1:
        position = random.randint(1,9)
    else:
        position = input("Player 2: ")

    while int(position) in player1 or int(position) in player2:
        if int(numplayer) == 1:
            position = random.randint(1,9)
        else:
            print("You cannot choose this position")
            position = input("Enter again: ")
    screen_clear()
    player2.append(int(position))
    board.build_board(player1, player2)
    win = checkwin(player2)
    if win == True:
        print("Congratulation player 2")
        break

  
        