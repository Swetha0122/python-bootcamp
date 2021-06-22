#To add +2to every element in the list

My_List = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for n in My_List[1::2]:
    print (n)
    
# To print the 5,4,3.. pattern
for i in range(1, 6):
    for j in range(5, i-1,-1):
        print(j, end="")
    print()
    
#Python program to generate Fibonacci series until 'n' value
    
n = int(input("Enter the value of 'n': "))
a = 0
b = 1
sum = 0
count = 1
print("Fibonacci Series: ", end = " ")
while(count <= n):
  print(sum, end = " ")
  count += 1
  a = b
  b = sum
  sum = a + b
  
#To generate armstrong number
  
for num in range(1000):
  temp=num
  sum=0
  while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10

  if sum==num:
    print (num)

#To print the multiplication of 9
n = int(9)
print("The muliplication table of 9 :")

# use for loop to iterate 10 times
for i in range(1,11):
   
   print(n,'x',i,'=',n*i)

#To check the program positive or negative
   
num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")
   
# To convert days into ages

print("Enter the days:")

d, y, w = int(input()), None, None

y = (int)(d / 365)
w = (int)((d % 365) / 7)
d = (int)(d - ((y * 365) + (w)))
print(y, " Year, ", w, " Weeks, and ", d, " Days\n")

#To solve trignomertic function using math function
import math
x = int(input("Enter the number:"))
print( "sin(x)=",math.sin(x));
print("cos(x)=",math.cos(x));
print("tan(x)=",math.tan(x));
a= math.sin(x)
b= math.cos(x)
c= math.tan(x)
d= (a+b)/c
print("(sin(x)+cos(x))/tan(x)=",d)

# To create calculator
print("Calculator")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")

ch=int(input("Enter the Choice(1-4): "))

if ch==1:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a+b
    print("Sum = ",c)
elif ch==2:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a-b
    print("Difference = ",c)
elif  ch==3:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a*b
    print("Product = ",c)
elif ch==4:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a/b
    print("Quotient = ",c)
else:
    print("Invalid Choice ")
