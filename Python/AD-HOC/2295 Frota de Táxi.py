# SUBPROGRAMA
def combustivelMaisEconomico(pA, pG, kmLa, kmLg):
    if (pA / kmLa) >= (pG / kmLg):
        print('G')
    else:
        print('A')
    return None

# PROGRAMA PRINCIPAL
precoDoAlcool, precoDaGasolina, quilometroPorLitroAlcool, quilometroPorLitroGasolina = map(float, input().split())
combustivelMaisEconomico(precoDoAlcool, precoDaGasolina, quilometroPorLitroAlcool, quilometroPorLitroGasolina)
