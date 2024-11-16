from textblob import TextBlob
from googletrans import Translator

def analyze_sentiment(text):
    translator = Translator()
    
    try:
        english_text = translator.translate(text, dest='en').text
        
        analysis = TextBlob(english_text)
        polarity = analysis.sentiment.polarity
        
        if polarity > 0.1:
            return "pozitīvs"
        elif polarity < -0.1:
            return "negatīvs"
        else:
            return "neitrāls"
    except:
        return "neitrāls"

def main():
    sentences = [
        "Šis produkts ir lielisks, esmu ļoti apmierināts!",
        "Esmu vīlies, produkts neatbilst aprakstam.",
        "Neitrāls produkts, nekas īpašs."
    ]
    
    for sentence in sentences:
        sentiment = analyze_sentiment(sentence)
        print(f"Teikums: '{sentence}'")
        print(f"Noskaņojums: {sentiment}\n")

if __name__ == "__main__":
    main()