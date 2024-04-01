import requests

# Define the URL of the website you want to scrape
url = 'http://web-03.challs.olicyber.it/flag'

# Set Custom header authorization
headers = { 'X-Password': 'admin' }

# Send an HTTP GET request to the URL
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the HTML source code
    print(response.text)
else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)
