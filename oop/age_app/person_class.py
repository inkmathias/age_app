# create a class called Person
# create init method
# 2 attributes (name, and birthdate)
# create an object from the Person class

from PIL import Image, ImageTk
import datetime
import tkinter as tk
import pygame



# Create frame
window = tk.Tk()

# Create frame geometry
window.geometry("300x300")

# Set frame title
window.title("Age Calculator App")

# Adding labels
year_label = tk.Label(text="Year")
year_label.grid(column=0, row=1)

month_label = tk.Label(text="Month")
month_label.grid(column=0, row=2)

day_label = tk.Label(text="Day")
day_label.grid(column=0, row=3)


# Adding entries
year_entry = tk.Entry()
year_entry.grid(column=1, row=1)

month_entry = tk.Entry()
month_entry.grid(column=1, row=2)

day_entry = tk.Entry()
day_entry.grid(column=1, row=3)


def calculate_age():
    print(year_entry.get())
    print(month_entry.get())
    print(day_entry.get())

    # Creates mathias object from Person class and assigns "Mathias
    # to the name argument and datetime.date to the birthdate argument
    person = Person("You", datetime.date(int(year_entry.get()),
                                              int(month_entry.get()),
                                              int(day_entry.get())))

    # Assigns the mathias object to the age function in Person class
    print(person.age())

    # Create a textfield inside the GUI
    text_answer = tk.Text(master=window, height=20, width=30)
    text_answer.grid(column=1, row=5)
    answer_text = "{name} are {age} years old".format(name=person.name, age=person.age())
    text_answer.insert(tk.END, answer_text)


pygame.init()
btn_sound = pygame.mixer.Sound("/Users/mathias/oop/age_app/button.wav")

def on_pressed(event):
    btn_sound.play()


# Adding a button
calc_button = tk.Button(text="Calculate", command=calculate_age)
calc_button.grid(column=1, row=4)
calc_button.bind("<Button-1>", on_pressed)



class Person:

    def __init__(self, name, birthdate):

        self.name = name
        self.birthdate = birthdate

# Function that calculates age to amount of years
    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        return age


# Adding an image
image = Image.open("/Users/mathias/Pictures/full.jpg")
image.thumbnail((100,100), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)

# Store image in label
label_image = tk.Label(image=photo)
label_image.grid(column=1, row=0)

# mathias = Person("Mathias", datetime.date(1987, 2, 18))
# print(mathias.age()) # Calls the age function

window.mainloop()