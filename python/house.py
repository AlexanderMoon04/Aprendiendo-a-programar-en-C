name = input("whats your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Griffindor\n")
    case "Draco":
        print("Slythering\n")
    case _:
        print("who\n")

students = ["Hermiona", "ELsucioHarry", "ROnCOnCOca"]

for student in students:
    print(student)
print("")

for i in range (len(students)): #len tells how longs the list is
    print(i + 1, students[i])
print("")

studentsdict = {
    "Hermione": "Gryfindor",
    "SucioHarry": "Grifindor",
    "Ronconcoca":"Marigua",
    "Yoonsina":"WWE",
    }
print(studentsdict["Hermione"])
print(studentsdict["SucioHarry"])
print("")

for studentdict in studentsdict: #Normally it iterates through the keys
    print(studentdict, studentsdict[studentdict], sep=", ")
print("")

studentsdict2 = [
    {"name": "Hermiona", "house": "Gryfindor", "Patronus": "Otter"},
    {"name": "Randy Orton", "house": "Smackdown", "Patronus": "Undertaker"},
    {"name": "Jeff Hardy", "house": "Gryfindor", "Patronus": "PaquitaLaDelBarrio"},
    {"name": "ESoTilin", "house": "La calle", "Patronus": None},
]

for studentsdict2 in studentsdict2:
    print(studentsdict2["name"], studentsdict2["house"], studentsdict2["Patronus"], sep= ", ")

