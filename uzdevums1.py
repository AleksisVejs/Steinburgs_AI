import nltk
from collections import Counter
from nltk.tokenize import word_tokenize

nltk.download('punkt_tab')

teksts = "Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēkas. Kaķis gribēja redzēt sauli, bet saule slēpās aiz mākoņiem."

vardi = word_tokenize(teksts.lower())

vardi = [vards for vards in vardi if vards.isalnum()]

vardu_biezums = Counter(vardi)

print("Vārdu biežuma analīze:")
for vards, skaits in vardu_biezums.most_common():
    print(f"{vards}: {skaits}")