#Flask Web Deployment

from flask import Flask
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import subprocess
import random


from random_word import Wordnik

app = Flask(__name__)
r = Wordnik()

bootstrap = Bootstrap(app)

def scramble(word):
        arr = list(word)
        n = len(word)
        for i in range(n):
            j = random.randint(0, n-2)
            element=arr.pop(j)
            arr.append(element)
            output = (" ".join(arr))
            return output
            break

def scramble_noError():  #Purpose of function is too prevent the program from failing
    NewWords = "invalid"  #whenever the "Random Words" are unable to be generated on the first try
    global given_words, scrambled_words  #due to any filters that may be in place.
    while NewWords != "valid":
        try:   #See below for an example of the "filters" mentioned previously.
            given_words = [
                r.get_random_word(maxLength=10, excludePartOfSpeech="noun", minCorpusCount=1200, hasDictionaryDef="true"),
                r.get_random_word(maxLength=10, excludePartOfSpeech="noun", minCorpusCount=1200, hasDictionaryDef="true"),
                r.get_random_word(maxLength=10, excludePartOfSpeech="noun", minCorpusCount=1200, hasDictionaryDef="true")
                ]
            scrambled_words = [scramble(word) for word in given_words]
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

    return render_template('WordFind_Unscramble.html', given_words = given_words, scrambled_words = scrambled_words)










#x = shuff_output_3(type)
#print(x)
#output = x
#with open("output.txt", "w") as file:
    #file.write(output)


#app.run(debug=True)
