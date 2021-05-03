from bs4 import BeautifulSoup
import requests
import re
import lxml

def scrape_links_from_single_url(url, filename):
    try:
        web=requests.get(url).text
        soup=BeautifulSoup(web, 'lxml')
        with open(filename, 'a') as file:
            for link in soup.findAll('a'):
                file.writelines('%s\n' % link.get('href'))
                print(link.get('href'))
    except Exception as e:
        print("Max retries exceeded with url. Failed to establish a new connection")


def scrape_links_from_multiple_urls(filename, output):
    try:
        with open(filename, 'r')as file1:
            file1=file1.readlines()
            for url in file1:
                web=requests.get(url).text
                soup=BeautifulSoup(web, 'lxml')
                with open(output, 'a') as file2:
                    for link in soup.findAll('a'):
                        file2.writelines('%s\n' % link.get('href'))
    except Exception as e:
        print("Max retries exceeded with url. Failed to establish a new connection")
