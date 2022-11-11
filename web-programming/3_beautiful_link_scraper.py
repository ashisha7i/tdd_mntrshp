import requests
from bs4 import BeautifulSoup

o = requests.get("https://xkcd.com")
soup = BeautifulSoup(o.text)

print(soup.prettify())

## Find ALL links on the page
all_links = soup.find_all("a")

CBLUE = '\033[94m'
CRED = '\033[1;91m'
CEND = '\033[0m'


# Print the links
for link in all_links:
    print(f"{CRED}{link.text:60}{CEND} --> {CBLUE}{link.attrs['href']}{CEND}")