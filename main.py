import bs4 as bs
from urllib.request import Request, urlopen
import webbrowser as browser
import random

# base url to append links to
base_url = 'https://www.resetera.com/'
# setup beautiful soup
req = Request(base_url+'forums/gaming-forum.7/', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
soup = bs.BeautifulSoup(webpage, 'lxml')

# list of divs containing threads
thread_links = soup.find_all('div', {'class': 'structItem-title'})
hrefs = []

def store_hrefs():
    for i in range(len(thread_links)):
        hrefs.append(thread_links[i].contents[1].get('href'))

store_hrefs()
print(hrefs[random.randint(0, len(hrefs))])
#browser.open(base_url+hrefs[random.randint(0, len(hrefs))])