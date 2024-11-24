from flask import Flask
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import subprocess
import random

from random_word import Wordnik

app = Flask(__name__)
r = Wordnik()

bootstrap = Bootstrap(app)

# Using the pip module "WordNik" was not returning enough of a variety of words. --->
## So instead I decided to create my own.

with open("/home/atatham45/mysite/names_parsable.txt") as f:
    name_list = []
    for line in f:
        name_list.append(line.strip())

with open("/home/atatham45/mysite/no_nsfw_long.txt") as f:
    raw_wordlist = []
    for line in f:
        raw_wordlist.append(line.strip())

with open("/home/atatham45/mysite/no_nsfw_med.txt") as f:
    for line in f:
        raw_wordlist.append(line.strip())

limit = len(raw_wordlist)
iter = 0

while iter < limit:
    for name in name_list:

        for word in raw_wordlist:
            iter += 1
            if name.lower() != word:
                pass
            elif name.lower() == word:
                raw_wordlist.remove(word)
                continue

def get_Words():
    limit = len(raw_wordlist)
    random_one = random.randint(0, limit)

    selection_one = raw_wordlist.pop(random_one)
    return selection_one

def scramble(word):
        arr = list(word)
        n = len(word)
        for i in range(n):
            j = random.randint(0, n-2)
            k = random.randint(0, n-3)
            element=arr.pop(j)
            additional=arr.pop(k)
            if j != k:
                arr.append(element)
                arr.append(additional)
                output = (" ".join(arr))
                return output
            elif j == k:
                arr.append(element)
                output = (" ".join(arr))
                return output
            else:
                arr.append(element)
                output = (" ".join(arr))
                return output
                break

def scramble_noError():
    NewWords = "invalid"
    global givenwords, scrambled_words
    while NewWords != "valid":
        try:
            givenwords = [
                get_Words(),
                get_Words(),
                get_Words()
                ]
            scrambled_words = [scramble(word) for word in givenwords]
        except Exception:
            break
        else:
            NewWords = "valid"
            return scrambled_words

@app.route('/', methods=['GET'])
def Home():
    return render_template('WordFind_LandingPage.html')

@app.route('/unscramble', methods=['GET'])
def UnScramble():

    scramble_noError()
    given_words = []

    for word in givenwords:
        given_words.append(word.lower())

    return render_template('WordFind_Unscramble.html', given_words = given_words, scrambled_words = scrambled_words)

