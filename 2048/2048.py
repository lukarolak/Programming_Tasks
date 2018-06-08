'''
2048
Implement a 2D sliding block puzzle game where blocks with numbers are combined to add their values.
The rules are that on each turn the player must choose a direction (up, down, left or right) and all tiles move as far as possible in that direction, some more than others. Two adjacent tiles (in that direction only) with matching numbers combine into one bearing the sum of those numbers. A move is valid when at least one tile can be moved, if only by combination. A new tile with the value of 2 is spawned at the end of each turn at a randomly chosen empty square, if there is one. To win the player must create a tile with the number 2048. The player loses if no valid moves are possible.
The name comes from the popular open-source implementation of this game mechanic, 2048.
Requirements:
"Non-greedy" movement. The tiles that were created by combining other tiles should not be combined again during the same turn (move). That is to say that moving the tile row of

https://rosettacode.org/wiki/2048
'''
import time 
import random
import msvcrt
def GameLogic(imin,imax,jmin,jmax,astep,bstep,alim,blim):
    for i in range(imin,imax):
        for j in range(jmin,jmax):
            if(Board[i][j] != 0):
                a,b = i,j
                while(True):
                    if(Board[a+astep][b+bstep] == 0):
                        Board[a+astep][b+bstep] = Board[a][b]
                        Board[a][b] = 0
                        b = b+bstep
                        a = a+astep
                    else: 
                        if(Board[a+astep][b+bstep] == Board[a][b]):
                            Board[a+astep][b+bstep] = Board[a+astep][b+bstep]*2
                            Board[a][b] = 0
                        else:
                            break
                    if(blim != -1):
                        if(b == blim):
                            break
                    else:
                        if(a == alim):
                            break
def PopulatePosition():
    Positions = [0,1,2,3]
    for i in range(4):
        Position = random.choice(Positions)
        Positions.pop(Positions.index(Position))
        if 0 in Board[Position]:
            positions = [0,1,2,3]
            for j in range(4):
                position = random.choice(positions)
                positions.pop(positions.index(position))
                if Board[Position][position] == 0:
                    Board[Position][position] = 2
                    return 0
    return 1

Board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
while(True):  
    if(PopulatePosition()):
        print("GameOver")
        break
    else:
        print(Board[0])
        print(Board[1])
        print(Board[2])
        print(Board[3])
        print(" ")
        Key = msvcrt.getch()
        if Key == b's':
            GameLogic(0,3,0,4,1,0,3,-1)
        if Key == b'w':
            GameLogic(1,4,0,4,-1,0,0,-1)
        if Key == b'a':
            GameLogic(0,4,1,4,0,-1,-1,0)
        if Key == b'd':
            GameLogic(0,4,0,3,0,1,-1,3)
        print(Board[0])
        print(Board[1])
        print(Board[2])
        print(Board[3])
        print(" ")
