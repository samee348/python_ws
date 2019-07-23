lst = []
def add(ele):
    lst.append(ele)
def pop():
    if len(lst)==0:
        print("list empty")
    else:
        ele=lst.pop()
        print(f"element {ele} is removed")
def search(ele):
    if len(lst)==0:
        print("list empty")
    else:
        if ele in lst:
            index=lst.index(ele)
            print(f"element {ele} is found at:{index}")
        else:
            print(f"Given element {ele} is not found")
def display():
    if len(lst)==0:
        print("list empty")
    else:
        for i in lst:
            print(lst)

   



while True:
    print("****1.Add 2.Delete 3.Search 4.Display 5.Exit****")
    ch=int(input("enter the choice:"))
    if ch==1:
        ele=int(input("enter the element to add:"))
        add(ele)
    elif ch==2:
        pop()
    elif ch==3:
        ele=int(input("enter the element to search:"))
        search(ele) 
    elif ch==4:
        display()
    else:
        print("Thank You")
        break   
