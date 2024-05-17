# -*- coding: utf-8 -*-
"""
Created on Sun May  5 13:51:56 2024

@author: Vincent Lomas

Used code from sieve.ai written by Rohit Bakoliya as a base for this model
https://github.com/rohitbakoliya/sieve.ai
"""

import string
from itertools import chain
import textract
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
     

def Preprocessfile(filename):
  text = textract.process(filename)
  text= text.decode('utf-8').replace("\n", " ")
  # print(text)
  x=[]
  tokens=word_tokenize(text)
  tok=[w.lower() for w in tokens]
  table=str.maketrans('','',string.punctuation)
  strpp=[w.translate(table) for w in tok]
  words=[word for word in strpp if word.isalpha()]
  stop_words=set(stopwords.words('english'))
  words=[w for w in words if not w in stop_words]
  x.append(words)
  # print(x)
  res=" ".join(chain.from_iterable(x))
  return res
     

x = Preprocessfile('jobtype.txt')
resume_words = Preprocessfile('resume.pdf')
# resume_words = Preprocessfile('bad_resume.pdf')

# Words to split
common_words = ['needs', 'must', 'preferred', 'email', 'phone', 'cv', 'page',
                'image', 'et', 'al', 'using', 'images', 'list', 'company',
                'track', 'forms']

x = [w for w in x.split() if w not in common_words] # Strip common words that are irrelevant
y= [word for word in resume_words.split() if word in x] 
y = [w for w in y if w not in common_words] # Ignore words only in resume for comparrision

# Remove duplicate words
y = list(dict.fromkeys(y))
x = list(dict.fromkeys(x))
z = list(dict.fromkeys(resume_words.split()))

# Form list of excess words and words missing
missing_words = [w for w in x if not w in y]
excess_words = [w for w in z if w not in common_words and not w in x]

y=" ".join(y)
x = " ".join(x)
text=[y,x]

print(f"Missing Words: {missing_words}")
print()
#print the similarity score
print("\n Similarity Score: ")
cv = CountVectorizer()
count_matrix = cv.fit_transform(text)
print(cosine_similarity(count_matrix))
matchpercent = cosine_similarity(count_matrix)[0][1]*100
matchpercent = round(matchpercent,2)

print("Your Resume matches about " + str(matchpercent) + "% of the job")
