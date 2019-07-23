import random as rn 
lst = []
for i in range(1,101):
    lst.append(rn.randint(1,1000))

new_lst = []
for ele in lst:
    if ele%3==0 and ele%6==0 and ele%9!=0:
        new_lst.append(ele)
print(new_lst)