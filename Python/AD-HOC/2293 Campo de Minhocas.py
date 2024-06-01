# SUBPROGRAMA
def somaDasMinhocas(campo, lins, cols):
    somaLinhas = somaColunas = maiorSoma = 0
    for linha in range(lins):
        for coluna in range(cols):
            somaLinhas += campo[linha][coluna]
        if somaLinhas > maiorSoma:
            maiorSoma = somaLinhas
        somaLinhas = 0
    for coluna in range(cols):
        for linha in range(lins):
            somaColunas += campo[linha][coluna]
            if somaColunas > maiorSoma:
                maiorSoma = somaColunas
        somaColunas = 0
    return maiorSoma

# PROGRAMA PRINCIPAL
campoDeMinhocas = []
linhas, colunas = map(int, input().split())
for i in range(linhas):
    celulas = list(map(int, input().split()))
    campoDeMinhocas.append(celulas)
totalDeMinhocas = somaDasMinhocas(campoDeMinhocas, linhas, colunas)
print(totalDeMinhocas)