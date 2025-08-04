import re

url = input("URL: ").strip()
# print(url)
# username = url.removeprefix("https://twitter.com/", "")
# print(f"Username: {username}")

username= re.sub(r"^(https?://)?(www\.)?twitter\.com/", "". url)
print(f"Username: {username}")




if matches2 := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE):
    print(f"Username: ", matches2.group(1))



name = input("Whats your name? ").strip() 
# if "," in name:
#     last, first = name.split(", ")
#     name = f"{first} {last}"
if matches := re.search(r"^(.+), *(.+)$", name): # := walrus operator to asign a value and make a boolean question at same time
    # last, first = matches.groups()
    # name = f"{first} {last}"
    name = f"{matches.group(2)} {matches.group(1)}" #group 0 is already occupied, you must start from position 1
print(f"hello, {name}")

