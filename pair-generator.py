Variable([
    dict(name="StringA", ui="EditText"),
    dict(name="StringB", ui="EditText"),
    ], globals())
lista = list(StringA)
listb = list(StringB)
output = []

for x in lista:
    for y in listb:
        output.append(x)
        output.append(y)
        output.append("\n")

print(*output, sep="")