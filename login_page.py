from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Login system")
root.geometry('450x350')
root.config(bg="ivory")

my_lable = Label(root,text="Sign in to X",font=("ariel,25"))
my_lable.pack()

button_1 = Button(root,text='Sign in with Google',bd=0,bg="white",state="active")
button_1.pack()

button_2 = Button(root,text='Sign in apple',bd=0,bg="white",state="active")
button_2.pack()

my_lable = Label(root,text="OR").pack()

def onclick():
    if entry1.get() == 'jiggyboy' and entry2.get() == 'jiggyboy1':
        messagebox.showwarning('This warning page',f"The username must be in capital letter: {entry1.get()}\npassword okay ")
    elif entry1.get() == '' and entry2.get() == '':
        messagebox.showerror('This error page',"You need to fill up the Field")
    else:
        messagebox.showinfo('This X page',f"Succesful Login\nUsername : {entry1.get()}\npassword : {entry2.get()}")
        
    

username = Label(root,text="Username",font=("mono upper",13))
username.pack()

entry1 = Entry(root,width=40,borderwidth=3)
entry1.pack(padx=2)
# entry1.insert(0,"Username or Email")

password = Label(root,text="Password",font=("mono upper",13))
password.pack()


entry2 = Entry(root,width=40,borderwidth=3)
entry2.pack(padx=2)
# entry2.insert(0,"Password",)

button_4 = Button(root,text='Submit',bd=0,bg="white",state="active",font=("ariel,13"),width=10,command=onclick)
button_4.pack()
button_3 = Button(root,text='Forgot password?',bd=0,bg="white",state="active",font=("ariel,10"))
button_3.pack()





root.mainloop()