from flask import Flask, request
import speech_recognition as sr
import time
import math

app = Flask(__name__)

@app.route('/listen')
def listen():
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
		# recognize speech using Google Speech Recognition
		#value = r.recognize_google(audio)
		value = r.recognize_ibm(audio, username=USER, password=PASS)

		# we need some special handling here to correctly print unicode characters to standard output
		if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                    ret = format(value).encode("utf-8")
                    wpmFromEt(et)
                    return ret
                    print(u"You said {}".format(value).encode("utf-8"))
	    except sr.UnknownValueError:
		print("Oops! Didn't catch that")
	    except sr.RequestError as e:
		print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
    except KeyboardInterrupt:
	pass

@app.route("/")
def hello():
    return "I love Cindy!"

@app.route('/book', methods=['POST'])
def book():
    a = request.files['content']
    wholeText = a.readlines()
    return renderText(wholeText)

def renderText(a):
    return 'blah'

def wordsInPassage():
    return 'blah'

@app.route('/age', methods=['POST'])
def endpointWpm():
    age = request.form['age']
    age = math.floor(int(age))
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

    return str(wpm)

def wpmFromEt(et):
    getExpectedWPM()


if __name__ == "__main__":
    app.run(debug=True)
