'''dice application'''
import random as rn 
num=rn.randint(1,6)
count=0
while True:
    inp_num=int(input("enter the number:"))
    if inp_num==num:
        count+=1
        print(f"you guessed number in {count} attempts ")
    elif inp_num<num:
        print(f"less number")
        count+=2
    else:
        print(f"greater number")
        count+=3
    if count==3:
        print(f"better luck next time")
        
