print("🌟Star Wars Name Generator🌟")
print("Hard edition")
print()
all = input("What is your firstname, lastname, your mother's maiden name and the city that you were born. You can seperate them with spaces.\n").split()

firstname = all[0].strip()
lastname = all[1].strip()
maidenname = all[2].strip()
city = all[3].strip()

name = f"{firstname[:3].title()}{lastname[:3].lower()} {maidenname[:2].title()}{city[-3:].lower()}"

print()
print(f"Your Star Wars name is {name}")