#merge two python dictionaries
def merge(a,b):
    return(b.update(a))
a={'p':1,'q':2}
b={'r':3,'s':4}
print(merge(a,b))
print(b)

x={'m':1,'n':2,'o':3}
print("Dictionary before performing deleting is",x)
del x['n']
print("Dictionary after performing deleting is",x)

#map two list into a dictionary
Names=['Abi','Ash','Rk']
rollno=['1','2','3']
group=dict(zip(Names,rollno))
print(group)

#length of a set
y={1,2,3,4,5}
print("The length of set is",len(y))

#remove the intersection of 2nd set from the 1st set
sn1={1,2,3,4,5}
sn2={4,5,6,7,8}
sn1.difference_update(sn2)
print("sn1:",sn1)
print("sn2:",sn2)

