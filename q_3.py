'''3.Write a program to accept 2 different numbers from the user and print all the prime numbers between these 2 numbers.'''

def is_prime(N):
   if N<2:
      return False
   else:
      for i in range(2,N//2+1):
         if N%i==0:
            return False
   return True

LB=int(input("Enter lower bound:"))
UB=int(input("Enter upper bound:"))
for i in range(LB,UB+1):
   if is_prime(i):
      print(i)