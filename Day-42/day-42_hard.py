print("👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾")
print()
beast = {"name": None, "type":None, "move": None, "hp": None, "mp": None}
for name,value in beast.items():
    value = input(f"{name} ").strip().title()
    beast[name] = value
if beast["type"]=="earth":
  print("\033[32m", end="")
elif beast["type"]=="air":
  print("\033[37m", end="")
elif beast["type"]=="fire":
  print("\033[31m", end="")
elif beast["type"]=="water":
  print("\033[34m", end="")
else:
  print("\033[33m", end="")
for name,value in beast.items():
    print(f"{name}: {value}")