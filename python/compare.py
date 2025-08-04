s = input("s: ")
t = input ("t: ")

if s == t:
    print("Are the same")
else:
    print("Are different")

agree = input("Do you agree?(y/n): ").lower()

if agree in ["y", "yes"]:
    print("Agreed.")

elif agree in ["n", "no"]:
    print("Not agreed.")

else:
    print("Answer incorrect.")

# if agree == "Y" or agree == "y":
#     print("Agreed.")

# elif agree == "N" or agree == "n":
#     print("Not agreed.")

# else:
#     print("Answer incorrect.")
