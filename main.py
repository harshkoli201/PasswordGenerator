
import random
import string
import tkinter

app = tkinter.Tk()
app.title("Password Generator")
app.geometry('500x500')
app.configure(bg='grey')


Lab = tkinter.Label(app,text = "Welcome to Password Generator",bg= "gray",font='Helvetica 10 bold').place(x = 150,y = 20)  

Lab1 = tkinter.Label(app,text = "Enter the length of your password",bg= "gray",font='Helvetica 10 bold').place(x = 150,y = 60)  

a=tkinter.Entry(app, width=30).place(x = 165,y = 100)  


def cal():
    l = tkinter.int(a.get())
    tot = string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation
    f = random.sample(tot,l)
    password = "".join(f)

b = tkinter.Button(app, text="Generate Password", command=cal).place(x = 195,y = 150)  

app.mainloop()