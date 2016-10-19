from bs4 import BeautifulSoup
import requests
import re


wayback_url = "https://web.archive.org"

fi = open("vnexpress_data/vnexpress.net.link.txt", mode="r")
fo = open("vnexpress_data/training_full_urls.txt", mode="w")
fi.readline()
indexs_url = fi.readlines()
list_url = []
for counter, index_url in enumerate(indexs_url):

    html_text = requests.get(index_url[:-1]).text
    soup = BeautifulSoup(html_text)
    # todo set prefix of link
    links =  soup.findAll('a')
    xxx = [link.get('href') for link in links]
    for link in links:
        try:
            link_str = link.get('href').split("?")[0].split("#")[0]
            if len(link_str) > 100 and link_str.find("vnexpress.net/tin-tuc/") != -1 and link_str not in list_url:
                list_url.append(link_str)
                # print(link_str)
        except:
            continue
    print("get link", index_url[:-1])
    if counter +1 % 100 == 0:
        print("Save ", len(list_url), "url")
        for url in list_url:
            fo.write(url+"\n")
        list_url = []
print("Save ", len(list_url), "url")
for url in list_url:
    fo.write(url+"\n")
list_url = []
fo.close()
fi.close()