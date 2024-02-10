import requests

# Define the URL of the server to which you want to send data
url = 'http://localhost:9999'

# Define the data you want to send
data = {'message': 'Hello, server!'}

# Send a POST request with the data to the server
response = requests.post(url, json=data)

# Check if the request was successful
if response.status_code == 200:
    print('Data sent successfully!')
else:
    print('Failed to send data. Status code:', response.status_code)
