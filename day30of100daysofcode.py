print("day 30 of 100 days of code replit")

print("30 Days Down - What did you think?")
print()
learnt_today = []
for day in range(1, 31):
    i = input(f"What did you think about day: {day} ")
    learnt_today.append(i)

print(f"day: {day: ^2}{learnt_today: ^2}." end="\n")