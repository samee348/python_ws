import random as rn 
nums = [i for i in range(1,201)]
lst=list(filter(lambda i:i % 5==0,nums))
print(lst)
