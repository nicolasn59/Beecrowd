#SUBPROGRAMA
#PROGRAMA PRINCIPAL
maior = 0
alunos = int(input())
while alunos != 0:
    matricula, nota = map(float, input().split())
    int(matricula)
    if maior < nota:
        maior = nota
        aprovado = matricula
    alunos -= 1
if maior < 8:
    print("Minimum note not reached")
else:
    print("%d" % aprovado)

