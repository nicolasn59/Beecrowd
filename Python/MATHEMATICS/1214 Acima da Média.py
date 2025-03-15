# SUBPROGRAMA
def calcularMedia(notasDosAlunos):
	somaNotas = 0
	for i in range(len(notasDosAlunos)):
		somaNotas += notasDosAlunos[i]
	mediaDasNotas = somaNotas/len(notasDosAlunos)
	return mediaDasNotas


def acimaDaMedia(notasDosAlunos, mediaDasNotas):
	contador = 0
	for i in range(len(notasDosAlunos)):
		if notasDosAlunos[i] > mediaDasNotas:
			contador += 1
	print("%.3f%%" % ((100*contador)/len(notasDosAlunos)))
	return None


# PROGRAMA PRINCIPAL

turmas = int(input())
while turmas != 0:
	notas = list(map(int , input().split()[1:]))
	media = calcularMedia(notas)
	acimaDaMedia(notas, media)
	turmas -= 1