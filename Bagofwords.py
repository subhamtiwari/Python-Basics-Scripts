import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re


#Creating objects for the functions and 
stemmer=PorterStemmer()
wordnet=WordNetLemmatizer()

#Importing the data to a varibale 

para= '''Here is the detailed discussion of the  Stemming process in 
Natural Language Processing. Stemming and Lemmatization are one of the most 
important steps in Text Preprocessing,
What I like the most about your videos is the way you speak. 
Your voice is gentle and also the tone is humble and is very much like you want the viewer to 
really grasp the things you are talking about. 
Your explanations are simple and yet not so simple that it makes it boring. 
It is optimum. Greatly appreciated.Remove capitals – making everything lowercase
Removing stop words
Stemming – taking each word back to its root
CREATING A BAG OF WORDS MODEL USING NATURAL LANGUAGE PROCESSING
'''


#Cleaning the data > removing the commas . fullstop , using stemming or lemmization


sentence=nltk.sent_tokenize(para)

#Creating a list to store the data / words in the end
corpus=[]


#Stemmer
for i in range(len(sentence)):
    review=re.sub('[^a-zA-Z]',' ',sentence[i])
    review=review.lower()#Converting to lower Case 
    review=review.split()#Splitting the words
    review=[stemmer.stem(word) for word in review if not word in set(stopwords.words('english'))]
    corpus.append(review)#Appending all the words and inserting in the list 
    
#Lemmitization
for i in range(len(sentence)):
    review=review.sub('[^a-zA-Z]', ' ',sentence[i])
    review.lower()
    review=reveiew.split()
    review=wordnet.Lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
    corpus.append(review)
    


    



