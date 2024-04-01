import requests

# Define the URL of the website you want to scrape
url = 'http://web-02.challs.olicyber.it/server-records'

# define parameters
params = { 'id': 'flag'};

# Send an HTTP GET request to the URL
response = requests.get(url, params=params)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the HTML source code
    print(response.text)
else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)
