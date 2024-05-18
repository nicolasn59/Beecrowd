# algoritmo
# ENTRADA COM VARIOS TESTES
# RECEBER NUMERO DE BILHETES ORIGINAIS E DE PESSOAS PRESENTES
# RECEBER SEQUENCIA DE BILHETES EM UMA LISTA
# CONTAR QUANTOS BILHETES REPETIDOS(FALSOS) TEM NA SEQUENCIA
# IMPRIMIR RESULTADO DA CONTAGEM DE BILHETES FALSOS
#SUBPROGRAMA

# PROGRAMA PRINCIPAL

filtro_bilhetes = []
filtro_bilhetes_falsos = []

bilhetes_origianais, pessoas_presentes = map(int, input().split())
while bilhetes_origianais != 0 and pessoas_presentes != 0:

    sequencia_bilhetes = list(map(int, input().split()))
    for bilhete in sequencia_bilhetes:
        if bilhete in filtro_bilhetes:
            filtro_bilhetes_falsos.append(bilhete)
        else:
            filtro_bilhetes.append(bilhete)

    bilhetes_falsos = set(filtro_bilhetes_falsos)
    print(len(bilhetes_falsos))

    filtro_bilhetes.clear()
    filtro_bilhetes_falsos.clear()

    bilhetes_origianais, pessoas_presentes = map(int, input().split())
