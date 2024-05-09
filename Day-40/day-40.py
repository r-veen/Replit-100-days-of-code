name = input("Name:  ").strip()
date = input("Date of Birth:  ").strip()
number = input("Telephone number:  ").strip()
email = input("Email:  ").strip()
address = input("Adress:  ").strip()
info = {"name": name, "date": date, "number": number, "email": email, "address": address}
print()
print("---------------------------")
print(f"Hi {info['name']}. Our dictionary says that you were born on {info['date']}, we can call you on {info['number']}, email {info['email']}, or write to The Cupboard Under The Stairs, {info['address']}.")