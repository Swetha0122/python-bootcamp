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
Firstname = Label(Rainbow ,text = "First Name").grid(row = 1,column = 0)
LastName = Label(Rainbow ,text = "Last Name").grid(row = 2,column = 0)
Email = Label(Rainbow,text = "Email Id").grid(row = 3,column = 0)
AadharNumber = Label(Rainbow,text="Aadhar Number").grid(row=4,column=0)
Mobile = Label(Rainbow,text = "Contact Number").grid(row = 5,column = 0)
Language = Label(Rainbow,text="Language").grid(row =6,column = 0)
Address =  Label(Rainbow,text="Address").grid(row =7,column = 0)
Pincode = Label(Rainbow,text="Pincode").grid(row =8,column = 0)
Gender =Label(Rainbow ,text = "Gender",width=8,font=("bold",10)).grid(row = 9,column = 0)
BloodGroup = Label(Rainbow,text = "Blood Group").grid(row =10,column = 0)

Firstname1 = Entry(Rainbow).grid(row = 1,column = 1)
Lastname1 = Entry(Rainbow).grid(row = 2,column = 1)
Email1 = Entry(Rainbow).grid(row = 3,column = 1)
AadharNumber1 = Entry(Rainbow).grid(row = 4,column = 1)
Mobile1 = Entry(Rainbow).grid(row = 5,column = 1)
Language1 = Entry(Rainbow).grid(row = 6,column = 1)
Address1 = Entry(Rainbow).grid(row = 7,column = 1)
Pincode1 = Entry(Rainbow).grid(row = 8,column = 1)

var=IntVar()
Radiobutton(Rainbow, text="Male",padx = 20, variable=var, value=1).grid(row = 9,column = 1)
Radiobutton(Rainbow, text="Female",padx = 30, variable=var, value=2).grid(row = 9,column = 2)

#List of Blood group
list_of_BloodGroup =['A+','A-','B+','B-','O+','O-','AB+','AB-']

#Dropdown menu
a=StringVar()
dropdown = OptionMenu(Rainbow,a,*list_of_BloodGroup)
dropdown.config(width=18)
a.set('Select Blood Group')
dropdown.grid(row = 10,column = 1)
    
Button(Rainbow, text='Registration Form' , width=20,bg="grey",fg='white',font=("bold",10)).grid(row = 0,column =1)   
Button(Rainbow, text='Submit' , width=20,bg="black",fg='white',font=("bold",10)).grid(row = 15,column =1)
Rainbow.mainloop()
