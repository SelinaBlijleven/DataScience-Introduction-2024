import requests
import pandas as pd

# API to use, in this case the countries API
url = "https://restcountries.com/v3.1/all"

# Store the data here (will remain a list)
data = []

# Call the API, this depends on third party services, so we use try-except.
try:
    # Call the countries API
    results = requests.get(url)
    if results.status_code == 200:
        data = results.json()

except Exception as e:
    print("Error occurred:", str(e))

# If we have at least one entry, we can check its keys to see what information to use.
if len(data) > 0:
    print(data[0].keys())

countries = []
# Names for the columns in the CSV
columns = ["name", "capital", "currencies", "region", "subregion", "languages", "population"]

# Loop over the different countries
for result in data:
    # Get the name for each currency or set the currency to unknown.
    currency_names = [c for c in result.get('currencies', [])]
    languages = [c for c in result.get('languages', [])]
    capitals = [c[0] for c in result.get('capital', [])]

    # Store some information about this country.
    countries.append([
        result['name']['common'],                   # Always exists
        ", ".join(capitals),                        # Default to 'unknown'
        ", ".join(currency_names),                  # Separate currency names with commas
        result.get('region', "unknown"),            # Default to 'unknown'
        result.get("subregion", "unknown"),         # Default to 'unknown'
        ", ".join(languages),                       # Separate languages with commas
        result.get("population", -1),               # Get the population or set it to -1 if invalid
    ])

df = pd.DataFrame(countries, columns=columns)
df.to_csv("countries.csv")
