import tkinter as tk

clicked1 = False
clicked2 = False

count = 1

def switch():
    global count, clicked1, clicked2
    if clicked1:
        count += 1
    elif clicked2:
        count += 2
    update_image()
    update_text_and_buttons()

def clicked1_action():
    global clicked1, clicked2, count
    if count >= 3:  
        reset()
    else:
        clicked1 = True
        clicked2 = False
        switch()

def clicked2_action():
    global clicked1, clicked2, count
    if count >= 4:  
        reset()
    else:
        clicked1 = False
        clicked2 = True
        switch()

def reset():
    global count, clicked1, clicked2
    count = 1
    clicked1 = False
    clicked2 = False
    update_image()
    update_text_and_buttons()

def update_image():
    global count, image_label
    try:
        image = tk.PhotoImage(file=f"{count}.png")
        image_label.config(image=image)
        image_label.image = image
    except tk.TclError:
        print(f"Bild {count}.png konnte nicht geladen werden.")

def update_text_and_buttons():
    global count, hello, button1, button2
    if count == 1:
        T = "You meet a woman on the way to a Replit meetup IRL"
        B1 = "Ask her how she codes?"
        B2 = "Tell her about Replit"
    elif count == 2:
        T = "I can't code!"
        B1 = "Help her"
        B2 = "Make Fun"
    elif count == 3:
        T = "Thanks for the help"
        B1 = "Restart"
        B2 = ""
    elif count == 4:
        T = "Why are you making fun of me!!"
        B1 = "Restart"
        B2 = ""

    hello.config(text=T)
    button1.config(text=B1)
    button2.config(text=B2 if B2 else " ")

window = tk.Tk()
window.title("Person Finder")
window.geometry("1000x1000")

canvas = tk.Canvas(window, width=300, height=150)
canvas.pack()

image = tk.PhotoImage(file=f"{count}.png")
image_label = tk.Label(window, image=image)
image_label.pack()

hello = tk.Label(window, text="")
hello.pack()

button1 = tk.Button(window, text="", command=clicked1_action)
button1.pack()

button2 = tk.Button(window, text="", command=clicked2_action)
button2.pack()

update_text_and_buttons()

window.mainloop()
