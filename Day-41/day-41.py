website = {"name":None, "url":None,"desc":None,"rating":None}
website["name"] = name = input("Input the website name: ")
website["url"] = url = input("Input the URL: ")
website["desc"] = desc = input("Input your a description:: ")
website["rating"] = rating = input("Input the a star rating out of 5: ")
print()
for name,value in website.items():
    print(f"{name}: {value}", end=", ")