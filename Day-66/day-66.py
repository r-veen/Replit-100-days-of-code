import tkinter as tk

window = tk.Tk()
window.title("Taschenrechner") 
window.geometry("600x400") 

input_text = "" 

def update_label(value):
    global input_text
    input_text += value  
    display_label["text"] = input_text  

def clear():
    global input_text
    input_text = "" 
    display_label["text"] = input_text 

def calculate():
    global input_text
    try:
        result = str(eval(input_text))
        display_label["text"] = result
        input_text = result
    except:
        display_label["text"] = "Error"
        input_text = ""

display_label = tk.Label(window, text=input_text, font=("Arial", 24))
display_label.grid(row=0, column=0, columnspan=5)

button1 = tk.Button(window, text="1", command=lambda: update_label("1"))
button1.grid(row=2, column=0)

button2 = tk.Button(window, text="2", command=lambda: update_label("2"))
button2.grid(row=2, column=1)

button3 = tk.Button(window, text="3", command=lambda: update_label("3"))
button3.grid(row=2, column=2)

button4 = tk.Button(window, text="4", command=lambda: update_label("4"))
button4.grid(row=3, column=0)

button5 = tk.Button(window, text="5", command=lambda: update_label("5"))
button5.grid(row=3, column=1)

button6 = tk.Button(window, text="6", command=lambda: update_label("6"))
button6.grid(row=3, column=2)

button7 = tk.Button(window, text="7", command=lambda: update_label("7"))
button7.grid(row=4, column=0)

button8 = tk.Button(window, text="8", command=lambda: update_label("8"))
button8.grid(row=4, column=1)

button9 = tk.Button(window, text="9", command=lambda: update_label("9"))
button9.grid(row=4, column=2)

button0 = tk.Button(window, text="0", command=lambda: update_label("0"))
button0.grid(row=5, column=1)

Pbutton = tk.Button(window, text="+", command=lambda: update_label("+"))
Pbutton.grid(row=2, column=3)

Mbutton = tk.Button(window, text="-", command=lambda: update_label("-"))
Mbutton.grid(row=2, column=4)

Tbutton = tk.Button(window, text="*", command=lambda: update_label("*"))
Tbutton.grid(row=3, column=3)

Dbutton = tk.Button(window, text="/", command=lambda: update_label("/"))
Dbutton.grid(row=3, column=4)

Ebutton = tk.Button(window, text="=", command=calculate)
Ebutton.grid(row=5, column=2)

Cbutton = tk.Button(window, text="C", command=clear)
Cbutton.grid(row=5, column=0)

tk.mainloop()
