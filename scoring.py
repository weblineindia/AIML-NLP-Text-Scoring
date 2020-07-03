''' Text Keyword Match'''
#--------------------------------
# Date : 19-06-2020
# Project : Text Keyword Match
# Category : NLP/NLTK sentence Scoring
# Company : weblineindia
# Department : AI/ML
#--------------------------------
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.translate.bleu_score import sentence_bleu

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))


class scoreText(object):
    """
    A class used to score sentences based on the input keyword
    """

    def __init__(self):

        self.sentences = []

    def cleanText(self,sentences):
        """
        Eliminates the duplicates and cleans the text
        """
        try:
            sentences = list(set(sentences))
            mainBody = []
            for i, text in enumerate(sentences):
                text = re.sub("[-()\"#/@&&^*();:<>{}`+=~|!?,]", "", text)
                mainBody.append(text)
            return mainBody
        except:
            print("Error occured in text clean")

    def preProcessText(self,sentences):
        """
        Tokenization of sentence and lemmatization of words
        """
        try:
            # Tokenize words in a sentence
            word_tokens = word_tokenize(sentences)
            # Lemmatization of words
            wordlist = [lemmatizer.lemmatize(w) for w in word_tokens if not w in stop_words]

            return wordlist
        except:
            print("Error occured in text preprocessing")

    # similarity of subject
    def scoreText(self,keyword,sentences):
        """
        Compares sentences with keyword with bleu scoring technique
        """
        try:
            # Remove symbols from text
            sentences = self.cleanText(sentences)
            
            # Tokenization and Lennatization of the keyword
            keywordList = self.preProcessText(keyword)

            scoredSentencesList = []
            for i in range(len(sentences)):
               
                # Tokenization and Lennatization of the sentences
                wordlist = self.preProcessText(sentences[i])

                #list of keyword taken as reference
                reference = [keywordList]
                #sentence bleu calculates the score based on 1-gram,2-gram,3-gram-4-gram,
                #and a cumulative of the above is taken as score of the sentence.
                bleu_score_1 = sentence_bleu(reference, wordlist, weights=(1, 0, 0, 0))
                bleu_score_2 = sentence_bleu(reference, wordlist, weights=(0.5, 0.5, 0, 0))
                bleu_score_3 = sentence_bleu(reference, wordlist, weights=(0.33, 0.33, 0.34, 0))
                bleu_score_4 = sentence_bleu(reference, wordlist, weights=(0.25, 0.25, 0.25, 0.25))
                bleu_score = ( 4*bleu_score_4 + 3*bleu_score_3 + 2*bleu_score_2 + bleu_score_1 )/10

                #append the score with sentence to the list
                scList = [bleu_score,sentences[i]]
                scoredSentencesList.append(scList)
            return scoredSentencesList


        except:
            print("Error occured in score text")

   
    def sortText(self,scoredText):
        """
        Returns 3 top scored list of sentences
        """
        try:
            scoredTexts = sorted(scoredText, key = lambda x: x[0],reverse=True)
            scoredTexts = [v[1] for i,v in enumerate(scoredTexts) if i < 3]
            return scoredTexts
        except:
            print("Error occured in sorting text")

    def sentenceMatch(self,keyword,paragraph):
        """
        Converts paragraph into list and calls scoreText and sortText functions,
        and returns the most matching sentences with the keywords.
        """
        try:
            sentencesList = sent_tokenize(paragraph)
            scoredSentence = self.scoreText(keyword,sentencesList)
            sortedSentence = self.sortText(scoredSentence)
            return sortedSentence
        except:
            print("Error occured in sentence match")
        