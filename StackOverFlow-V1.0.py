import requests
from bs4 import BeautifulSoup
import time
import csv


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}


def get_links(url):
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    links = soup.select('div.summary > div.result-link > span > a')
    for link in links:
        href = 'https://stackoverflow.com/' + link.get("href")
        get_infos(href)


def get_infos(url):
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    tittles = soup.select('#question-header > h1 > a')
    questions = soup.select('#question > div.post-layout > div.postcell.post-layout--right > div.post-text')
    answers = soup.select('div > div.answercell.post-layout--right > div.post-text')
    for tittle, question, answer in zip(tittles, questions, answers):
            tittle = tittle.get_text().strip()
            question = question.get_text().strip()
            answer = answer.get_text().strip()

            writer.writerow((tittle, question, answer, url))



if __name__ == '__main__':
    fp = open('Stack.csv', 'wt', newline='', encoding='utf-8')
    writer = csv.writer(fp)
    writer.writerow(('tittle', 'question', 'answer', 'url'))
    word = input('请输入想要爬取的关键词：')
    words = str(word)
    pages = input('请输入查询的页数（每页50条）：')
    page = int(pages) + 1
    urls = [('https://stackoverflow.com/search?page={}&tab=Relevance&pagesize=50&q=' + word).format(str(i))
            for i in range(1, page)]
    for url in urls:
        get_links(url)
        time.sleep(1)
    fp.close()
