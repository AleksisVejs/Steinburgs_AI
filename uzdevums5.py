import re
import nltk
from nltk.tokenize import word_tokenize

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

def clean_text(text):
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'#\w+', '', text)
    
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"
        u"\U0001F300-\U0001F5FF"
        u"\U0001F680-\U0001F6FF"
        u"\U0001F1E0-\U0001F1FF"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        "]+", flags=re.UNICODE)
    text = emoji_pattern.sub(r'', text)
    
    text = re.sub(r'([!?])\1+', r'\1', text)
    
    text = re.sub(r'\s+', ' ', text)
    
    text = text.lower()
    
    text = re.sub(r'[^a-zāčēģīķļņšūž\s]', '', text)
    
    text = text.strip()
    
    return text

def main():
    raw_text = "@John: Šis ir lielisks produkts!!! Vai ne? 👏👏👏 http://example.com"
    
    print("Sākotnējais teksts:")
    print(raw_text)
    print("\nTīrīts teksts:")
    print(clean_text(raw_text))

if __name__ == "__main__":
    main() 