import nltk 
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

#nltk.download()



paragrah='''Here is the detailed discussion of the  Stemming process in Natural Language Processing. Stemming and Lemmatization are one of the most important steps in Text Preprocessing,
What I like the most about your videos is the way you speak. 
Your voice is gentle and also the tone is humble and is very much like you want the viewer to 
really grasp the things you are talking about. 
Your explanations are simple and yet not so simple that it makes it boring. 
It is optimum. Greatly appreciated.'''

#Convert the para to sente and then word and then use stop words to remove pratical words

sentence=nltk.sent_tokenize('paragrah')

#Creating a object for the function & package POTERSTEMMER

 stemmer=PosterStemmer()

#REMOVING THE WORDS WHICH ARE NOT USEFUL FOR THE SENTENCE AND ARE NOT MEANINGFUL

for i in range(len(sentence)):
    words=nltk.word_tokenize(sentence[i])
    words=[stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    sentence[i]=' '.join(words)