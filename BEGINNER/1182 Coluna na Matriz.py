# SUBPROGRAMA
def fazerMatriz():
	minhaMatriz = []
	for col in range(12):
		linha = []
		for lin in range(12):
			linha.append(float(input()))
		minhaMatriz.append(linha)
	return minhaMatriz


def somarColuna(colunaOp, matriz):
	somaDaColuna = 0
	for lin in range(len(matriz)):
		somaDaColuna += matriz[lin][colunaOp]
	return somaDaColuna


def mediarColuna(ColunaOp, matriz):
	somaColuna = somarColuna(ColunaOp, matriz)
	mediaDaColuna = somaColuna / len(matriz)
	return mediaDaColuna


# PRINCIPAL
colunaDaOperacao = int(input())
operacao = input()
essaMatriz = fazerMatriz()
if operacao == 'S':
	soma = somarColuna(colunaDaOperacao, essaMatriz)
	print('%.1f' % soma)
else:
	media = mediarColuna(colunaDaOperacao, essaMatriz)
	print('%.1f' % media)
