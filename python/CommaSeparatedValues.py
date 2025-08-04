import csv

# tilines = []

# with open ("CommaSeparatedValues.csv") as file:
#     reader = csv.reader(file)
#     for name, home in reader:
#         tilines.append({"name": name, "home": home})

# with open ("CommaSeparatedValues.csv") as file:
#     reader = csv.DictReader(file) #dictionary helps to create a more flexible program
#     for row in reader:
#         tilines.append({"name": row ["name"], "home": row["home"]})

#     for tilin in sorted(tilines, key=lambda tilin: tilin["name"]) :
#         print(f"{tilin['name']} is from {tilin['home']}")


name = input("Whats your name? ")
home = input("Whats your home? ")

with open ("CommaSeparatedValues.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames = ["name", "home"])
    writer.writerow({"name": name, "home": home})




