__author__ = 'HyNguyen'
import os
import codecs
import numpy as np
import codecs

class Cluster(object):
    def __init__(self, cluster_id ,list_documents, list_references, title = ""):
        self.list_documents = list_documents
        self.list_references = list_references
        self.length_documents = len(list_documents)
        self.length_references = len(list_references)
        self.cluster_id = cluster_id
        self.title = title
        self.my_summarys = []

    def __str__(self):
        documentstr = ""
        referencestr = ""
        for document in self.list_documents:
            for sentence in document.list_sentences:
                documentstr = documentstr + sentence.string + "\n"

        for document in self.list_references:
            for sentence in document.list_sentences:
                referencestr = referencestr + sentence.string + "\n"

        return documentstr +"\n\n" +referencestr

class Document(object):
    def __init__(self,title, list_sentences , document_id = -1,):
        self.title = title
        self.list_sentences = list_sentences
        self.document_id = document_id
        self.length = len(list_sentences)
        self.word_count = sum([sentence.length for sentence in list_sentences if isinstance(sentence, Sentence)])

    def __str__(self):
        txt = ""
        for sentence in self.list_sentences:
            txt = txt + sentence.string + "\n"
        return txt

class Sentence(object):
    def __init__(self, string, vector = None):
        self.string = string
        self.vector = vector
        self.length = string.count(" ")
        self.sentece_id = -1

import numpy as np
import time
import pickle

if __name__ == "__main__":

    print("ttdt")