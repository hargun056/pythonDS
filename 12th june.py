print("*******************************")
print("/tQuestion 1")
print("*******************************")
name=input("Enter student's name: ")
std=input("Enter student's class: ")
section=input("Enter student's section: ")
math=int(input("Enter marks in Maths: "))
coa=int(input("Enter marks in COA: "))
daa=int(input("Enter marks in DAA: "))
uhv=int(input("Enter marks in UHV: "))
os=int(input("Enter marks in OS: "))
total=math+coa+os+uhv+daa
av=total/5
print("-------------------------------------------")
print("\t\tRESULT")
print("-------------------------------------------")
print("Name- ",name)
print("Class- ",std)
print("Section- ",section)
print("Percentage scored- ",av,"%")


print("*******************************")
print("/tQuestion 2")
print("*******************************")
a=int(input("Enter a number "))
b=int(input("Enter a number "))
c=int(input("Enter a number "))
sum=a+b+c
print("Sum ",sum)


print("*******************************")
print("/tQuestion 3")
print("*******************************")
a=int(input("Enter a number "))
print("Square= ",a*a)


print("*******************************")
print("/tQuestion 4")
print("*******************************")
temp=input("Enter the temperature in Celsius- ")
tempc=float(temp)
tempf=(tempc*(9/5))+32
print("Temperature in Celsius= ",tempc)
print("Temperature in Fahrenheit= ",tempf)


print("*******************************")
print("/tQuestion 5")
print("*******************************")
a=int(input("Enter a number  "))
b=int(input("Enter a number  "))
quotient=a//b
remainder=a%b
print("Quotient= ",quotient)
print("Remainder= ",remainder)