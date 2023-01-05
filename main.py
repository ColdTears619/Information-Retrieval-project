import json
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import pandas as pd
import numpy as np
from rank_bm25 import BM25Okapi

filename = 'test.dev'
en_stops = set(stopwords.words('english'))
wordnet_lemmatizer = WordNetLemmatizer()
words_set = set()

# with open(filename) as fh:

#     out_file = open("collection.jsonl", "a") 
#     for line in fh:
 
#         # reads each line and trims of extra the spaces
#         # and gives only the valid words
#         command, description = line.strip().split(None, 1)
 
#         result = {
#             "id": command,
#             "contents": description
#         }
        
#         json.dump(result, out_file, indent = 4)
#         out_file.write("\n")
        
#     out_file.close()
 
# creating json file
# the JSON file is named as test1
# print(result)
# out_file = open("test2.json", "w")
# json.dump(result, out_file, indent = 4)
# out_file.close()


############################################################################################

#with open(filename) as data_file:
#    with open('output.dev', 'a') as output_file:
 #           output_file.write(data_file.read().lower())

###########################################################################################
#my_text = """The Advertisement was telecasted nationwide, and the product was sold in around 30 states of America."""

# with open ('test.dev') as ctl: 
#     with open('tokens.txt','w') as fout:
#         for line in ctl:
#             tokens = word_tokenize(line)
#             for term in tokens:
#                 lemm = wordnet_lemmatizer.lemmatize(term)
#                 print(' '.join(tokens), end='\n', file=fout)
# with open('test2.dev','r') as input , open('tokens.txt','w') as output:
    # for line in input:
        # tokens = word_tokenize(line)
        # for term in tokens:
            # lemm = wordnet_lemmatizer.lemmatize(term)
            # print(lemm, end='\t', file=output)
        # output.write('\n')

#############################################################################################

#- with open('tokens.txt','r') as input , open('stopwords.txt','w') as output:
#     for line in input:
#         tokens = word_tokenize(line)
#         for term in tokens:
#              if term not in en_stops:
#                 print(term, end='\t', file=output)
#         output.write('\n')

#################################################################################################

numberOfDoc = 0
with open('stopwords.txt') as f:
    lines = f.read().splitlines()
with open('stopwords.txt') as input:
     for line in input:
         words = line.split(' ')
         words_set = words_set.union(set(words))
         numberOfDoc = numberOfDoc + 1
   
     n_docs = numberOfDoc         #·Number of documents in the corpus
     n_words_set = len(words_set) #·Number of unique words in the
     
     ConvertSetToList = list(words_set)
     df_tf = pd.DataFrame(np.zeros((n_docs, n_words_set)), columns=ConvertSetToList)
     
     
     # Compute Term Frequency (TF)
     for i in range(n_docs):
            words = lines[i].split(' ') # Words in the document
            words.remove('')
            for w in words:
                df_tf[w][i] = df_tf[w][i] + (1 / len(words))
print(df_tf)

print("IDF of: ")

idf = {}

for w in words_set:
    k = 0  # number of documents in the corpus that contain this word

    for i in range(n_docs):
        words = lines[i].split(' ')
        words.remove('')
        if w in lines[i].split(' '):
            k += 1
    
    idf[w] =  np.log10(n_docs / (k + 1))

    #print(f'{w:>15}: {idf[w]:>10}' )


df_tf_idf = df_tf.copy()

for w in words_set:
    for i in range(n_docs):
        df_tf_idf[w][i] = df_tf[w][i] * idf[w]

print(df_tf_idf)    


with open('stopwords.txt') as f:
    lines = f.read().splitlines()

###########################################################################################