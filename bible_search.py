#author: paulmarinos

from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd



# - webscrape
webpage = urlopen("http://www.gutenberg.org/files/10/10-h/10-h.htm")
soupd = BeautifulSoup(webpage, "lxml")
h3tags = soupd.find_all('h3')
ptags = soupd.find_all('p')



# - create list of chapter:verse numbers
chapters = []
for tag in h3tags:
    chapters.append(tag.get_text())



# - create list of verses
verses = []
for tag in ptags:
    verses.append(tag.get_text())



def searchVerses (w, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16):
    count = 0

    for verse in verses:
        if any(x in verse for x in [w, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16]):
            count +=1
            print (verse, "\n")

    print (count, "verses found")



#lower-case input with punctuations
word = input("\nsearch word: ")
wordl = word.lower()
wordlwspc = " " + wordl + " "
wordlwper = " " + wordl + "."
wordlwcom = " " + wordl + ","
wordlwcol = " " + wordl + ":"
wordlwscol = " " + wordl + ";"
wordlwque = " " + wordl + "?"
wordlwexc = " " + wordl + "!"
wordlwdash = " " + wordl + "-"


#capitalized input with punctuations
wordc = word.capitalize()
wordcwspc = " " + wordc + " "
wordcwper = " " + wordc + "."
wordcwcom = " " + wordc + ","
wordcwcol = " " + wordc + ":"
wordcwscol = " " + wordc + ";"
wordcwque = " " + wordc + "?"
wordcwexc = " " + wordc + "!"
wordcwdash = " " + wordc + "-"


searchVerses(wordlwspc, wordlwper, wordlwcom, wordlwcol, wordlwscol, wordlwque, wordlwexc, wordlwdash ,wordcwspc, wordcwper, wordcwcom, wordcwcol, wordcwscol, wordcwque, wordcwexc, wordcwdash)

