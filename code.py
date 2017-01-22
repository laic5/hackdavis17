from nltk.tokenize import RegexpTokenizer

with open('chp1.txt', 'r', encoding='utf-8') as f:
    bookText = f.readline() # list, each item is a paragraph

n = 1
passageDivider = 3      
currTime = 0
totalTimes = len(bookText) / passageDivider + 1
tokenizer = RegexpTokenizer(r'\w+')
wrongWords = []


# need to clean the passage so it will be easier to compare
# input: string list OR string 
# output: list of words, lower-case 
def cleanText(text, isList = False):

    if isList == True:
        newtext = " ".join(text)
    newtext = newtext.tolower()
    
    cleanedText = tokenizer.tokenize(newtext)
    return cleanedText 

    
# ask user if they wish to continue or not     
def getAnswer():
    answer = input("Do you wish to continue? (Enter 'yes' or 'no')\n")
    
    while answer != "yes" or answer != "no":
        answer = input("I'm sorry, I did not understand what you said. Please say 'yes' or 'no'.\n")
    

def excerptExtractor(ind):
    sideNum = 2
    
    if len(passageList) < (2 * sideNum + 1):
        excerpt = passageList # output the whole passage 
        return excerpt
    
    beginIndex = ind - sideNum
    endIndex = ind + sideNum 
    
    while beginIndex < 0:
        beginIndex += 1
        endIndex += 1
        
    excerpt = ' '.join(passageList[beginIndex:endIndex])
    
    return excerpt 
    
    
while currTime < totalTimes:
    if n + passageDivider - 1 < len(bookText):
        passage = bookText[n:]
    else:
        passage = bookText[n:(n + passageDivider - 1)]
        
    passageList = passage.split()
        
    cleanedPassage = cleanText(passage, isList = True)

    with open(WATSON_FILE, 'r') as watfile:             #########
        watsonIn = watfile.read()
        
    cleanedWatson = cleanText(watsonIn)

    
    # compare cleanedPassage and cleanedWatson now      #########
    # compare function
    # if words do not match
        # find where it is in the original passage 
        # index = the index of the word from the original passage, "passage"
        wrongWords.append(passage[index])
        
        print "You pronounced this word wrong: %s\n" %passage[index]
        #excerpt = passage[index - 2):(index + 2)] # be careful of the beginning and ends of the list!
        excerpt = excerptExtractor(index)
        print "It is found in this section of the passage: ...%s...\n" %excerpt # bold misread word, if possible
        print "This is how you correctly say it!\n"
        print "\n"

    

    # print diagnostics
    print "Number of words read wrong: %d\n" %len(wrongWords)
    # later-- add Speed: use clock timer 
    
    answer = getAnswer()
    if answer == "no":
        print "Thank you for using Booboobear Reading Bot :)"
        watfile.close()
        break
        
    currTime += 1
    n += passageDivider 
    watfile.close()
    
    
    
f.close()
