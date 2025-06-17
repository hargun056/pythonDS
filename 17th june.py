# List Comprehension
# Question 1
# Find all of the words in a string that are less than 4 letters
list1=["hello","Mohali","Hey","Here","Chandigarh","Hola"]
result=[i for i in list1 if len(i)<=4]
print("Strings with less than four letters: ",result)


print()
print("______________________________")
print()
# Question 2
list1=[i for i in range(20)]
print(list1)
list2=["even" if i%2==0 else "odd" for i in list1]
print("New list: ",list2)


print()
print("______________________________")
print()
# Question 3
l1=[i for i in range(1,1000) if i%7==0]
print("Numbers divisible by 7: ",l1)


print()
print("______________________________")
print()
# Question 4
str1="Hey! How are you? I hope you are doing great. "
count=0
for i in str1:
    if i==" ":
        count+=1
print("Total number of spaces: ",count)


print()
print("______________________________")
print()
# Question 5
list_a=[1,2,3,4]
list_b=[2,3,4,5]
l=[i for i in list_a for j in list_b if i==j] 
print("New list: ",l)