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
def update_request_info(page_number):
    global req, webpage, soup, threads

    if page_number == 0:
        url = base_url+'forums/gaming-forum.7/'
        print(url)
        # update request info
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        soup = bs.BeautifulSoup(webpage, 'lxml')
        # update threads array
        threads = soup.find_all('div', {'class': 'structItem-title'})
    else:
        url = base_url+'forums/gaming-forum.7/'+page_url+str(page_number)
        print(url)
        # update request info
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        soup = bs.BeautifulSoup(webpage, 'lxml')
        # update threads
        threads = soup.find_all('div', {'class': 'structItem-title'})

def get_titles():
    global total_pages, threads, titles, title_text_file

    # update requests with each page
    for p in range(total_pages):
        update_request_info(p)
        print(threads)
        # iterate through all thread objects on current page
        for i in range(len(threads)):
            if str(threads[i].text).replace("\n", "") not in titles:
                titles.append(str(threads[i].text).replace("\n", ""))
                title_text_file.write(str(threads[i].text).replace("\n", "") + "\n")
                print("PAGE: " + str(p) + "\n" + "THREAD: " + str(i))

    title_text_file.close()
    print("Finished scraping titles!")

# RUN
get_titles()