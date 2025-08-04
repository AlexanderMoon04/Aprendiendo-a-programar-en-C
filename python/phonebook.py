import csv

# name = input("Name: ")
# number = input ("Number: ")

with open("phonebook.csv", "r") as file:
# with open("phonebook.csv", "a") as file:

    reader = csv.DictReader(file)
    for row in reader:
        print(row["Name"])
    
    # writer = csv.DictWriter(file, fieldnames=["name", "number"])
    # writer.writerow({"name": name,"number": number})

# people = {
#     "Yulia": "6142298154",
#     "ElDiablo": "666",
#     "Yonsina": "777" 
# }
 
# name = input ("Name: ") 

# if name in people:
#     print(f"Number: {people[name]}")
# else:
#     print("Not found")
 


#Dictionaries
# people = [
#     {"name": "Alets", "number": "6142298154"}, #Represents a dictionary
#     {"name": "ElDiablo", "number": "666"}, 
#     {"name": "Yonsina", "number": "777"} 
# ]

# name = input ("Name: ")
# for person in people:
#     if person ["name"] == name:
#         number = person["number"]
#         print(f"founf {number}")
#         break 
# else:
#     print("Not found")


#LIST
# names = ["Yulia", "David", "Yoonsina"]

# name = input ("Name:")

# for i in names:
#     if name == i:
#         print("Found")
#         break
# else:
#     print("Not found")
    
