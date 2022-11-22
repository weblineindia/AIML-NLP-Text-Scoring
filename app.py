''' Keyword Matched Sentences '''
# --------------------------------
# Date : 19-06-2020
# Project : Keyword Matched Sentences
# Category : NLP/NLTK sentence Scoring
# Company : weblineindia
# Department : AI/ML
# --------------------------------
import scoring

print("#-----------------------------------------------------------#")

print("#------------------------- TEXT SCORING --------------------#")
# Enter keyword and paragraph
print("#-----------------------------------------------------------#")
keyword = input("ENTER KEYWORDS : ")
print("#############################################################")
paragraph = input("ENTER PARAGRAPH : ")
print("#############################################################")

# Initialize the textscoring instance
scoreTextObj = scoring.scoreText()
# Paragraph passed will be split inot sentences,
# Each sentence will be split and it will be compared with keyword and a score is given.
# Top scored sentence will be displayed as results.
matchedSentences = scoreTextObj.sentenceMatch(keyword, paragraph)
print()
print("#-------------------------- RESULTS ------------------------#")
print("#-------------------BEST MATCHING SENTENCES-----------------#")
print()
# print the top scored sentences

# try:
count = 1
for text in matchedSentences:
    print(' '+str(count)+' : '+text)
    count += 1
    print()
# except:
    # print('something went wrong')