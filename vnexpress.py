__author__ = 'HyNguyen'
import nltk
from bs4 import BeautifulSoup
import urllib.request
import time
import io
import datetime

def save_plain(dataset, fo):
    title, short_intro, detail = dataset
    words_title = nltk.word_tokenize(title)
    words_intro = nltk.word_tokenize(short_intro)
    words_detail = nltk.word_tokenize(detail)
    with io.open(fo, mode="w", encoding="utf8") as f:
        f.write(" ".join(words_title)+u"\n")
        f.write(" ".join(words_intro)+u"\n")
        f.write(" ".join(words_detail)+ u"\n")


def craw_data(url):
    try:
        with urllib.request.urlopen(url) as response:
            html_text = response.read()
            soup = BeautifulSoup(html_text)

            # Remove invisible elements
            for invisible_elem in soup.find_all(['script', 'style']):
                invisible_elem.extract()

            title = soup.find("div", class_ = "title_news").get_text().strip()
            short_intro = soup.find("div", class_ = "short_intro").get_text().strip()
            details = soup.find("div", class_ = "fck_detail").get_text().strip()
            details = nltk.sent_tokenize(details.replace("\n"," "))
            detail = " ".join([ string for string in details if len(string) > 20 ])
            return title, short_intro, detail
    except:
        return None, None, None


if __name__ == "__main__":

    with open("vnexpress_data/training_full_urls.txt", mode="r") as f:
        fullurls = f.readlines()

    for counter, fullurl in enumerate(fullurls):
        timestamp = fullurl[5:19]
        url = fullurl[20:-1]
        title, short_intro, detail = craw_data(url)
        if title is not None:
            save_plain((title, short_intro, detail),"vnexpress_data/data_craw/{0}_{1}.txt".format(timestamp,counter))
        else:
            print("Exception URL:", url)

        if counter % 500 == 0 and counter != 0:
            print("sleeping")
            time.sleep(300)

