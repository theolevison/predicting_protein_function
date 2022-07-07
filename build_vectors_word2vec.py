import gensim
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',
                    level=logging.INFO)

sentences = []
print("Reading File")
with open("E:/Diss/"
          "word2vec_input_E.dat") as inputs:
    for line in inputs:
        entries = line.split()
        sentences.append(entries[1:])

print("Training Vector Embedding")
model = gensim.models.Word2Vec(sentences, min_count=0)
model.save('E:/diss/word2vec_E.model')
