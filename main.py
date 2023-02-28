from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_list = []

for char in range(nr_letters):
  password_list.append(random.choice(letters))

for char in range(nr_symbols):
  password_list += random.choice(symbols)

for char in range(nr_numbers):
  password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_ent.get()  # zapisuje dane w zmiennej 'website' to co zostalo wpisane w polu web_ent
    email = em_us_ent.get()
    password = pass_ent.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message=f"You've left empty fields!")

    else:
        is_ok = messagebox.askokcancel(title=f"{website}", message=f"Are the account information correct?: \nEmail:"
                                                                  f" {email} \nPassword: {password}")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} || {email} || {password}\n")
                web_ent.delete(0, END)  # czysci pole gdzie wpisano strone, przygotowuje pole na nowe dane
                pass_ent.delete(0, END)


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

web_ent = Entry(width=35)
web_ent.grid(column=2, row=2, columnspan=2)
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

gen_pass_butt = Button(text="Generate Password")
gen_pass_butt.grid(column=3, row=4)

add_butt = Button(text="Add", width=30, command=save)
add_butt.grid(column=2, row=5, columnspan=2)

window.mainloop()
