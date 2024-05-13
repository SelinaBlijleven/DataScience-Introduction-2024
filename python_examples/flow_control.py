# Maak vast een variabele aan de naam in op te slaan
name = ""

# While loop (we weten nog niet hoe vaak we gaan loopen)
while name == "":
    name = input("Wat is je naam?")

# als naam niet leeg is
if name != "":
    # zie f-strings
    print(f"Hallo {name}!")
else:
    # normaal printen
    print("Hallo!")

# Zie ook match case (switch implementatie van Python)
age = 29

if age > 18:
    print("Je bent volwassen!")
elif age == 17:
    print("Je bent bijna volwassen")
elif age == 16:
    print("Duurt nog eventjes")
else:
    print("Je bent nog een kind")

# For-loops (we weten hoe vaak we gaan loopen)
text = "Tekstje met dubbele woorden en met weinig leestekens en met veel woorden \n"

for word in text.split(" "):
    print(word)

# Nog een for-loop met getallen
grades = [7.0, 6.1, 6.4, 9.5]

for grade in grades:
    print(f"Je cijfer is {grade}")
