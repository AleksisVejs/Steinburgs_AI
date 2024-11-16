from langdetect import detect_langs
from langdetect import DetectorFactory

DetectorFactory.seed = 0

def detect_language(text):
    try:
        langs = detect_langs(text)
        prob_langs = [(l.lang, l.prob) for l in langs]
        
        if any(lang == 'en' for lang, prob in prob_langs):
            return 'en'
            
        most_probable = prob_langs[0]
        if most_probable[1] > 0.5:
            return most_probable[0]
            
        return "Nevarēja noteikt valodu"
    except:
        return "Nevarēja noteikt valodu"

texts = [
    "Šodien ir saulaina diena.",
    "Today is a sunny day.",
    "Сегодня солнечный день."
]

for text in texts:
    language = detect_language(text)
    print(f"Teksts: '{text}'")
    print(f"Valoda: {language}\n")