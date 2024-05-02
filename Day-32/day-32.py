import random
language = ["Hello there!", "Konnichiwa!", "Guten Tag!", "Bore Da!", "Bonjour", "Bom dia"]
number = random.randint(0,len(language))
print(f"{language[number]}")