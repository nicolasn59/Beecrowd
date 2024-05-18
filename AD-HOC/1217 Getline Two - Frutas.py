# SUBPROGRAMA
def consumoDeFrutas(dias):
    peso = valor = 0
    for dia in range(1, dias+1):
        valor += float(input())
        frutas = list(map(str, input().split()))
        print('day %s: %d kg' % (dia, len(frutas)))
        peso += len(frutas)

    mediaPeso = '%.2f kg by day' % (peso/dias)
    mediaPreco = 'R$ %.2f by day' % (valor/dias)
    return '%s\n%s' % (mediaPeso, mediaPreco)

# PRINCIPAL
numeroDeTestes = int(input())
print(consumoDeFrutas(numeroDeTestes))