# SUBPROGRAMA
def encaixaOuNao(numTestes):
    while numTestes != 0:
        A, B = input().split()
        if len(B) > len(A):
            print('nao encaixa')
        else:
            cont = 0
            A, B = A[::-1], B[::-1]
            for i in range(len(B)):
                if B[i] == A[i]:
                    cont += 1
            if cont == len(B):
                print('encaixa')
            else:
                print('nao encaixa')
        numTestes -= 1
    return None
# PROGRAMA PRINCIPAL
numeroDeTestes = int(input())
encaixaOuNao(numeroDeTestes)
