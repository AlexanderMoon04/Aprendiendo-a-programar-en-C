while True:
    try: #Write all of the code inside try is a bad design practice. The correct way is only write the part of the code that could fail
        n =int(input("Input: ")) 
    except ValueError:
        print("Ese no es integer, w")
    else:
        print(f"Integer is {n}")
        break

while True:
    try:
        x = int(input("Height: "))
        y = int(input("Lenght: "))
        if x > 0 and y > 0:
            break
        else:
            print("both sizes must be > 0")
        
    except ValueError: 
        print("Incorrect value")


            

for i in range(x):
    print("#" * y)

