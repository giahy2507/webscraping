
import feedparser
from summaryobject import Cluster, Document, Sentence
import nltk
from bs4 import BeautifulSoup
import requests
import re
import pickle

def extract_document(title, url):
    '''
    Extract Summary & Document

    Parameters
    ----------
    url : string
        The url of the web.
    '''
    try:
        html_text = requests.get(url).text

        soup = BeautifulSoup(html_text)

        # Remove invisible elements
        for invisible_elem in soup.find_all(['script', 'style']):
            invisible_elem.extract()

        reference_sentences = []
        # Get texts from visible elements, concatenate them using spaces, and then lower all characters
        summary_tag = soup.find_all("ul", class_="mol-bullets-with-font")

        for child in summary_tag[0].contents:
            reference_sentences.append(Sentence(child.contents[0].contents[0].text))

        document_sentences = []
        sentence_tags = soup.find_all("p", class_="mol-para-with-font")
        for sentence_tag in sentence_tags:
            sentences = sentence_tag.contents[0].text
            sentences = nltk.sent_tokenize(sentences)
            for sentence in sentences:
                if sentence != "" and sentence.find("Scroll down for video") == -1:
                    document_sentences.append(Sentence(sentence))

        ref = Document(title=title, list_sentences=reference_sentences)
        doc = Document(title=title, list_sentences=document_sentences)
        return Cluster(-1, [doc], [ref], title=title)
    except:
        print('Cannot parse: ' + url)
        return None

if __name__ == "__main__":
    title_save = []
    rss = feedparser.parse('http://www.dailymail.co.uk/news/headlines/index.rss')
    clusters = []
    for entry in rss.entries:
        cluster = extract_document(entry.title, entry.link)
        if cluster is not None:
            if entry.title not in title_save:
                clusters.append(cluster)
                title_save.append(entry.title)

    with open("data/data_scraping.pickle", mode="wb") as f:
        pickle.dump((title_save,cluster),f)

    print(len(title_save))
    print(len(clusters))




