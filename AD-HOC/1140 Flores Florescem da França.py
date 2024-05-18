# VARIOS CASOS DE TESTES
# RECEBER A ENTRADA EM STRING
# VERIFICAR SE A FRASE É UM TATOGRAMA
# IMPRIMIR RESULTADO Y SE SIM, CASO CONTRÁRIO, IMPRIMIR N
# PASSO A PASSO:
# 1: RECEBER EM UMA LISTA
# 2: INICIAR UM LOOP FOR PARA VERIFICAR O INDICE DA PALAVRA E DA LETRA
# 3: VER A POSIÇÃO DAS PALAVRAS E VERIFICAR SE TODAS ELAS TEM A MESMA LETRA DO INDICE 0 DA PALAVRA NO INDICE 0
# ENTRADA TERMINAR EM "*"

# SUBPROGRAMA
def verificarTautograma(letras):
    filtroDeLetras = []
    for posicao in range(len(letras)):
        if letras[posicao][0].lower() == letras[0][0].lower():
            filtroDeLetras.append('Y')
        else:
            filtroDeLetras.append('N')
    if 'N' in filtroDeLetras:
        return 'N'
    else:
        return 'Y'


# PROGRAMA PRINCIPAL
frase = list(map(str, input().split()))
while frase[0][0] != '*':
    resultado = verificarTautograma(frase)
    print(resultado)
    frase = list(map(str, input().split()))
