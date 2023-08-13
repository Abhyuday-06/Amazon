from bs4 import BeautifulSoup
from urllib.request import urlopen as uopen

user_input = input("Enter the name of the thing that you want to search on Amazon:")
n = user_input.replace(' ','+')
amazon_url = 'https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=' + str(n)


def download_data(url):
    response = uopen(url)
    page_html = response.read()
    response.close()
    soup = BeautifulSoup(page_html,'html.parser')
    containers = soup.findAll('div', {'class':'a-section a-spacing-small a-spacing-top-small'})
    cnt = len(containers)
    for i in range(0,cnt):
        print(i + 1, '--------')
        try:
            print(containers[i].find('span',{'class':'a-size-medium a-color-base a-text-normal'}).text)
        except AttributeError:
            print("", end='')
        try:
            print("Rs.",(containers[i].find('span',{'class':'a-price-whole'}).text))
        except AttributeError:
            print("", end='')
        try:
            print('Rating:', (containers[i].find('span',{'class':'a-icon-alt'}).text))
        except AttributeError:
            print("", end='')


download_data(amazon_url)
