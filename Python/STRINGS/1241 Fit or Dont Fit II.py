# SUBPROGRAM
def fitsOrNot(numTests):
    while numTests != 0:
        A, B = input().split()
        if len(B) > len(A):
            print('nao encaixa')
        else:
            count = 0
            A, B = A[::-1], B[::-1]
            for i in range(len(B)):
                if B[i] == A[i]:
                    count += 1
            if count == len(B):
                print('encaixa')
            else:
                print('nao encaixa')
        numTests -= 1
    return None

# MAIN PROGRAM
numTests = int(input())
fitsOrNot(numTests)