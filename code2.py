from nltk.tokenize import RegexpTokenizer

with open('chp1.txt', 'r') as f:
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
    
    ## NOTE: Using cleanedPassage right now. when more established, switch to clean original version
    if len(cleanedPassage) < (2 * sideNum + 1):
        excerpt = cleanedPassage # output the whole passage 
        return excerpt
    
    beginIndex = ind - sideNum
    endIndex = ind + sideNum 
    
    while beginIndex < 0:
        beginIndex += 1
        endIndex += 1
        
    excerpt = ' '.join(cleanedPassage[beginIndex:endIndex])
    
    return excerpt 
    
# this while loop will take the first passageDivider (3) amount of paragraphs
# and wait for the reader to read them and then process them.
# there is a user input question at the end which will ask the user 
# if they want to continue onto the next passageDivider (3) amount of paragraphs    
while currTime < totalTimes:
    if n + passageDivider - 1 < len(bookText):
        passage = bookText[n:]
    else:
        passage = bookText[n:(n + passageDivider - 1)]
        
    passageList = passage.split()
        
    cleanedPassage = cleanText(passage, isList = True)

    ### watsonIn is the string received from Watson on your side
        
    cleanedWatson = cleanText(watsonIn)

    # COMPARISON FUNCTION
    # assumptions: 
    # 1. lengths of cleanedPassage and cleanedWatson are the same
    # 2. the only form of impediment are the hesitations, which are represented by "%HESITATION"
    
    for ind, word in enumerate(cleanedWatson):
        if word == "%%HESITATION":
            # do something
            wrongWords.append(cleanedPassage[ind])
        
            print "Do you need help with this word? %s\n" %cleanedPassage[index] ###
            excerpt = excerptExtractor(index)
            print "It is found in this section of the passage: ...%s..." %excerpt # bold misread word, if possible
            print "This is how you correctly say it!"
        
            ### INSERT WATSON TEXT TO SPEECH ###
            print "\n"
        
    answer = getAnswer()
    if answer == "no":
        print "~~~\n\nThank you for using Booboobear Reading Bot :)"
        watfile.close()
        break
        
    currTime += 1
    n += passageDivider 
    watfile.close()
    
# print diagnostics
print "Number of words read wrong this session: %d\n" %len(wrongWords)
# later-- add Speed: use clock timer 
    
    
    
f.close()
