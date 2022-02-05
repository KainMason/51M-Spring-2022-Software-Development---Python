# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 17:44:20 2022

@author: 18122
"""
import random
ans = random.sample(range(1,35),3)


winner1 =("JACKPOT!!! $15000")
winner2 =("Winner!!! $7500")
winner3=("Win!!! $2000")
loser=("Sorry ! Better luck next time")




print("LOTTERY GAME: PLAY 3 numbers 1-35")
a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))
c = int(input("Enter 3rd Number: "))


guess1=[a,b,c]

counter=0
prize=0
while counter<=2:
    if ans[counter] == guess1[0] or ans[counter] == guess1[1]or ans[counter] == guess1[2]:
        counter+=1
        prize+=1
    else:
        counter+=1
 
  
    
    
if prize == 3 and ans==guess1:
    print()
    print("lottery numbers: "+ str(ans))
    print("Your Numbers: "+ str(guess1)) 
    print(winner1)
elif prize == 3 and ans!=guess1:
    print()
    print("lottery numbers: "+ str(ans))
    print("Your Numbers: "+ str(guess1)) 
    print(winner2)
elif prize == 3 and ans==guess1:
    print()
    print("lottery numbers: "+ str(ans))
    print("Your Numbers: "+ str(guess1)) 
    print(winner2)
elif prize == 2 :
    print()
    print("lottery numbers: "+ str(ans))
    print("Your Numbers: "+ str(guess1)) 
    print(winner3)
elif prize <=1:
    print()
    print("lottery numbers: "+ str(ans))
    print("Your Numbers: "+ str(guess1)) 
    print(loser)
        
        












































