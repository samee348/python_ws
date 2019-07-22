'''6. program to accept a number from the user and display the reverse of it'''

num=int(input("enter the number:"))
temp=num
rev = 0
while num!=0:
    rev=rev*10+num%10
    num//=10

print(f"reverse of {temp} is {rev}")
