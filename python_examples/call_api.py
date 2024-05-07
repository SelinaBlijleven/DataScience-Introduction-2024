"""
call_api.py

Run a small test run with an API to see what the data looks like.

python call_api.py https://api.example.com/data
"""
import sys
import requests


def call_api(api_url):
    try:
        # Make a GET request to the API endpoint
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Extract and print the JSON data from the response
            data = response.json()
            print(f"API Response:\n {data}")
            print(data.keys())
        else:
            # Print an error message if the request was unsuccessful
            print("Error:", response.status_code)
    except Exception as e:
        print("Error occurred:", str(e))


if __name__ == "__main__":
    # Check if the URL argument is provided
    if len(sys.argv) != 2:
        print("Usage: python call_api.py <API_URL>")
        sys.exit(1)

    # Get the API endpoint URL from command-line arguments
    url = sys.argv[1]

    # Call the API with the provided URL
    call_api(url)
