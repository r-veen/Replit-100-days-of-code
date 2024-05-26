import time,os

orders = []
debugmode = False



def viewPizza():
  h1 = "Name"
  h2 = "Topping"
  h3 = "Size"
  h4 = "Quantity"
  h5 = "Total"
  print(f"{h1:^10}{h2:^20}{h3:^10}{h4:^10}{h5:^10}")
  for row in orders:
    print(f"{row[0]:^10}{row[1]:^20}{row[2]:^10}{row[3]:^10}{row[4]:^10}")
  if len(orders) < 2:
    print("You haven't ordered anything yet.")

def autoLoad():
  global orders
  f=open("pizzas.txt", "a")
  orders=eval(f.read())
  f.close()

def autoSave():
  f=open("pizzas.txt", "w")
  f.write(str(orders))
  f.close()
while True:
  answer = input("What do you wahnt to do add or view? ").strip().lower()
  if answer == "add":
    try:
      autoLoad()
    except Exception as err:
      print("Error: unable to load.")
      if debugmode:
        print(err)
    print("🌟Dave's Dodgy Pizzas🌟")
    try:
        count = int(input("How many pizzas? > "))

    except Exception as err:
        print("You must input a numerical ccharacter,")
        count = int(input("Try again, how many pizzas? > "))
    size = input("What size? S or M or B > ")
    name = input("Name please > ")
    toppings = input("Wich toppings do you wahnt on your pizza? > ")
    cost = 0
    if size =="s":
      cost = 5.99
    elif size =="m":
      cost = 9.99
    else:
      cost = 14.99
    total = cost * count
    total = round(total, 2)
    row = [name, toppings, size, count, total]
    orders.append(row)
    autoSave()
  elif answer == "view":
    viewPizza()
