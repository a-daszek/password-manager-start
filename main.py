# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = web_ent.get() # zapisuje dane w zmiennej 'website' to co zostalo wpisane w polu web_ent
    email = em_us_ent.get()
    password = pass_ent.get()

    with open("data.txt", "a") as data_file:
        data_file.write(f"{website} || {email} || {password}\n")
        web_ent.delete(0, END) # czysci pole gdzie wpisano strone, przygotowuje pole na nowe dane
        pass_ent.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

window = Tk()
window.title("Password Manager")
window. config(padx=40, pady=40)

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