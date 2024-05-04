import os, time
listOfEmail = []
count = 0

def prettyPrint():
    os.system("clear")
    print("listofEmail")
    print()
    for index, email in enumerate(listOfEmail):
        print(f"{index}: {email}")
    time.sleep(1)

def spamPrint():
    global count
    os.system("clear")
    if count < len(listOfEmail):
        print(f"Dear {listOfEmail[count]}")
        print("It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.")
        print()
        print("Love and hugs,\nIan Spammington III \n")
        count += 1 
    else:
        print("No more emails to spam.")
    time.sleep(1)

while True:
    print("SPAMMER Inc.")
    menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
    if menu == "1":
        email = input("Email > ")
        listOfEmail.append(email)
    elif menu =="2":
        email = input("Email > ")
        if email in listOfEmail:
            listOfEmail.remove(email)
    elif menu == "3":
        prettyPrint()
        time.sleep(1)
    elif menu == "4":
        for i in range(10):
            spamPrint()
        break
    time.sleep(1)
    os.system("clear")