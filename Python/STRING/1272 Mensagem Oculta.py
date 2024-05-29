def decodificarMensagem(msgCod):
    msg = []
    if msgCod == []:
        return ''
    else:
        for palavra in range(len(msgCod)):
            msg.append(msgCod[palavra][0])
    return ''.join(msg)


# PROGRAMA PRINCIPAL
qtdDeFrases = int(input())
while qtdDeFrases != 0:
    mensagemCodificada = input().split()
    mensagem = decodificarMensagem(mensagemCodificada)
    print(mensagem)
    qtdDeFrases -= 1
