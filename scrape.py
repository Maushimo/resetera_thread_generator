import bs4 as bs
from urllib.request import Request, urlopen
import random

total_pages = 1682

# base url to append links to
base_url = 'https://www.resetera.com/'
# page url to append at the end of the base url
page_url = 'page-'
# setup beautiful soup
req = Request(base_url+'forums/gaming-forum.7/', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
soup = bs.BeautifulSoup(webpage, 'lxml')

# list of divs containing threads
threads = soup.find_all('div', {'class': 'structItem-title'})
titles = []

title_text_file = open("data/titles.txt", "w")


# FUNCTIONS
def iterate_through_pages(page_number):
    if page_number != 0:
        req = Request(base_url+'forums/gaming-forum.7/', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        soup = bs.BeautifulSoup(webpage, 'lxml')
    else:
        req = Request(base_url+'forums/gaming-forum.7/'+page_url+str(page_number), headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        soup = bs.BeautifulSoup(webpage, 'lxml')


def get_titles():
    for p in range(total_pages):
        try:
            iterate_through_pages(p)
        except Exception as e:
            print(e)
        for i in range(len(threads)):
            try:
                titles.append(str(threads[i].text).replace("\n", ""))
                title_text_file.write(str(threads[i].text).replace("\n", "") + "\n")
            except Exception as e:
                print(e)

    title_text_file.close()

# RUN
get_titles()