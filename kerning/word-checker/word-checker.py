from random import shuffle

with open('eng_news_2016_100K-words-UC.txt', 'r', encoding='utf-8') as f:
    words = 10000
    loadWords = [l[:-1] for l in f.readlines()]
    shuffle(loadWords)
    loadWords = loadWords[:words]


Variable([
    dict(name="Right", ui="EditText"),
    dict(name="Left", ui="EditText"),
    dict(name="Case", ui="PopUpButton", args=dict(items=['UC_UC', 'UC_lc', 'lc_lc'])),
    ], globals())
lista = list(Right)
listb = list(Left)
output = []
finalWords = []

for x in range(len(lista)):
    for y in listb:
        output.append(lista[x] + y)
        
if Case == 0:
    for uc in range(len(output)):
        output[uc] = output[uc].upper()
    for ucw in range(len(loadWords)):
        loadWords[ucw] = loadWords[ucw].upper()
        
if Case == 1:
    for cp in range(len(output)):
        output[cp] = output[cp].capitalize()
    for cpw in range(len(loadWords)):
        loadWords[cpw] = loadWords[cpw].capitalize()

if Case == 2:
    for lc in range(len(output)):
        output[lc] = output[lc].lower()
    for lcw in range(len(loadWords)):
        loadWords[lcw] = loadWords[lcw].lower()
        

print("#_____KERNING PAIRS______#")
print(*output, sep="\n")

for a in range(len(output)):
    finalWords.append("\n###_______"+output[a]+"______###\n")
    for i in range(len(loadWords)):
        if output[a] in loadWords[i]:
            finalWords.append(loadWords[i])
    

print("\n \n#_____KERNABLE WORDS______#")            
print (*finalWords, sep="\n")