import csv
import requests
import sys
from bs4 import BeautifulSoup

def retrieve_words(url):
    print(url)
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    words_tl = soup.find_all('div', class_='col_a col text')
    words_en = soup.find_all('div', class_='col_b col text')

    clean_words = []

    for word_tl, word_en in zip(words_tl, words_en):
        clean_words.append([str(word_tl.find('div').text), str(word_en.find('div').text)])

    return clean_words

url = sys.argv[1]
start = int(sys.argv[2]) // 20 + 1
stop = int(sys.argv[3]) // 20 + 1

with open('output.csv', 'w', encoding='utf-8', newline='') as file:
    print(start, ",", stop)
    for x in range(start, stop):
        # example url without number after it
        # https://app.memrise.com/course/426582/top-5000-words-in-greek/
        newurl = url + str(x)
        writer = csv.writer(file)
        writer.writerows(retrieve_words(newurl))