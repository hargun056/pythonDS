print("*******************************")
print("/tQuestion 1")
print("*******************************")
num=int(input("Enter a number: "))
if num==1:
    print("January")
elif num==2:
    print("February")
elif num==3:
    print("March")
elif num==4:
    print("April")
elif num==5:
    print("May")
elif num==6:
    print("June")
elif num==7:
    print("July")
elif num==8:
    print("August")
elif num==9:
    print("September")
elif num==10:
    print("October")
elif num==11:
    print("November")
elif num==12:
    print("December")
else:
    print("Invalid")


print("*******************************")
print("/tQuestion 2")
print("*******************************")
#WAP Ask user to input 2 number,
#tell the followings
#1. Both number are equal or not
#2. Which is Bigger in both
#3. Either First NUmber is smaller or equal to Second Number
#4. Print your first name 5 times is first number is
#   greather than second and print your surname 3 times if 1st no
#   is less than second



a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
fname=input("Enter your first name: ")
lname=input("Enter your last name: ")
name=fname+ " "+lname
print("a= ",a)
print("b= ",b)
print("name= ",name)
if a>b:
    print(a, " is greater than ",a)
    for i in range(5):
        print(fname)
elif b>a:
    print(b," is greater than ",a)
    for i in range(3):
        print(lname)
else:
    print(a," is equal to ",b)



print("*******************************")
print("/tQuestion 3")
print("*******************************")
str1=input("Enter first string: ")
str2=input("Enter second string: ")
if str1==str2:
    print("String 1 is equal to string 2")
else: 
    print("Strings are not equal")
if str1 is str2:
    print("String 1 and String 2 are equal(ID)")
else:
    print("Strings are not equal(ID)")



print("*******************************")
print("/tQuestion 4")
print("*******************************")
str1=input("Enter first string: ")
str2=input("Enter second string: ")
# Strings can't be converted into numbers
if str1 is str2:
    print("String 1 and String 2 are equal")
else:
    print("Strings are not equal(ID)")


print("*******************************")
print("/tQuestion 5")
print("*******************************")
num=int(input("Enter a number: "))
sum=0
for i in range(num+1):
    sum=sum+i
print("Sum from 0 to ",num,"= ",sum)


print("*******************************")
print("/tQuestion 6")
print("*******************************")
num=int(input("Enter a number: "))
print("Even numbers are ")
for i in range(num+1):
    if i%2==0:
        print(i,end=" ")


print("*******************************")
print("/tQuestion 7")
print("*******************************")
num=int(input("Enter a number: "))
op=input("Enter the operator (+ or -): ")
if op=='+':
    for i in range(num):
        print(i,end=" ")
elif op=="-":
    for i in range(num,0,-1):
        print(i,end=" ")
else:
    print("Wrong operator")


print("*******************************")
print("/tQuestion 8")
print("*******************************") 
num=int(input("Enter a number: "))
for i in range(1,11):
    print(num," x ",i," = ",num*i)


print("*******************************")
print("/tQuestion 9")
print("*******************************")
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


print("*******************************")
print("/tQuestion 10")
print("*******************************")
n=int(input("Enter a number: "))
print("Squares of ",n," natural numbers: ")
for i in range(1,n+1):
    print(i*i,end=" ")