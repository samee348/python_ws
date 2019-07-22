'''2.	Write a program to accept a number “n” from the user; then display the sum of the following series:
1+ 1/2 + 1/3 + ……+ 1/n'''

num=int(input("Enter a number:"))
sum=0
if num>0:
   for i in range(1,num+1):
      fact=1
      for j in range(1,i+1):
         fact*=j
      sum+=1/fact
print(f"the result is {sum}")
  


