# Salary

class devoloper: #perent class
    def a(object, name1, salary1): #child class
        object.name=name1
        object.salary1=salary1
        print("\nName   : ",object.name)
        print("Salary : ",object.salary1)

class Manager:
    def b(object, name2, salary2):
        object.name=name2
        object.salary=salary2
        print("\nName   : ",object.name)
        print("Salary : ",object.salary)
        object.final=object.salary

    def rent(object):
        object.j=object.final*0.08  #from manager (object.final)
        print("Rent   : %0.2f"%object.j)

class Assistant():   #perent class
    def c(object, name3):  #chiled class
        object.name=name3
        object.salary=salary2
        print("\nName   : ",object.name)

    def d(object, salary2,per):
        object.salary=per/100
        object.finalsa=object.salary*salary2
        object.salary3=salary2-object.finalsa
        print("Salary : ",object.salary3)

    def rent(object):
        object.j=object.salary3*.04 #from def d (child) (object.salary3)
        print("Rent   : %0.2f"%object.j)
        

name1=input("Enter Devoloper name:------->: ")
name2=input("Enter Manager name:--------->: ")
name3=input("Enter Assistant nam:-------->: ")

salary1=int(input("Enter selary for Devoloper:->: "))
salary2=int(input("Enter salary for Manager:--->: "))
per=int(input("Percentage for Assistant:------->: "))

call=devoloper()
call.a(name1, salary1)

call=Manager()
call.b(name2, salary2)
call.rent()

call=Assistant()
call.c(name3)
call.d(salary2,per)
call.rent()
