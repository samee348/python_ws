name = input("enter your name:")
lst=['a','e','i','o','u']
print(len(list(filter(lambda x:x in lst, name))))