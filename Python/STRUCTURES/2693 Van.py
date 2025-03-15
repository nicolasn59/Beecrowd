# SUBPROGRAMA
def filtrarDistancia(lisDeAlunos):
    filtroDeDistancia = list()
    for _ in range(len(lisDeAlunos)):
        menorDistancia = lisDeAlunos[0]['distancia']
        indice = 0
        for i in range(1, len(lisDeAlunos)):
            if lisDeAlunos[i]['distancia'] < menorDistancia:
                menorDistancia = lisDeAlunos[i]['distancia']
                indice = i
        filtroDeDistancia += [lisDeAlunos[indice]]
        lisDeAlunos.pop(indice)
        if lisDeAlunos == []:
            return filtroDeDistancia


def filtrarDirecao(filtroDeDistancia):
    filtroDeDirecao = list()
    tamanho = len(filtroDeDistancia)
    for _ in range(tamanho):
        menorDistancia = filtroDeDistancia[0]['distancia']
        menorDirecao = filtroDeDistancia[0]['direcao']
        indice = 0
        for i in range(len(filtroDeDistancia)):
            if filtroDeDistancia[i]['direcao'] < menorDirecao and filtroDeDistancia[i]['distancia'] == menorDistancia:
                menorDirecao = filtroDeDistancia[i]['direcao']
                indice = i
        filtroDeDirecao += [filtroDeDistancia[indice]]
        filtroDeDistancia.pop(indice)
        if filtroDeDistancia == []:
            return filtroDeDirecao

def filtrarNome(filtroDeDirecao):
    filtroDeNome = list()
    tamanho = len(filtroDeDirecao)
    for _ in range(tamanho):
        menorDistancia = filtroDeDirecao[0]['distancia']
        menorDirecao = filtroDeDirecao[0]['direcao']
        menorNome = filtroDeDirecao[0]['nome']
        indice = 0
        for i in range(len(filtroDeDirecao)):
            if filtroDeDirecao[i]['nome'] < menorNome and filtroDeDirecao[i]['direcao'] == menorDirecao and filtroDeDirecao[i]['distancia'] == menorDistancia:
                menorNome = filtroDeDirecao[i]['nome']
                indice = i
        filtroDeNome += [filtroDeDirecao[indice]]
        filtroDeDirecao.pop(indice)
        if filtroDeDirecao == []:
            return filtroDeNome


# PROGRAMA PRINCIPAL
parar = False
while parar == False:
    try:
        alunosPresentes = int(input())
        listaDeAlunos = list()
        for i in range(alunosPresentes):
            aluno = dict()
            aluno['nome'], aluno['direcao'], aluno['distancia'] = input().split()
            listaDeAlunos.append(aluno)
    except EOFError:
        parar = True
    else:
        for i in range(len(listaDeAlunos)):
            listaDeAlunos[i]['distancia'] = int(listaDeAlunos[i]['distancia'])
        distanciaFiltrada = filtrarDistancia(listaDeAlunos)
        direcaoFiltrada = filtrarDirecao(distanciaFiltrada)
        melhoresRotas = filtrarNome(direcaoFiltrada)
        for rota in melhoresRotas:
            print(rota['nome'])
