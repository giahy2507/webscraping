
import feedparser
from summaryobject import Cluster, Document, Sentence
import nltk
from bs4 import BeautifulSoup
import requests
import re
def extract_words(url):
    '''
    Extracts words from a web.

    Parameters
    ----------
    url : string
        The url of the web.
    '''
    try:
        soup = BeautifulSoup(open("dailymailsample"))
    except:
        print('Cannot read ' + url)
        return None

    # Remove invisible elements
    for invisible_elem in soup.find_all(['script', 'style']):
        invisible_elem.extract()

    summary_sentences = []
    # Get texts from visible elements, concatenate them using spaces, and then lower all characters
    summary_tag = soup.find_all("ul", class_="mol-bullets-with-font")

    for child in summary_tag[0].contents:
        summary_sentences.append(child.contents[0].contents[0].text)

    document_sentences = []
    sentence_tags = soup.find_all("p", class_="mol-para-with-font")
    for sentence_tag in sentence_tags:
        sentence = sentence_tag.contents[0].text
        if sentence != "" or sentence_tag.string != None:
            document_sentences.append(sentence)


    print(summary_sentences)



    return None


if __name__ == "__main__":
    # rss = feedparser.parse('http://www.dailymail.co.uk/news/headlines/index.rss')
    extract_words("")

