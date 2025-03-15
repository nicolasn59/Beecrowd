# SUBPROGRAMA
def fazerMatriz():
	minhaMatriz = []
	for col in range(12):
		linha = []
		for lin in range(12):
			linha.append(float(input()))
		minhaMatriz.append(linha)
	return minhaMatriz


def somarLinha(linhaOp, matriz):
	somaDaLinha = 0
	for col in range(len(matriz)):
		somaDaLinha += matriz[linhaOp][col]
	return somaDaLinha


def mediarLinha(linhaOp, matriz):
	somaLinha = somarLinha(linhaOp, matriz)
	mediaDaLinha = somaLinha / len(matriz[linhaOp])
	return mediaDaLinha


# PRINCIPAL
linhaDaOperacao = int(input())
operacao = input()
essaMatriz = fazerMatriz()
if operacao == 'S':
	soma = somarLinha(linhaDaOperacao, essaMatriz)
	print('%.1f' % soma)
else:
	media = mediarLinha(linhaDaOperacao, essaMatriz)
	print('%.1f' % media)
