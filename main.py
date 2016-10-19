
import time
import os
from summaryobject import *
import pickle
import xml.etree.cElementTree as ET

if __name__ == "__main__":

    data = "data"
    file_names = os.listdir(data)
    root = ET.Element("data")
    counter = 0
    for file_name in file_names:
        if file_name[0] == ".":
            continue
        if len(file_name.split(".")) == 5:
            with open(data + "/" + file_name, mode="rb") as f:
                clusters = pickle.load(f)
                print(len(clusters))
        for cluster in clusters:
            sentences_doc = cluster.list_documents[0].__str__()
            sentences_ref = cluster.list_references[0].__str__()
            doc = ET.SubElement(root, "cluster", id=str(counter))
            ET.SubElement(doc, "document").text = sentences_doc
            ET.SubElement(doc, "summary").text = sentences_ref
            counter +=1
    tree = ET.ElementTree(root)
    tree.write("data_dailymail.xml")

