import re

# . any character except a newline
# * 0 or more repetitions
# + 1 or more repetitions
# ? 0 or 1 repetition
# {m} m repetitions
# {m,n} m-n repetitions
# ^ matches the start of the string
# $ matches the end of the string or just before que newline at the end of the string
# [] set of characters  for example [a-zA-Z0-9_] to indicate only alphanumeric input (and _)
#[^] complementing the set
# \w represents word to refer alphanumeric symbols
# \W not a word character
# \d decimal digit
# \D not a decimal digit
# \s whitespace characters
# \S not a whitespace character
#-----------Groups-------------
# A|B either A or B
# (...) a group
# (?:...) non-capturing version



email= input("whats your email? ").strip()

if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE): #r - raw string, \ is for special sequences. ^ and $ indicates to only acept start and finish with the pattern proposed
    print("Valid")
else:
    print("Invalid")

