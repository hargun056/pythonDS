# #Question 1
# str1=input("Enter a String: ")
# l=len(str1)
# if l<2:
#     print("Invalid String")
# else:
#     str2=str1[:2]+str1[l-2:l]
#     print("New String- ",str2)

print()
print("______________________________")
print()

# Question 2
# str1=input("Enter First String- ")
# str2=input("Enter Second String- ")
# a=str1[:1]
# b=str2[:1]
# str1=str1.replace(a,b)
# str2=str2.replace(b,a)
# print("New String= ",str1," ",str2)


print()
print("______________________________")
print()

# Question 3
# str1=input("Enter a string: ")
# l=len(str1)
# if l<3:
#     print("String- ",str1)
# elif str1.endswith("ing"):
#     print("New String- ",str1+"ly")
# else:
#     print("New String- ",str1+"ing")

print()
print("______________________________")
print()

# Question 4
str1=input("Enter a String: ")
if len(str1)==0:
    print("String is empty")
else:
    a=int(input("Enter the index: "))
    if a>len(str1):
        print("Entered index is greater than the length of string")
    else:
        print("String= ",str1)
        print("New String= ",str1[:a]+str1[a+1:])