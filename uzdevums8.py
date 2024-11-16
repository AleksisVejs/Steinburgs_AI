import spacy

nlp = spacy.load("lv_core_news_sm")

def atpazit_vienibas(teksts):
    doc = nlp(teksts)
    
    personvardi = []
    organizacijas = []
    
    for ent in doc.ents:
        if ent.label_ == "PER":
            personvardi.append(ent.text)
        elif ent.label_ == "ORG":
            organizacijas.append(ent.text)
    
    return personvardi, organizacijas

teksts = "Valsts prezidents Egils Levits piedalījās pasākumā, ko organizēja Latvijas Universitāte."

personvardi, organizacijas = atpazit_vienibas(teksts)

print("Atrastie personvārdi:", personvardi)
print("Atrastās organizācijas:", organizacijas)