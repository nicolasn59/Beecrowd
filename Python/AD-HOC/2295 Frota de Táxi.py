# SUBPROGRAM
def mostEconomicalFuel(pA, pG, kmLa, kmLg):
    if (pA / kmLa) >= (pG / kmLg):
        print('G')
    else:
        print('A')
    return None

# MAIN PROGRAM
alcoholPrice, gasolinePrice, kmPerLiterAlcohol, kmPerLiterGasoline = map(float, input().split())
mostEconomicalFuel(alcoholPrice, gasolinePrice, kmPerLiterAlcohol, kmPerLiterGasoline)