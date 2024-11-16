from gensim.models import KeyedVectors
import numpy as np
from scipy.spatial.distance import cosine

class WordEmbedding:
    def __init__(self):
        try:
            print("Ielādē modeli...")
            self.model = KeyedVectors.load_word2vec_format(
                'cc.lv.300.vec',
                binary=False,
                limit=100000
            )
            print("Modelis ielādēts!")
        except Exception as e:
            print(f"Kļūda ielādējot modeli: {e}")
            self.model = None

    def get_vector(self, word):
        try:
            return self.model[word]
        except:
            print(f"Vārds '{word}' nav atrasts modelī.")
            return None

    def get_similarity(self, word1, word2):
        try:
            return self.model.similarity(word1, word2)
        except:
            print(f"Nevar aprēķināt līdzību starp '{word1}' un '{word2}'")
            return None

def main():
    embeddings = WordEmbedding()
    
    words = ["māja", "dzīvoklis", "jūra"]
    
    print("\nVārdu vektori:")
    for word in words:
        vector = embeddings.get_vector(word)
        if vector is not None:
            print(f"\n{word}:")
            print(f"Vektora izmērs: {len(vector)}")
            print(f"Pirmie 5 elementi: {vector[:5]}")
    
    print("\nVārdu līdzības:")
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            similarity = embeddings.get_similarity(words[i], words[j])
            if similarity is not None:
                print(f"{words[i]} - {words[j]}: {similarity:.3f}")

if __name__ == "__main__":
    main() 