import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from string import punctuation
from heapq import nlargest
import re

class TextSummarizer:
    def __init__(self):
        # Initialize NLTK resources
        try:
            nltk.data.find('tokenizers/punkt')
            nltk.data.find('corpora/stopwords')
        except LookupError:
            nltk.download('punkt')
            nltk.download('stopwords')
        
        # Get stopwords
        try:
            self.stop_words = set(stopwords.words('latvian'))
        except:
            self.stop_words = set(stopwords.words('english'))
        self.stop_words.update(set(punctuation))
        
        # Latvian specific words to exclude
        self.stop_words.update({'ir', 'un', 'ar', 'kas', 'tā', 'no'})

    def clean_text(self, text):
        # Basic text cleaning
        text = re.sub(r'\s+', ' ', text)
        text = text.strip()
        return text

    def get_word_frequency(self, text):
        words = word_tokenize(text.lower())
        return FreqDist(word for word in words 
                       if word not in self.stop_words and word.isalnum())

    def score_sentences(self, sentences, word_freq):
        scores = {}
        for sentence in sentences:
            words = word_tokenize(sentence.lower())
            word_count = len([word for word in words if word.isalnum()])
            if word_count == 0:
                continue
                
            # Calculate score based on word frequency and position
            score = sum(word_freq[word] for word in words 
                       if word in word_freq)
            # Normalize by sentence length
            scores[sentence] = score / word_count
            
            # Give bonus to first sentence
            if sentence == sentences[0]:
                scores[sentence] *= 1.25
        return scores

    def summarize(self, text, num_sentences=2, num_keywords=5):
        # Clean text
        text = self.clean_text(text)
        
        # Tokenize into sentences
        sentences = sent_tokenize(text)
        
        if len(sentences) <= num_sentences:
            return text, []
        
        # Get word frequencies
        word_freq = self.get_word_frequency(text)
        
        # Score sentences
        sentence_scores = self.score_sentences(sentences, word_freq)
        
        # Select top sentences
        summary_sentences = nlargest(num_sentences, sentence_scores, 
                                   key=sentence_scores.get)
        summary_sentences.sort(key=lambda x: sentences.index(x))
        
        # Get key words
        key_words = [word for word, freq in word_freq.most_common(num_keywords)]
        
        return ' '.join(summary_sentences), key_words

def main():
    text = """Latvija ir valsts Baltijas reģionā. Tās galvaspilsēta ir Rīga, kas ir slavena ar savu vēsturisko centru un skaistajām ēkām. Latvija robežojas ar Lietuvu, Igauniju un Krieviju, kā arī tai ir piekļuve Baltijas jūrai. Tā ir viena no Eiropas Savienības dalībvalstīm."""
    
    summarizer = TextSummarizer()
    
    print("Sākotnējais teksts:")
    print(text)
    print("\n" + "="*50 + "\n")
    
    summary, keywords = summarizer.summarize(text)
    
    print("Kopsavilkums:")
    print(summary)
    print("\nGalvenie atslēgvārdi:")
    print(", ".join(keywords))

if __name__ == "__main__":
    main()