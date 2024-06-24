import tkinter as tk
import random

#This only works with the pictures

def check_guess():
    user_input = text.get("1.0", "end-1c").strip().lower()
    if user_input == random_key:
        load_new_image()
    else:
        result_label.config(text="Wrong", fg="red")


def load_new_image():
    global random_key, random_image_path, image
    new_key = random.choice(list(images.keys()))
    while new_key == random_key:
        new_key = random.choice(list(images.keys()))
    random_key = new_key
    random_image_path = images[random_key]
    image = tk.PhotoImage(file=random_image_path)
    image = image.subsample(3)
    canvas.itemconfig(image_id, image=image)
    window.image = image

window = tk.Tk()
window.title("Person Finder")
window.geometry("500x500")

images = {"mo": "mo.png", "katie": "katie.png", "gerald": "gerald.png", "charlotte": "charlotte.png"}

random_key = random.choice(list(images.keys()))
random_image_path = images[random_key]

hello = tk.Label(window, text="Guess Who?")
hello.pack()

text = tk.Text(window, height=1, width=40)
text.pack()

button = tk.Button(window, text="Find", command=check_guess)
button.pack()

canvas = tk.Canvas(window, width=300, height=150)
canvas.pack()

image = tk.PhotoImage(file=random_image_path)
image = image.subsample(3)
image_id = canvas.create_image(150, 75, image=image)

result_label = tk.Label(window, text="")
result_label.pack()

window.image = image

window.mainloop()
