from transformers import pipeline

def translate_to_english(text):
    # Inicializējam tulkošanas pipeline ar Helsinki-NLP/opus-mt-lv-en modeli
    translator = pipeline("translation", model="Helsinki-NLP/opus-mt-lv-en")
    
    # Veicam tulkošanu
    translation = translator(text)[0]['translation_text']
    return translation

def main():
    # Teksti latviešu valodā
    latvian_texts = [
        "Labdien! Kā jums klājas?",
        "Es šodien lasīju interesantu grāmatu.",
        "Kā tev iet?"
    ]
    
    print("Tulkošana no latviešu valodas uz angļu valodu:")
    print("-" * 50)
    
    # Tulkojam katru tekstu
    for text in latvian_texts:
        translation = translate_to_english(text)
        print(f"LV: {text}")
        print(f"EN: {translation}")
        print("-" * 50)

if __name__ == "__main__":
    main()