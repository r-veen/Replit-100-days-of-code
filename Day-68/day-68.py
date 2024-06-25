import tkinter as tk

def check_guess():
    user_input = text.get("1.0", "end-1c").strip().lower()
    if user_input in images:
        file_path = images[user_input]
        image = tk.PhotoImage(file=file_path)
        image = image.subsample(3)
        canvas.create_image(150, 75, image=image)
        canvas.image = image
        result_label.config(text="", fg="black")
        canvas.pack()
    else:
        canvas.pack_forget()
        result_label.config(text="Unable to find this user", fg="red")

window = tk.Tk()
window.title("Person Finder")
window.geometry("500x500")

images = {"mo": "mo.png", "katie": "katie.png", "gerald": "gerald.png", "charlotte": "charlotte.png"}

hello = tk.Label(window, text="Guess Who?")
hello.pack()

text = tk.Text(window, height=1, width=40)
text.pack()

button = tk.Button(window, text="Find", command=check_guess)
button.pack()

canvas = tk.Canvas(window, width=300, height=150)
canvas.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
