print("👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾")
print()
name = input("Name: ").lower()
type = input("Type: ").lower()
move = input("Special Move: ").lower()
hp = input("HP: ").lower()
mp = input("MP: ").lower()
beast = {"name": name, "type":type, "move": move, "hp": hp, "mp": mp}
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