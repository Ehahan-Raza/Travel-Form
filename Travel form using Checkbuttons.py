from tkinter import *
import time
root=Tk()

root.geometry("633x333")

# Getting value through COMMAND
def getvals():
    print("Submitting Form...")
    time.sleep(3)
    print(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentmodevalue.get(), checkbuttonvalue.get()}")
    
    with open("records.txt","a")as f:
        f.write(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentmodevalue.get(), checkbuttonvalue.get()}\n")
        
# Title
root.title("Ehshan GUI")

# HEading
Label(text="Welcome to Travels",font="Comicsansms 15 bold").grid(row=0,column=2,pady=20)

# Text for our Form
name=Label(text="Name")
phone=Label(text="Phone")
gender=Label(text="Gender")
emergency=Label(text="Emergency Contact")
paymentmode=Label(text="Payment Mode")

# packing Text for our Form
name.grid()
phone.grid()
gender.grid()
emergency.grid()
paymentmode.grid()

#String Variable 
namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emergencyvalue=StringVar()
paymentmodevalue=StringVar()
checkbuttonvalue=IntVar()

# Entries for our Form
nameentry=Entry(textvariable=namevalue)
phoneentry=Entry(textvariable=phonevalue)
genderentry=Entry(textvariable=gendervalue)
emergencyentry=Entry(textvariable=emergencyvalue)
paymentmodeentry=Entry(textvariable=paymentmodevalue)

# Packing Entries for our Form
nameentry.grid(row=1,column=2)
phoneentry.grid(row=2,column=2)
genderentry.grid(row=3,column=2)
emergencyentry.grid(row=4,column=2)
paymentmodeentry.grid(row=5,column=2)

#Checkbuttons
checkbutton=Checkbutton(text="Do You Want To Prebook Your Meal?",variable=checkbuttonvalue)
checkbutton.grid(row=6,column=2)

# Button
Button(text="Submit",relief=RAISED,borderwidth=3,command=getvals).grid(row=7,column=2,pady=20)

root.mainloop()