# índices:
# X0 = 0; X1 = 2
# Y0 = 1; Y1 = 3

cont = 0
plano1 = list(map(int, input().split()))
plano2 = list(map(int, input().split()))

if (plano2[0] <= plano1[0] <= plano2[2]) or (plano2[0] <= plano1[2] <= plano2[2]) or (plano1[0] <= plano2[0] <= plano1[2]) or (plano1[0] <= plano2[2] <= plano1[2]): # X0
    cont += 1
if (plano2[1] <= plano1[1] <= plano2[3]) or (plano2[1] <= plano1[3] <= plano2[3]) or (plano1[1] <= plano2[1] <= plano1[3]) or (plano1[1] <= plano2[3] <= plano1[3]): # Y0
    cont += 1

if cont >= 2:
    print(1)
else:
    print(0)
