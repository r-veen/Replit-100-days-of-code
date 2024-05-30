import csv
debugmode = False

try:
    with open("Day54Totals.csv") as file:
        reader = csv.DictReader(file)

        total = 0.0
        for row in reader:
            total += float(row["Cost"])
except Exception as err:
    print("Error: Unable to load")
    if debugmode:
        print(err)
print(f"Total: ${round(total,2)}")