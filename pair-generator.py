Variable([
    dict(name="Right", ui="EditText"),
    dict(name="Left", ui="EditText"),
    ], globals())
lista = list(Left)
listb = list(Right)
output = []

for x in lista:
    for y in listb:
        output.append(x)
        output.append(y)
        output.append("\n")

print(*output, sep="")