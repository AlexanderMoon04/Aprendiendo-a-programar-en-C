def meow():
    print("meow")

for i in range(3):
    meow()

while True: #infinite loop until the correct input is given
    n = int(input("whats in? "))
    if n > 0:
        break

for _ in range (n):
    print("Hijueputa")