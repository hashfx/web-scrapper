import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
website = 'canva.com'
url = f'https://bugmenot.com/view/{website}'

# Define the headers (user-agent) to mimic a web browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Send a GET request to the website with headers
response = requests.get(url, headers=headers)

# Check if the response is successful (status code 200)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")
    exit()

# Find all the article elements with class 'account' that contain the usernames and passwords
account_articles = soup.find_all('article', class_='account')

# Check if any accounts were found
if not account_articles:
    print("No accounts found on the page.")
    exit()

# Loop through the article elements and extract the usernames and passwords
for article in account_articles:
    username = article.find('kbd').text.strip()
    password = article.find_all('kbd')[1].text.strip()
    success_rate = article.find('li', class_='success_rate').text.strip()
    age = article.find_all('li')[-1].text.strip()
    print(f"Username: {username}, Password: {password}, Success Rate: {success_rate}, Age: {age}")
