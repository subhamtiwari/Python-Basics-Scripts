import nltk
nltk.download()



paragrah='''Here is the detailed discussion of the  Stemming process in Natural Language Processing. Stemming and Lemmatization are one of the most important steps in Text Preprocessing,
What I like the most about your videos is the way you speak. 
Your voice is gentle and also the tone is humble and is very much like you want the viewer to 
really grasp the things you are talking about. 
Your explanations are simple and yet not so simple that it makes it boring. 
It is optimum. Greatly appreciated.'''paragrah='''Here is the detailed discussion of the  Stemming process in Natural Language Processing. Stemming and Lemmatization are one of the most important steps in Text Preprocessing,
What I like the most about your videos is the way you speak. 
Your voice is gentle and also the tone is humble and is very much like you want the viewer to 
really grasp the things you are talking about. 
Your explanations are simple and yet not so simple that it makes it boring. 
It is optimum. Greatly appreciated.'''

nltk.download('punkt')


#Tokenization : breaking down the words and sentenaces 

senetences=nltk.sent_tokenize(paragrah)

#Converting the para to words 

words=nltk.wordpunct_tokenize(paragrah)



