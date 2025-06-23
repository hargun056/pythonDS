# Dictionary 
# Question 1
num=int(input("Enter the number of items: "))
dict={}
for i in range(num):
    key=input("Enter the key: ")
    value=input("Enter the value: ")
    dict[key]=value
print("Dictionary: ",dict)


print()
print("______________________________")
print()


# Question 2
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


# Question 3
import random
ans=random.randint(1,100)
guess = int(input("guess the number: "))

while(guess!=ans):
    if guess<ans:
        print("guess higher")
    else:
        print("guess lower")
    guess=int(input("guess the number: "))

print("CORRECT GUESS! YOU WON")


print()
print("______________________________")
print()


# Question 4
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


# Question 5
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


# Question 6
li=[20,30,40,[57,66,30,[70,80],"Hello"],50,True]
li[3][3].insert(1,76)
print("List after inserting 76: ",li)
li[3].insert(1,88)
print("List after inserting 88: ",li)

print("Letter H: ",li[3][4][0])


print()
print("______________________________")
print()


# Question 7
print("----------------------------------------")
print("\tWelcome to Trip Planner")
print("----------------------------------------")

budget=int(input("Enter your budget (5000-10000, 10000-20000, 20000-30000, 30000-40000): ")) 
choice=''
if budget>=5000 and budget<10000:
    print("Countries Under 10000: ")
    print("\tUAE")
    print("\tIndonesia")
    print("\tSri Lanka")
    print("\tNepal")
    print("\tCyprus")

    print("----------------------------------------")
    choice=input("Enter your choice of country: ")
    print("You have chosen to visit ",choice)

    place={"UAE": ["Dubai", "Burj Khalifa", "Sheikh Zayed Grand Mosque"],
    "Indonesia": ["Bali", "Jakarta", "Borobudur Temple"],
    "Sri Lanka": ["Kandy", "Sigiriya Rock", "Colombo"],
    "Nepal": ["Kathmandu", "Mount Everest", "Pashupatinath Temple"],
    "Cyprus": ["Nicosia", "Aphrodite's Rock", "Limassol"]}

elif budget>=10000 and budget<20000:
    print("Countries Under 20000: ")
    print("\tTurkey")
    print("\tMalaysia")
    print("\tNew Zealand")
    print("\tSouth Africa")
    print("\tBulgaria")

    print("----------------------------------------")
    choice=input("Enter your choice of country: ")
    print("You have chosen to visit ",choice)

    place={"Turkey": ["Istanbul", "Cappadocia", "Hagia Sophia"],
    "Malaysia": ["Kuala Lumpur", "Petronas Towers", "Langkawi"],
    "New Zealand": ["Queenstown", "Hobbiton", "Milford Sound"],
    "South Africa": ["Cape Town", "Table Mountain", "Kruger National Park"],
    "Bulgaria": ["Sofia", "Rila Monastery", "Plovdiv"]}


elif budget>=20000 and budget<30000:
    print("Countries Under 30000: ")
    print("\tAustralia")
    print("\tUnited Kingdom")
    print("\tCanada")
    print("\tAustria")
    print("\tIndia")

    print("----------------------------------------")
    choice=input("Enter your choice of country: ")
    print("You have chosen to visit ",choice)

    place={"Australia": ["Sydney", "Great Barrier Reef", "Melbourne"],
    "United Kingdom": ["London", "Stonehenge", "Big Ben"],
    "Canada": ["Toronto", "Niagara Falls", "Vancouver"],
    "Austria": ["Vienna", "Hallstatt", "Schönbrunn Palace"],
    "India": ["Taj Mahal", "Kashmir", "Golden Temple"]}

elif budget>=30000 and budget<40000:
    print("Countries Under 40000: ")
    print("\tUnited States")
    print("\tGermany")
    print("\tFrance")
    print("\tItaly")
    print("\tSpain")

    print("----------------------------------------")
    choice=input("Enter your choice of country: ")
    print("You have chosen to visit ",choice)

    place={"United States": ["New York", "Statue of Liberty", "Grand Canyon"],
    "Germany": ["Berlin", "Brandenburg Gate", "Neuschwanstein Castle"],
    "France": ["Paris", "Eiffel Tower", "Louvre Museum"],
    "Italy": ["Rome", "Colosseum", "Venice"],
    "Spain": ["Barcelona", "Sagrada Familia", "Madrid"]
    }
else:
    print("Invalid Budget")
    place={}
if choice in place:
    print("Top Three Destinations in ",choice)
    for i in place[choice]:
        print("\t#",i)
else:
    print("Invalid Choice")
