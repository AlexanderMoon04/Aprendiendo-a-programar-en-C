x=int(input("x: "))
y=int(input("y: "))

print(f"The result is {x/y:.50f}")

if x > y:
    print("x is greater than y")
elif y > x:
    print("x is smaller than y")
else:
    print("x and y are equal")


