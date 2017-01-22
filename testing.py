
with open('backend/alice/chp1.txt', 'r') as f:
    bookText = f.readlines() # list, each item is a paragraph


def getAnswer():
    answer = raw_input("Do you wish to continue? (Enter 'yes' or 'no') ")
    while answer != "yes" and answer != "no":
        answer = raw_input("I'm sorry, I did not understand what you said. Please say 'yes' or 'no'.\n")
        if answer == "yes" or answer == "no":
            break
        print answer
    return answer

n = 0
passageDivider = 3
currTime = 0
totalTimes = (len(bookText) + passageDivider - 1)/ passageDivider
#tokenizer = RegexpTokenizer(r'\w+')
wrongWords = []

#print bookText[0:2]
#print len(bookText)
#print "totalTimes: %d\n" %totalTimes

while currTime < totalTimes:
    if n + passageDivider > len(bookText):
        passage = str(bookText[n:])
    else:
        passage = str(bookText[n:(n + passageDivider - 1)])
    print "I love Varun infinity + x%d times\n" %(n+100)
    passageList = passage.split()


    n += passageDivider
    currTime += 1

    answer = getAnswer()
    if answer == "no":
        print "~~~\n\nThank you for using Booboobear Reading Bot :)"
        break
f.close()
