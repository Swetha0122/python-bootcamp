#importing library
from tkinter import *
from tkinter import ttk

Rainbow = Tk()
#Declaring Rainbow Title
Rainbow.title("Registration Screen")
#Declaring Rainbow size
Rainbow.geometry('300x300')
#Declaring Rainbow Color
Rainbow.configure(background = "light blue");
#below four fields are declared
Firstname = Label(Rainbow ,text = "First Name").grid(row = 0,column = 0)
LastName = Label(Rainbow ,text = "Last Name").grid(row = 1,column = 0)
Email = Label(Rainbow,text = "Email Id").grid(row = 2,column = 0)
AadharNumber = Label(Rainbow,text="Aadhar Number").grid(row=3,column=0)
Mobile = Label(Rainbow,text = "Contact Number").grid(row = 4,column = 0)
Language = Label(Rainbow,text="Language").grid(row =5,column = 0)
Address =  Label(Rainbow,text="Address").grid(row =6,column = 0)
Pincode = Label(Rainbow,text="Pincode").grid(row =6,column = 0)

Firstname1 = Entry(Rainbow).grid(row = 0,column = 1)
Lastname1 = Entry(Rainbow).grid(row = 1,column = 1)
Email1 = Entry(Rainbow).grid(row = 2,column = 1)
AadharNumber1 = Entry(Rainbow).grid(row = 3,column = 1)
Mobile1 = Entry(Rainbow).grid(row = 4,column = 1)
Language1 = Entry(Rainbow).grid(row = 5,column = 1)
Address1 = Entry(Rainbow).grid(row = 6,column = 1)
Pincode = Entry(Rainbow).grid(row = 7,column = 1)

#function declaration
def clicked():
res = "Welcome to " + txt.get()
lbl.configure(text= res)
btn = ttk.Button(window ,text="Submit").grid(row=4,column=0)
window.mainloop()
