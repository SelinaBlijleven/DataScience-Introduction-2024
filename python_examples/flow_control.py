"""
flow_control.py

Deze file bevat wat voorbeelden van flow control in python.
"""
# Maak vast een variabele aan de naam in op te slaan
name = ""

"""
While loop

De while-loop wordt vaak gebruikt in een onvoorspelbare context. Bijvoorbeeld als we een paar keer moeten 
proberen om een server te bereiken, of om de input van een gebruiker te controleren (dat kan immers een paar keer 
fout gaan). De while loop bevat uiteraard het woordje 'while' gevolgd door een logisch statement. Deze is dan of 
True, of False. Als de conditie True is blijft de loop doorgaan, maar als de vergelijking uiteindelijk False wordt, 
wordt de loop uiteindelijk afgebroken.

Let op: als je een conditie schrijft die altijd waar is, maak je een programma dat in een infinite loop belandt.
Zie ook: break en continue
"""
# Blijf vragen tot er een naam is ingevuld (direct op enter klikken resulteert in de lege string "")
while name == "":
    name = input("Wat is je naam?")

"""
If-else

De if-else statement is een voorbeeld van conditionele code: code die alleen uitgevoerd wordt als er aan checks 
voldaan wordt. Je kunt alleen een if-statement gebruiken, of een combinatie van if/else. In het eerste geval voeren 
we dan alleen code uit als er aan de voorwaarde(n) voldaan is. In het tweede geval wordt er altijd code uitgevoerd, maar 
hangt de precieze verloop van het programma af van de waarden van variabelen.
"""
# als naam niet leeg is
if name != "":
    # zie f-strings
    print(f"Hallo {name}!")
else:
    # normaal printen
    print("Hallo!")

# Zie ook match case (switch implementatie van Python)
age = 29

"""
If-elif-else

If-elif-else is een conditionele constructie die gebruik maakt van meerdere mogelijke condities. Ook is het mogelijk 
om hier de else weg te laten. Elif staat voor else if: elif wordt dan ook alleen uitgevoerd als de bovenstaande if-statement 
niet waar is. Elif wordt vaak gebruikt wanneer we meerdere keren naar een enkele variabele kijken (age in dit geval). 
Als de leeftijd boven de 18 is, kan deze natuurlijk niet ook onder de 18 liggen. We hoeven de elif-regels dus alleen uit te 
voeren als we al weten dat de bovenste statement niet waar is.
"""
if age > 18:
    print("Je bent volwassen!")
elif age == 17:
    print("Je bent bijna volwassen")
elif age == 16:
    print("Duurt nog eventjes")
else:
    print("Je bent nog een kind")

# Wat denk je dat er gebeurt als we het script met leeftijd 15 runnen? Controleer het antwoord voor jezelf.
# if age == 15:
#   print("Je bent nu 15 jaar oud.")

"""
for-loop


"""
# For-loops (we weten hoe vaak we gaan loopen)
text = "Tekstje met dubbele woorden en met weinig leestekens en met veel woorden \n"

for word in text.split(" "):
    print(word)

# Nog een for-loop met getallen
grades = [7.0, 6.1, 6.4, 9.5]

for grade in grades:
    print(f"Je cijfer is {grade}")
