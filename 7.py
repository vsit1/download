#  implement membership and identity operators | in or not in.:
list1=[]
print("Enter 5 numbers")
for i in range(0,5):
    v=int(input())
    list1.append(v)
list2=[]
print("Enter 5 numbers")
for i in range(0,5):
    v=int(input())
    list2.append(v)
flag=0
for i in list1:
    if i in list2:
        flag=1
if(flag==1):
    print("The lists overlap")
else:
    print("Lists do not overlap")
# Not in operator in python:
list1=[]
c=int(input("Enter the number of elements that you want to insert in List1: "))
for i in range(0,c):
    ele=int(input("Enter the element : "))
    list1.append(ele)
a=int(input("Enter the number that you want to find in List1: "))
if a not in list1:
    print("The list does not contain: ",a)
else:
    print("The list contains: ",a)
# Implement Membership and Identity Operator is.
details=[]
name=input("Enter your name: ")
details.append(name)
age=float(input("Enter your exact age: "))
details.append(age)
roll_no=int(input("Enter your Roll NO.: "))
details.append(roll_no)
for i in details:
    print(i)
    print("Int= ",type(i) is int)
    print("Float= ",type(i) is float)
    print("String= ",type(i) is str)
    print()
# Implement Membership and Identity Operator is not.
details=[]
name=input("Enter your name: ")
details.append(name)
age=float(input("Enter your exact age: "))
details.append(age)
roll_no=int(input("Enter your Rol NO.: "))
details.append(roll_no)
for i in details:
    print(i)
    print("Not Int= ",type(i) is not int)
    print("Not Float= ",type(i) is not float)
    print("Not String= ",type(i) is not str)
    print()
