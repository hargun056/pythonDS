# Question 1
t1=(22,10,'hey',10,9.8,'yo','hey',22,10)
print(t1)
t1=set(t1)
t1=tuple(t1)
print("After removing duplicate elements: ",t1)


print()
print("______________________________")
print()
# Question 2
l1=[[1, 2], [3, 4], [5, 6]]
print("Original List: ", l1)
l2=[j for i in l1 for j in i]
print("Flattened list: ", l2)


print()
print("______________________________")
print()
# Question 3
tup=(3, 5, 1, 8, 2)
print("Original Tuple: ", tup)
tup=list(tup)
tup.sort()
print("Min= ",tup[0])
print("Max= ",tup[-1])


print()
print("______________________________")
print()
# Question 4
l1=[(i,i**3) for i in range(1,6)]
print("List : ",l1)