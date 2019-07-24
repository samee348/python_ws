from employee import Employee

lst_emp = []

def load_emp():
    with open("empdata.txt") as f:
        fdata = f.readlines()
        for data in fdata:
            edata=data.strip("\n").split(",")
            empno = int(edata[0])
            ename = edata[1]
            qualification = edata[2]
            salary = int(edata[3])
            dept_name = edata[4]
            emp = Employee(empno,ename,qualification,salary,dept_name)
            lst_emp.append(emp)
    print(f"total employee count :{len(lst_emp)}")

def showDeptName():
    dept_name=set(map(lambda emp:emp.dept_name,lst_emp))
    for name in dept_name:
        print(name)

def showAllQualifications():
    qualifications = set(map(lambda emp:emp.qualification,lst_emp))
    for qualification in qualifications:
        print(qualification)

def maxSalaryEmp():
     max_salary = max(list(map(lambda x:x.salary,lst_emp)))
     lst = list(filter(lambda x:x.salary==max_salary,lst_emp))
     for emp in lst:
         emp.show_info()



load_emp()
print("All department names:")
showDeptName()
print("All qualifications:")
showAllQualifications()
maxSalaryEmp()