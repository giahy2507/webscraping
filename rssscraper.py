
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
    except:
        print('Cannot parse: ' + url)
        return None

    soup = BeautifulSoup(html_text)

    # Remove invisible elements
    for invisible_elem in soup.find_all(['script', 'style']):
        invisible_elem.extract()

    reference_sentences = []
    # Get texts from visible elements, concatenate them using spaces, and then lower all characters
    summary_tag = soup.find_all("ul", class_="mol-bullets-with-font")
    if len(summary_tag) == 0:
        print( url + " dont have summary text")
        return None
    
    for child in summary_tag[0].contents:
        try:
            reference_sentences.append(Sentence(child.contents[0].contents[0].text))
        except:
            continue
    if len(reference_sentences) == 0:
        print("have bug")
        return None

    document_sentences = []
    sentence_tags = soup.find_all("p", class_="mol-para-with-font")
    for sentence_tag in sentence_tags:
        try:
            if len(sentence_tag.contents) == 0:
                continue
            xxx = sentence_tag.contents[0].text
            sentences = nltk.sent_tokenize(xxx)
            for sentence in sentences:
                if sentence != "" and sentence.find("Scroll down for video") == -1:
                    document_sentences.append(Sentence(sentence))
        except:
            print("except", sentence_tag)
            return None

    ref = Document(title=title, list_sentences=reference_sentences)
    doc = Document(title=title, list_sentences=document_sentences)
    return Cluster(-1, [doc], [ref], title=title)

import time
import os

if __name__ == "__main__":

    while True:
        if os.path.isfile("data/title.save.pickle"):
            with open("data/title.save.pickle", mode="rb") as f:
                title_save = pickle.load(f)
        else:
            title_save = []

        rss = feedparser.parse('http://www.dailymail.co.uk/news/headlines/index.rss')
        clusters = []
        for entry in rss.entries:
            if entry.title not in title_save:
                cluster = extract_document(entry.title, entry.link)
                if cluster is not None:
                        clusters.append(cluster)
                        title_save.append(entry.title)

        with open("data/title.save.pickle", mode="wb") as f:
            pickle.dump(title_save,f)

        if len(clusters) != 0:
            file_save = "data/"+str(time.time())+".cluster.save.pickle"
            with open(file_save, mode="wb") as f:
                pickle.dump(clusters,f)
            print("save", len(clusters), file_save )
        else:
            print("nothing to save")

        print("title.length",len(title_save))
        print("clusters.length",len(clusters))
        print("\n")
        time.sleep(60*60*8)





