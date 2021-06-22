#merge two dictionary
def merge(a,b):
    return(b.update(a))
a={'p':1,'q':2}
b={'r':3,'s':4}
merge(a,b)
print(b)

#sort values from descending to ascending in a list
a=[1,3,6,2,5,1,7,4,9,5]
print("The list is",a)
a.sort(reverse=True)
print("Descending order of a list",a)
a.sort()
print("Ascending order of a list",a)
b=set(a)
print(b)

p={'a':[1,2,3],'b':[4,5,6]}
res=dict()
for key in sorted(p):
    res[key]=sorted(p[key])
print("The sorted dictionary is ",str(res))
#Write a Python program to get a string from a given string (user input) and change the first occurrence of the word to a user specified input.

def change_char(str1):
    char = str1[5]
    str1 = str1.replace(char, '@')
    str1 = char + str1[1:]
   
    return str1
print(change_char("Swetha"))

#Write a Python program to get a string from a given string where all occurrence of its frist char have been changed to capital letter

def function():
    user=input("Enter the string : ")
    return user.capitalize()

function()

#Write a Python program to find the repeated items of a list

a =[1,2,3,3,3,4,4,5,6,7,7,5,8,9,10]
print(a)
b = a.count(3)
print(b)

#Write a Python program to check the sum of three element and divided by a value which is given as an input by the user

A=int(input("Enter a value : "))
B=int(input("Enter a value : "))
C=int(input("Enter a value : "))
sum = A+B+C
print(sum)
div=int(input("Enter a number to divide the  sum "))
if (sum% div)==0:
    print("The input value divide the sum value ")
else :
    print("The  input value does not divide the sum value ")

#Write a Python program to find the Mean,median,mode among three given numbers

x = input("Enter the first number ")
y = input("Enter the second number ")
z = input("Enter the third number ")
print("the Median of the above three numbers")
if y < x and x < z:
    print(x)
elif z < x and x < y:
    print(x)
elif z < y and y < x:
    print(y)
elif x < y and y < z:
    print(y)
elif y < z and z < x:
    print(z)
elif x < z and z < y:
    print(z)

#Write a Python program to swap cases of a given string

a="Swetha"
b="Bala"
r=a
a=b
b=r
print(a,b)

dec = 221

print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")

