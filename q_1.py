'''1. write a program to accept a number and determine whether it is prime or not'''

import math
def is_prime_fun(num):
num=int(input("enter the numer:"))
is_prime=True
if num<2:
    is_prime=False
else:
    for i in range(2,num//2+1):
        if num%i==0:
            is_prime=False
            break
if is_prime:
    print(f"{num} is prime number")
else:
    print(f"{num} is not a prime number")