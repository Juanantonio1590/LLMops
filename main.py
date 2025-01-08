import requests
from bs4 import BeautifulSoup

# URL of the Acquired Podcast episode
url = 'https://www.acquired.fm/episodes/mars-inc-the-chocolate-story'  # replace with actual episode URL

# Send HTTP request to fetch the page content
response = requests.get(url)
response.encoding = 'utf-8'

# Parse the page content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the transcript (replace with the actual HTML tag and class/ID)
transcript_section = soup.find('div', class_='transcript')  # adjust class or tag accordingly

# If the transcript is found, extract the text
if transcript_section:
    transcript = transcript_section.get_text(strip=True)
    print(transcript)
else:
    print('Transcript not found.')
    