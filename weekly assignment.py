# Question 1

for i in range(1,51):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0:
        print("Fizz")
    else:
        print(i)


print()
print("______________________________")
print()

# Question 2

print("Prime numbers from 1 to 100")
for num in range(1,101):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)

    
print()
print("______________________________")
print()

# Question 3

num=float(input("Enter the score between 0 and 100: "))
if num<=100 and num>90:
    print("Grade A")
elif num<=90 and num>80:
    print("Grade B")
elif num<=80 and num>70:
    print("Grade C")
elif num<=70 and num>60:
    print("Grade D")
elif num<=60:
    print("Fail")
else:
    print("Invalid score")


print()
print("______________________________")
print()

# Question 4

num=int(input("Enter a number: "))
for i in range(1,11):
    print(num,'x',i,'=',num*i)


print()
print("______________________________")
print()

# Question 5

li=[]
for i in range(1,21):
    if i%2==0:
        li.append(i**2)
print(li)


print()
print("______________________________")
print()

# Question 6

year=int(input("Enter a year: "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(year,"is a leap year")
        else:
            print(year,"is not a leap year")
    else:
        print(year,' is a leap year')
else:
    print(year,' is not a leap year')


print()
print("______________________________")
print()

# Question 7

s1=float(input("Enter side 1 of triangle: "))
s2=float(input("Enter side 2 of triangle: "))
s3=float(input("Enter side 3 of triangle: "))
if s1+s3>s2 or s1+s2>s3 or s2+s3>s1:
    if s1==s2==s3:
        print("It is an equilateral triangle")
    elif s1==s2 or s2==s3 or s3==s1:
        print("It is an isosceles triangle")
    elif s1**2==s2**2 + s3**2 or s2**2==s1**2 + s3**2 or s3**2==s1**2 + s2**2:
        print("It is a right angled triangle")
    else:
        print("It is a scalene triangle")
else:
    print("It is not a triangle")


print()
print("______________________________")
print()

# Question 8

num=int(input("Enter an integer number: "))
if num>0:
    print("It is a positive number")
elif num<0:
    print("It is a negative number")
else:
    print("It is zero")


print()
print("______________________________")
print()

# Question 9

pwd=input("Enter the password: (At least 8 characters long \nContains both uppercase and lowercase characters \nContains at least one digit \nContains at least one special character): ")
if len(pwd)>=8:
    for i in pwd:
        if i.isupper():
            up=True
        elif i.islower():
            lo=True
        elif i.isdigit():
            di=True
        elif i in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/\\`~":
            sp=True
    if up and lo and di and sp:
        print("Password is strong")
    else:
        print("Password is not strong")
else:
    print("Length is less than 8.")
    print("Password is weak")


print()
print("______________________________")
print()

# Question 10

weight=float(input("Enter weight in kilogram: "))
height=float(input("Enter height in metre: "))
bmi=weight/(height**2)
print("BMI(Body Mass Index)= ",bmi)

if bmi<18.5:
    print("Underweight")
elif bmi>=18.5 and bmi<24.9:
    print("Normal weight")
elif bmi>=25 and bmi<29.9:
    print("Overweight")
elif bmi>=30:
    print("Obesity")


print()
print("______________________________")
print()

# Question 11

num=int(input("Enter the number for day: "))
if num==1:
    print("Monday")
elif num==2:
    print("Tuesday")
elif num==3:
    print("Wednesday")
elif num==4:
    print("Thursday")
elif num==5:
    print("Friday")
elif num==6:
    print("Saturday")
elif num==7:
    print("Sunday")
else:
    print("Invalid day")


print()
print("______________________________")
print()

# Question 12

price=float(input("Enter the price of the product: "))
if price>=1000:
    print("Price: ",price)
    print("Discount applied= 10%")
    dis=price-(price/10)
    print("Discounted Price: ",dis)
elif price<1000 and price>=500:
    print("Price: ",price)
    print("Discount applied= 5%")
    dis=price-(price/20)
    print("Discounted Price: ",dis)
else:
    print("Price: ",price)
    print("No discount")


print()
print("______________________________")
print()

# Question 13

num=int(input("Enter a number: "))
sum=0
for i in range(1,num+1):
    sum+=i
print("Sum of first ",num," natural numbers is: ",sum)


print()
print("______________________________")
print()

# Question 14

employee_details={101:{'name':"Klaus","dept":"Technology",'salary':100000},
                  102:{'name':'Elijah','dept':'Pharmacy','salary':70000},
                  103:{'name':"Rebecca","dept":"Technology",'salary':90000},
                  104:{'name':"Kol","dept":"Finances",'salary':50000},
                  105:{'name':"Hope","dept":"Accounts",'salary':45000}}
list1=[]
for i in employee_details:
    if employee_details[i]['salary']>50000:
        list1.append(employee_details[i]['name'])
print("Employees with salary greater than 50000: ",list1)


print()
print("______________________________")
print()

# Question 15

str1=input("Enter a string: ")
count=0
for ch in str1:
    if ch=='a'or ch=='A' or ch=='e' or ch=='E' or ch=='i' or ch=='I' or ch=='o' or ch=='O' or ch=='u' or ch=='U':
        count+=1
print("Number of vowels in the given string= ",count)


print()
print("______________________________")
print()

# Question 16

num=int(input("Enter a number: "))
sum=0
while num>0:
    num1=num%10
    num=num//10
    sum+=num1
print("Sum of digits of the given number is: ",sum)


print()
print("______________________________")
print()

# Question 17

n=int(input("Enter n: "))
for i in range(n+1):
    for j in range(i):
        print("*",end="")
    print()


print()
print("______________________________")
print()

# Question 18

import random
ans=random.randint(1,100)
guess = int(input("guess the number: "))

while(guess!=ans):
    if guess<ans:
        print("too low")
        print("guess higher")
    else:
        print("too high")
        print("guess lower")
    guess=int(input("guess the number: "))

print("CORRECT GUESS! YOU WON")


print()
print("______________________________")
print()

# Question 19

num=int(input("Enter a number: "))
print("Even numbers upto ",num," :")
for i in range(1,num+1):
    if i%2==0:
        print(i,end=" ")


print()
print("______________________________")
print()

# Question 20

list1=[5,10,25,22,12,25,10,5,25,50]
for i in list1:
    if i==25:
        ele=True
        break
    else:
        ele=False
if ele:
    print("25 is present in the list")
else:
    print("25 is not present in the list")

l=len(list1)
print("Length of the list is ",l)

count=0
for i in list1:
    if i==25:
        count+=1
print("Total occurence of 25 is ",count)

print("Traversing elements of list........")
for i in list1:
    print(i,end=" ")
print()
print("Even numbers in the list......")
for i in list1:
    if i%2==0:
        print(i,end=" ")


print()
print("______________________________")
print()

# Question 21

str1=input("Enter a string of min 10 words and max 19 words:")
words=str1.split(" ")
if len(words)<=19 or len(words)>=10:
    print("String: ",str1)
    print("Length of string: ",len(str1))
    print("Number of words: ",len(words))
    newstr=str1.lower()
    newstr=newstr.replace(' ','')
    if newstr==newstr[::-1]:
        print("String is a palindrome")
    else:
        print("String is not a palindrome")

    mid=len(words)//2
    print("Middle word of the string is: ",words[mid])

    print("Second last word= ",words[-2])
else:
    if len(words)>19:
        print("String is too long")
    elif len(words)<10:
        print("String is too short")



print()
print("______________________________")
print()

# Question 22

print("Welcome to Calci")
print("1.Power \n2.Sum \n3.Sub \n4.Multiple")
choice=int(input("Enter your choice: "))
if choice==1:
    num1=float(input("Enter first number for power: "))
    num2=float(input("Enter second number for power: "))
    print("Result of power is: ",num1**num2)
elif choice==2:
    num1=float(input("Enter first number for sum: "))
    num2=float(input("Enter second number for sum: "))
    print("Result of sum is: ",num1+num2)
elif choice==3:
    num1=float(input("Enter first number for sub: "))
    num2=float(input("Enter second number for sub: "))
    print("Result of sub is: ",num1-num2)
elif choice==4:
    num1=float(input("Enter first number for multiple: "))
    num2=float(input("Enter second number for multiple: "))
    print("Result of multiple is: ",num1*num2)
else:
    print("Invalid choice")


print()
print("______________________________")
print()

# Question 23

list1= ['abc', 'xyz', 'aba', '1221']
count=0
for i in list1:
    if len(i)>=2 and i[0]==i[-1]:
        count+=1
print("Count= ",count)
