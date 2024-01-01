from textblob import TextBlob

words = ["crickt", "platfrm", "Machne Learning"]

spell_correct_words = []

for word in words:
    spell_correct_words.append(TextBlob(word))

print("Misspelled Words : ", words)
print("Corrected Words : ")
for word in spell_correct_words:
    print(word.correct())
