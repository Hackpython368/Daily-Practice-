import random

letter = "abcdefghijklmnopqrstuvwxyz"
symbol = "!@#$%^&*:."
number = "123456789"

passwordLength = 9

randomPass = ""

charletter = 3

for i in range(charletter):
    count = random.randint(0,len(letter))
    randomPass += letter[count]

letter =letter.upper()
for i in range(charletter):
    count = random.randint(0,len(letter))
    randomPass += letter[count]

for i in range(charletter):
    count = random.randint(0,len(symbol))
    randomPass += symbol[count]

for i in range(charletter):
    count = random.randint(0,len(number))
    randomPass += number[count]


print(f"Generated Password : {randomPass}")