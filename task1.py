# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
def getTheGameData():
    f = open('game.txt', 'r')
    c = f.read()
    c=c.split(' ')
    f.close()
    return c
def updateGameFile(win,lose):
    
    f = open('game.txt', 'w')
    state= ""
    state+=(str(win)+" "+str(lose))
    f.write(state)
    f.close()
    

playing =1
while playing:
    number = random.randrange(1, 100, 1)
    print(number)
    lives=10
    moves=[]

    c = getTheGameData()
    print("the number of games = ",(int(c[0])+int(c[1]))," you win ",c[0]," and lose ",c[1]," times")
    while lives:
        move=input("Guss the number ")
        move=int(move)
        if ((move>100) | (move<0)):
            print( "Please inter a valid number")
            pass # pass: do nothing keyword, continue, break
        elif move in moves:
                
            print( "Please inter a new number")
            pass
        else:
            if move==number:
            # increase winning number in file
                print("you win")
                
                c = getTheGameData()
                win=int(c[0])
                win+=1;
                updateGameFile(win,c[1])
            # start new game
                moves=[]
                number = random.randrange(1, 100, 1)
                print ('new number ',number)
            elif move>number:
                print("tne number is smaller ");
                moves.append(move)
                lives-=1;
            else:
                print("tne number is greater ");
                moves.append(move)
                lives -=1;
    c = getTheGameData()
    lose=int(c[1])
    lose+=1;
    updateGameFile(c[0],lose)
    playing=(input("do you want to continue ?y/n?  ")=='y')

