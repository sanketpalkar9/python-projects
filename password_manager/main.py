from tkinter import *
from tkinter import messagebox
from random import *



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(choice(letters))

    for char in range(nr_symbols):
        password_list += choice(symbols)

    for char in range(nr_numbers):
        password_list += choice(numbers)

    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = username_input.get()
    password = password_input.get()

    if len(email)==0 or len(password)==0 or len(website)==0:
        messagebox.showinfo(title="Oops",message="Please don't leave any field empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200, height= 200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)


label1 = Label(text="Website:")
label1.grid(row=1,column=0)
label2 = Label(text="Email/Username:")
label2.grid(row=2,column=0)
label3 = Label(text="Password:")
label3.grid(row=3,column=0)

website_input = Entry()
website_input.grid(row=1,column=1,columnspan=2)
website_input.config(width=35)
website_input.focus()

username_input = Entry()
username_input.grid(row=2,column=1,columnspan=2)
username_input.config(width=35)
username_input.insert(0,"sanketpalkar996@gmail.com")

password_input = Entry()
password_input.config(width=21)
password_input.grid(row=3,column=1)


generate_password = Button(text="Generate Password",command=generate_password)
generate_password.grid(row=3,column=2)

add = Button(text="Add",command=save)
add.config(width=36)
add.grid(column=1,row=4,columnspan=2)



window.mainloop()
