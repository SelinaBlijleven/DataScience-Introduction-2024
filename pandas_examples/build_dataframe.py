"""
build_dataframe.py

Builds klantenbestand.csv for a dummy dataset. If you want more realistic dummy data,
check out the faker_example for an example using the faker library.
"""
import numpy as np
import pandas as pd


namen = ["A", "B", "C", "D", "E", "F", "G"]
emailadressen = []
telefoonnummers = []

# Genereer wat data voor de persoonlijke informatie
for naam in namen:
    emailadres = f"{naam}@mail.com"
    cijfers = np.random.randint(0, 10, 10)

    telefoonnummer = ""
    for c in cijfers:
        telefoonnummer += str(c)

    emailadressen.append(emailadres)
    telefoonnummers.append(telefoonnummer)

# Aanmaken vanaf kolommen
df = pd.DataFrame(
    data={
        'naam': namen,
        'emailadressen': emailadressen,
        'telefoonnummers': telefoonnummers,
        'kinderen': np.random.randint(0, 4, len(namen)),
        'katten': np.random.randint(0, 4, len(namen)),
        'honden': np.random.randint(0, 4, len(namen))
    },
    index=emailadressen
)

print(df.describe())
#df.to_csv('klantenbestand.csv', index=False)

# Zoek naar een specifieke unieke index (label)
print(df.loc[['C@mail.com', 'G@mail.com']])

# Selecteer numerieke kolommen
print(df[['kinderen', 'katten', 'honden']])

# Selecteer alleen de waarden van de numerieke kolommen
print(df[['kinderen', 'katten', 'honden']].values)

print(df['naam'].apply(lambda x: x.lower()))
