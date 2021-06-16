#create a list
def createList(r1,r2):
    if(r1==r2):
        return r1
    else:
        res=[]
        while(r1<r2+1):
            res.append(r1)
            r1+=1
        return res

r1=int(input("Enter the starting value of the list"))
r2=int(input("Enter the starting value of the list"))
z=createList(r1,r2)
print(z)

#add items to list
x=int(input("Enter the value to be added in the list"))
z.append(x)
print('New List',z)

#delete item from list
z.remove(z[3])
print("List after removing a number is",z)

#store a largest number in a list
def maxnum(z):
    max=z[0]
    for a in z:
        if a > max:
            max=a
    return max
print("The largest number stored in the list is",maxnum(z))

#store a smallest number in a list
def minnum(z):
    min=z[0]
    for b in z:
        if b<min:
            min=a
    return min
print("The smallest number stored in the list is",minnum(z))


#create tuple
s1=(1,2,3,4,5)
print("Tuple values",s1)

#reverse tuple
def reverse(s1):
    new_tup=s1[::-1]
    return new_tup
print("Reverse tuple is",reverse(s1))

#tuple into list
q = (1,2,3)
print("Tuple values is",q)
y = list(q)
print("Tuple converted into list",y)
