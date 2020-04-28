from random import shuffle

with open('eng_news_2016_100K-words-UC.txt', 'r', encoding='utf-8') as f:
    words = 10000
    loadWords = [l[:-1] for l in f.readlines()]
    shuffle(loadWords)
    loadWords = loadWords[:words]


Variable([
    dict(name="Right", ui="EditText"),
    dict(name="Left", ui="EditText"),
    ], globals())
lista = list(Right)
listb = list(Left)
output = []
finalWords = []

for x in range(len(lista)):
    for y in listb:
        output.append(lista[x] + y)

print("#_____KERNING PAIRS______#")
print(*output, sep="\n")

for a in range(len(output)):
    finalWords.append("\n###_______"+output[a]+"______###\n")
    for i in range(len(loadWords)):
        if output[a] in loadWords[i]:
            finalWords.append(loadWords[i])
    

print("\n \n#_____KERNABLE WORDS______#")            
print (*finalWords, sep="\n")