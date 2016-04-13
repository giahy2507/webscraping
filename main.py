
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
        reference_sentences.append(Sentence(child.contents[0].contents[0].text))

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

    ref = Document(title=title, list_sentences=reference_sentences)
    doc = Document(title=title, list_sentences=document_sentences)
    return Cluster(-1, [doc], [ref], title=title)

if __name__ == "__main__":
    a = extract_document("hynguyen", "http://www.dailymail.co.uk/news/article-3534797/Bristol-Palin-blasts-hypocrites-Twitter-refusing-ban-Azealia-Banks-rapper-called-Sarah-Palin-gang-raped-rant-social-media-site.html?ITO=1490&ns_mchannel=rss&ns_campaign=1490")
    if a is None:
        print("ttdtilu")