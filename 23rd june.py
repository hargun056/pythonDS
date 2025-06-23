# # Question 1
# print("----------------------------------------")
# print("\t Welcome to CodeRail")
# print("----------------------------------------")
# name=input("Enter your name: ")
# age=int(input("Enter your age: "))
# print("Choose a class: ")
# print("1. First Class- Rs.1500 \n2. Second Class- Rs.1000 \n3. Sleeper Class- Rs.500")
# choice=int(input("Choice-  "))
# if choice==1:
#     clss="First Class"
#     price=1500
# elif choice==2:
#     clss="Second Class"
#     price=1000
# elif choice==3:
#     clss="Sleeper Class"
#     price=500
# else:
#     print("Invalid choice")
#     exit()


# if age<=5:
#     print("Ticket is free")
#     price=0
# elif age>60:
#     print("20% discount")
#     price=price-(price/5)
# print("Do you want to add a meal(Y/N): ")
# meal=input("Enter your choice: ")
# if meal=='y' or meal=='Y':
#     price=price+200
#     print("Rs 200 extra")
#     m='Yes'
# elif meal=='n' or meal=='N':
#     print("No extra charge")
#     m='No'
# else:
#     print("Invalid choice")
#     m='No'


# print()
# print("----------------------------------------")
# print("\t Ticket Summary")
# print("----------------------------------------")
# print("Passenger Name- ",name)
# print("Age- ",age)
# print("Class- ",clss)
# print("Meal added- ",m)
# print("Final Price- ",price)
# print("Enjoy your journey!🎉")


# print()
# print("______________________________")
# print()

#Question 2

print("-------------------------------")
print("    Welcome to Burger King")
print("-------------------------------")
print()
print("\t     MENU")
print("-------------------------------")
print("\t Item            \tPrice(Rs)")
print("\t1.Whopper Burger \tRs.150")
print("\t2.Crispy Veg     \tRs.100")
print("\t3.Chicken Wings  \tRs.120")
choice=int(input("Enter the item number(1/2/3): "))
print()
if choice==1:
    price=150
elif choice==2:
    price=100
elif choice==3:
    price=120
else:
    print("Invalid choice")
    exit()

qt=int(input("Enter quantity: "))
price=qt*price
print()

coup=input("Do you have coupon code?(yes/no): ")
print()
if coup.lower()=="yes":
    code=input("Enter your coupon code: ")
    print("Applying coupon......")
    if code=='KING50':
        print("Original Price- ",price)
        print("Discount applied: 50%")
        price=price-(price*0.5)
    elif code=='BK20':
        print("Original Price- ",price)
        print("Discount applied: 20%")
        price=price-(price*0.2)
    else:
        print("Invalid coupon code")
        print("No coupon applied")

print("Final price: ",price)
print("Thank you for ordering at Burger King!🍟🍔")
        


