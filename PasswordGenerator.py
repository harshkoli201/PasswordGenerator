from tkinter import *
import random
import string

app = Tk()
app.title("Password Generator")
app.geometry('500x500')
app.configure(bg='grey')

def cal():
        l = int(b.get())
        tot = string.ascii_lowercase+string.ascii_uppercase+string.digits
        f = random.sample(tot,l)
        p = "".join(f)
        a.config(text="Your Password is = %s" % p)  

Lab = Label(app,text = "Welcome to Password Generator",bg= "gray",font='Helvetica 10 bold').place(x = 150,y = 20)  

Lab1 = Label(app,text = "Enter the length of your password",bg= "gray",font='Helvetica 10 bold').place(x = 150,y = 60)  

b = Entry(app, width=230)
b.pack(padx=150, pady= 100)  


button = Button(app, text="Generate Password", command=cal, bg="gray").place(x = 195,y = 150)  


a = Label(app, text='',bg= "gray",font='Helvetica 12 bold')
a.pack()

app.mainloop()