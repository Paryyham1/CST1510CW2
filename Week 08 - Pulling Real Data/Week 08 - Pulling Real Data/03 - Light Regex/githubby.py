import requests

url = "https://raw.githubusercontent.com/Paryyham1/CST1510/main/Week%2004%20-%20Lists%2C%20Dictionaries%20and%20Files/LAB/records_sample.txt"
response = requests.get(url, timeout=10)
print(response.status_code)
print(response.text[:100])