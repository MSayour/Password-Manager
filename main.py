from tkinter import *
from tkinter import messagebox
import pyperclip
import random
import json



PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#228B22"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"


#-----------------------------------------------------------search function --------------------------------------#


def search():
    with open("data file.json","r") as data_file:
        data = json.load(data_file)
        try:
            messagebox.showinfo(title=website_entry.get(),message=f"your email is : {data[website_entry.get()]['email']}\n "
                  f"your password is : {data[website_entry.get()]['password']}")
        except KeyError:
            messagebox.showinfo(title=website_entry.get(),message="you don't have an email and password for this website")

# ----------------------------------------------------------- PASSWORD GENERATOR ------------------------------- #


letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','z']
num = ['1','2','3','4','5','6','7','8','9','0']
symbol = ['!','@','#','$','%','^','*']
def generate_password():
    password_entry.delete(0,END)
    letters_list = [random.choice(letters) for _ in range(random.randint(8,12))]
    num_list = [random.choice(num) for _ in range(random.randint(1,6))]
    symbols_list = [random.choice(symbol) for _ in range(random.randint(5,7))]
    pass_list = letters_list+num_list+symbols_list
    random.shuffle(pass_list)
    password = "".join(pass_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)


# ----------------------------------------------------- SAVE PASSWORD ------------------------------- #


def add():
    new_data = {
        website_entry.get(): {
            "email": email_entry.get(),
            "password": password_entry.get(),
        }
    }
    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(title="Warning", message="Don't leave any field empty")
    else:
        try:
            with open("data file.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data file.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data file.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)
            email_entry.insert(END, "@gmail.com")



# ------------------------------------------------------------------ UI SETUP ------------------------------- #


window = Tk()
window.title("password manager")
window.config(padx=20,pady=20,bg=YELLOW)
window.resizable(False,False)
window.minsize(height=400,width=450)

#labels and buttons

text1 = Label(text="Website",anchor='w')
text1.grid(row = 1,column = 0)

text2 = Label(text="Email / Username",anchor='w')
text2.grid(row = 2,column = 0)

text3 = Label(text="Password", bg=YELLOW, highlightthickness=0,anchor='w')
text3.configure(justify='left')
text3.grid(column = 0, row = 3)

website_entry = Entry(width=35)
website_entry.grid(column = 1, row = 1, columnspan = 2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column = 1, row = 2, columnspan = 2)
email_entry.insert(END,"@gmail.com")

password_entry = Entry(width=35)
password_entry.grid(column = 1, row = 3, columnspan = 2)

button1 = Button(text="Generate Password",command=generate_password,width=30)
button1.grid(column = 1, row=4)

button2 = Button(text="Add",width=30, command=add)
button2.grid(column = 1,row = 5,columnspan = 2)

button3 = Button(text="search",command=search)
button3.grid(column =3 ,row = 1)

canvas = Canvas(width=200,height=200,highlightthickness=0,bg=YELLOW)
lock_pick = PhotoImage(file="logo.png")

#-----------------------------------------------the 100,100 are the x,y position of the image--------------------#
canvas.create_image(100,100,image = lock_pick)
canvas.grid(row = 0,column = 1)
window.mainloop()