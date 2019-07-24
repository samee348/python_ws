from employee import Employee

lst_emp = []

def load_emp():
    with open("empdata.txt") as f:
        fdata = f.readlines()
        for data in fdata:
            print(data)