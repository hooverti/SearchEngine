from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import re


def parser(file_name):
    url  = open(file_name, "r")

    html = url.read()
    soup = BeautifulSoup(html, "lxml")
    for script in soup(["script", "style"]):
        script.decompose()

    text = soup.get_text()

    tokens = re.findall('\w+', text)
    word_freq = dict()
    stop_words = set(stopwords.words('english'))
    for word in tokens:
        nw = word.lower()
        if nw not in stop_words:
            if nw not in word_freq:
                word_freq[nw] = 1
            else:
                word_freq[nw] += 1

    #for x,y in word_freq.items():
    #    print("key: ", x, "freq:", y)
    return word_freq

if __name__ == "__main__":
    
    parser()
