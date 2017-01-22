from flask import Flask, request, redirect, url_for
import speech_recognition as sr
import time
import math
import string
from nltk.tokenize import RegexpTokenizer
wrongWords = []

app = Flask(__name__)

out = []
wholeParagraphs = []
HESITATION = 'hesitation'
tokenizer = RegexpTokenizer(r'\w+')

###endpoints
def speak():
    r = sr.Recognizer()
    m = sr.Microphone()

    with open('USERNAMES.txt', 'r') as f:
	USER = str(f.readline())
    with open('PASSWORDS.txt', 'r') as f:
	PASS = str(f.readline())
    print(USER,PASS)

    try:
	print("A moment of silence, please...")
	with m as source: r.adjust_for_ambient_noise(source)
	print("Set minimum energy threshold to {}".format(r.energy_threshold))
	while True:
	    print("Say something!")
	    start_time = time.time()
            with m as source: audio = r.listen(source)
	    print("Got it! Now to recognize it...")
	    et = time.time() - start_time
            try:
		value = r.recognize_ibm(audio, username=USER, password=PASS)
		if str is bytes:
                    ret = format(value).encode("utf-8")
                    #returning the spoken phrase as a string
                    return cleanText(ret)
                    print(u"You said {}".format(value).encode("utf-8"))
	    except sr.UnknownValueError:
		print("Oops! Didn't catch that")
	    except sr.RequestError as e:
		print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
    except KeyboardInterrupt:
	pass

#base route
@app.route("/")
def hello():
    return "I love Cindy!"


#the passed age of the user, returns their expected wpm
@app.route('/age', methods=['POST'])
def endpointWpm():
    age = request.form['age']
    age = math.floor(int(age))
    calc = getExpectedWPM(age)
    return str(calc)

#user speaks, returns string of spoken text
#assume you can only read one paragraph at a time
@app.route('/speak')
def callListen():
    spokenParagraphs = 'asdfasdf'
    writtenParagraphs = 'asdfasdf'
    speakCount = 0
    while speakCount < len(out):
        spokenParagraphs = speak()
        writtenParagraphs = getXParagraph(speakCount)
        #compareOneSpokenVsText(spokenParagraphs.split(), writtenParagraphs.split())
        speakCount += 1
        print(speakCount, len(out))

    return spokenParagraphs + '\n' + writtenParagraphs

#post a text file containing a chapter
@app.route('/book', methods=['POST'])
def book():
    a = request.files['content']
    wholeText = a.readlines()
    processedReadText(wholeText)

    return redirect(url_for('callListen'))
    #return renderText(wholeText)

###class functions to parse the entire text passed in
def processedReadText(wholeText):
    wholeParagraphs = ''
    for paragraphs in wholeText:
        newtext = (''.join(x for x in paragraphs if x in string.printable))
        out.append(cleanText(newtext))

    return out

def cleanText(newtext):
    newtext = newtext.lower()
    cleanedText = tokenizer.tokenize(newtext)
    cleanString = ' '.join(cleanedText)
    return cleanString

#gets the x paragraph from the list
def getXParagraph(x):
    if x > len(out):
        return out[len(out)-1]
    else:
	return out[x]

#utility function to get expected wpm
def getExpectedWPM(age):
    if age == 5:
        wpm = 45
    if age == 6:
        wpm = 60
    if age == 7:
        wpm = 90
    if age == 8:
        wpm = 115
    if age == 9:
        wpm = 130
    if age == 10:
        wpm = 145
    else:
        wpm = 160
    return wpm

def compareOneSpokenVsText(spoken, written):
    numHesitations = 0
    for writtenIndex, word in enumerate(written):
        if spoken[writtenIndex + numHesitations] == HESITATION:
            numHesitations += 1
            print(written[writtenIndex])

    #if len(spoken) != len(written):
    #    tup = makeStringLenghtsEqual(spoken, written)
    #    spoken = tup[0]
    #    written = tup[1]

    #findHesitations(spoken, written)

def makeStringLenghtsEqual(spoken, written):
    sgreater = len(spoken) - len(written)
    wgreater = len(written) - len(spoken)

    if sgreater > 0:
        alteredSpoken = spoken + sgreater * ' BOOBOOBEAR '
        return (alteredSpoken, written)

    if wgreater > 0:
        alteredWritten = written + wgreater * ' BOOBOOBEAR '
        return (alteredWritten, spoken)

def findHesitations(spoken, written):
    for ind, word in enumerate(cleanedWatson):
	if word == "%%HESITATION":
	    # do something
	    wrongWords.append(cleanedPassage[ind])

def findIndexOfWordInString(sentence):
    words = sentence.split(' ')
    for i, word in enumerate(words):
        if keyword == word:
            return (i+1)

def excerptExtractor(writtenText, hesitationIndex):
    sideNum = 2
    cleanedPassage = writtenText.split()

    ## NOTE: Using cleanedPassage right now. when more established, switch to clean original version
    if len(cleanedPassage) < (2 * sideNum + 1):
        excerpt = cleanedPassage # output the whole passage
        return excerpt

    beginIndex = hesitationIndex - sideNum
    endIndex = hesitationIndex + sideNum

    while beginIndex < 0:
        beginIndex += 1
        endIndex += 1

    excerpt = ' '.join(cleanedPassage[beginIndex:endIndex])

    return excerpt

def setNumberOfWordsInReadPassage():
    return 5

def wpmFromElapsedTime(elapsedTime):
    return 'blah'

def renderText(a):
    return 'blah'

def wordsInPassage():
    return 'blah'

if __name__ == "__main__":
    app.run(debug=True)
