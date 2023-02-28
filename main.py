from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    password = "".join(password_list)
    pass_ent.insert(0, password)

    pyperclip.copy(password)  # od razu kopiuje wygenerowane haslo


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_ent.get()  # zapisuje dane w zmiennej 'website' to co zostalo wpisane w polu web_ent
    email = em_us_ent.get()
    password = pass_ent.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message=f"You've left empty fields!")
    else:
        try:
            # is_ok = messagebox.askokcancel(title=f"{website}", message=f"Are the account information correct?:
            # \nEmail:" {email} \nPassword: {password}")
            # with open("data.txt", "a") as data_file:
            #     data_file.write(f"{website} || {email} || {password}\n")
            #     web_ent.delete(0, END)  # czysci pole gdzie wpisano strone, przygotowuje pole na nowe dane
            #     pass_ent.delete(0, END)
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web_ent.delete(0, END)  # czysci pole gdzie wpisano strone, przygotowuje pole na nowe dane
            pass_ent.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    typed_web = web_ent.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops!", message="File does not exist.")
    else:
        if typed_web in data:
            email = data[typed_web]["email"]
            password = data[typed_web]["password"]
            messagebox.showinfo(title="Oops!", message=f"You already have an account on this site.\nEmail: {email}"
                                                       f" \nPassword: {password}")
        else:
            messagebox.showinfo(title="Oops!", message=f"No details found for {typed_web} website.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=2, row=1)

web_label = Label(text="Website:")
web_label.grid(column=1, row=2)

web_ent = Entry(width=17)
web_ent.grid(column=2, row=2)
web_ent.focus()

em_us_label = Label(text="Email/Username:")
em_us_label.grid(column=1, row=3)

em_us_ent = Entry(width=35)
em_us_ent.grid(column=2, row=3, columnspan=2)
em_us_ent.insert(0, "andziulasek@gmail.com")

pass_label = Label(text="Password:")
pass_label.grid(column=1, row=4)

pass_ent = Entry(width=17)
pass_ent.grid(column=2, row=4)

gen_pass_butt = Button(text="Generate Password", command=generate_password)
gen_pass_butt.grid(column=3, row=4)

add_butt = Button(text="Add", width=30, command=save)
add_butt.grid(column=2, row=5, columnspan=2)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=3, row=2)

window.mainloop()
