"""
build_dataframe.py

Builds klantenbestand.csv for a dummy dataset using the faker library,
which can be used to generate somewhat real looking data.

Note that this simple application will generate email addresses that contain entirely
different names.
"""
import pandas as pd
from faker import Faker

N = 100

# Dummy info generator
fake = Faker()


def generate_fakes(n=N, f=fake.name) -> list:
    """
    Generate fake entries using a given function
    :param n:   Number of fakes
    :param f:   Function to generate fakes with
    :return:    List of desired length
    """
    return [f() for _ in range(n-1)]

# Aanmaken vanaf kolommen
df = pd.DataFrame(
    data={
        'naam': generate_fakes(f=fake.name),
        'land': generate_fakes(f=fake.country),
        'addres': generate_fakes(f=fake.address),
        'geboortedatum': generate_fakes(f=fake.date_of_birth)
    },
    index=generate_fakes(f=fake.email)
)

print(df.head())
df.to_csv('faker.csv', index=False)

