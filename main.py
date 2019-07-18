from bs4 import BeautifulSoup
import html5lib
import requests
import re
import itertools
import tkinter
import tkHyperlinkManager
import webbrowser
from functools import partial

#Declaring the variables
array_of_names = [""]
array_of_links = [""]
url = "https://gadgets.ndtv.com/news"
html = requests.get(url)

#Set true if Debugging
DEBUG = False

m=tkinter.Tk()


m.attributes("-fullscreen", True)
m.bind("<Escape>", lambda e: m.quit())
t=tkinter.Text(m)
t.insert(tkinter.END,"Please eait \n")

t.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand = tkinter.YES)
soup = BeautifulSoup(html.content, 'html5lib')

divfornews = soup.find_all("div", {"class": "story_list row margin_b30"})

if(DEBUG):
    print(divfornews)

#Find each news and append it to the list
for tag in divfornews:
    tdTags = tag.find_all("div", {"class": "caption_box"})
    for tag in tdTags:
        if DEBUG:

          print(tag.text)
        array_of_names.append(tag.text)

#Find the link for the news and then append it to the link list
for link_tag in divfornews:
    linkTags = link_tag.find_all("div", {"class": "thumb"})
    for tag1 in linkTags:

        for link in tag1.find_all("a"):
             array_of_links.append(link.get('href'))
             if(DEBUG):
               print(link.get('href'))

#Iterate through the list and print
text_for_tkinter=[""]
hyperlink=tkHyperlinkManager.HyperlinkManager(t)

for (i,j) in zip(array_of_names,array_of_links):
    print(i)
    print(j)
    print("////////////////////////////////")
    text_for_tkinter.append(i)
    text_for_tkinter.append(j)
    t.insert(tkinter.END,i+"\n")
    #Add the hyper link
    t.insert(tkinter.INSERT, j,
                hyperlink.add(partial(webbrowser.open, j)))




t.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand = tkinter.YES)
m.mainloop()

