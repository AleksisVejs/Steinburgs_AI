import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string

try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')

def process_text(text):
    tokens = word_tokenize(text.lower())
    
    tokens = [word for word in tokens if word not in string.punctuation and not word.isnumeric()]
    
    try:
        stop_words = set(stopwords.words('latvian'))
    except:
        stop_words = set(stopwords.words('english'))
    
    tokens = [word for word in tokens if word not in stop_words]
    
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    
    return set(tokens)

def calculate_overlap(text1, text2):
    words1 = process_text(text1)
    words2 = process_text(text2)
    
    common_words = words1.intersection(words2)
    
    total_unique_words = len(words1.union(words2))
    overlap_percentage = (len(common_words) / total_unique_words) * 100
    
    return common_words, overlap_percentage

def main():
    text1 = "Rudens lapas ir dzeltenas un oranžas. Lapas klāj zemi un padara to krāsainu."
    text2 = "Krāsainas rudens lapas krīt zemē. Lapas ir oranžas un dzeltenas."
    
    common_words, percentage = calculate_overlap(text1, text2)
    
    print(f"Kopīgie vārdi: {', '.join(common_words)}")
    print(f"Sakritības līmenis: {percentage:.2f}%")

if __name__ == "__main__":
    main() 