# Semantic_similarity.py - This function takes in the flagged explicit lyric and detetcs how semantically close the new clean-edited word is 

#

import fasttext
import fasttext.util
from sklearn.manifold import TSNE
import numpy as np

embeddings = fasttext.load_model('en.bin')   #load embedding into memeory 


# takes in the bad word and a list of possibel replacemnt words using the N gram model 
def similarity(bad_words, edits):
    edit_scores = {}
    for word in edits:
        w1 = embeddings.get_word_vector(bad_words)
        w2 = embeddings.get_word_vector(word)
        dist = np.linalg.norm(w2 - w1)
        edit_scores[word] = dist 
        
    sorted_edit_scores =  sorted(edit_scores.items(), key=lambda x:x[1])
    return sorted_edit_scores 
