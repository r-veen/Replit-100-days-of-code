website = {"name":None, "url":None,"desc":None,"rating":None}
for i in website:
    website[i] = input(f"{i}:")
print()
for name,value in website.items():
    print(f"{name}: {value}", end=", ")