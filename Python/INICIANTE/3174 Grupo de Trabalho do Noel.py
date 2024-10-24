#SUBPROGRAMA
def producaoDePresentes(numElfos):
    somaBonecos = somaArquitetos = somaMusicos = somaDesenhistas = 0
    for i in range(numElfos):
        nome, profissao, tempoDeTrabalho = input().split()
        if profissao == "bonecos":
            somaBonecos += int(tempoDeTrabalho)
        elif profissao == "arquitetos":
            somaArquitetos += int(tempoDeTrabalho)
        elif profissao == "musicos":
            somaMusicos += int(tempoDeTrabalho)
        else:
            somaDesenhistas += int(tempoDeTrabalho)
    print("%d" % ((somaBonecos//8) + (somaArquitetos//4) + (somaMusicos//6) + (somaDesenhistas//12)))
    return None

# PRINCIPAL
numeroDeElfos = int(input())
producaoDePresentes(numeroDeElfos)
