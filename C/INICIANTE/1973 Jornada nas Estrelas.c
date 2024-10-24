#include <stdio.h>

int main () 
{
    unsigned long long numDeEstrelas;
    scanf("%llu", &numDeEstrelas);
    
    unsigned long long carneirosNasEstrelas[numDeEstrelas], cont, totalDeCarneiros;
    cont = totalDeCarneiros = 0;
    while (cont != numDeEstrelas)
    {
        scanf("%llu", &carneirosNasEstrelas[cont]);
        totalDeCarneiros += carneirosNasEstrelas[cont];
        cont += 1;
    }
    unsigned long long carneirosRoubados, estrelasAtacadas;
    cont = carneirosRoubados = 0;
    estrelasAtacadas = 1;
    while (cont != (unsigned long long)-1 && cont != numDeEstrelas)
    {
        if (carneirosNasEstrelas[cont] == 0)
        {
            printf("%llu %llu\n", estrelasAtacadas, (totalDeCarneiros - carneirosRoubados));
            return 0;
        }
        else if (carneirosNasEstrelas[cont] % 2 != 0)
        {
            carneirosNasEstrelas[cont] -= 1;
            carneirosRoubados += 1;
            cont += 1;
        }
        else
        {
            carneirosNasEstrelas[cont] -= 1;
            carneirosRoubados += 1;
            cont -= 1;
        }
        if (cont+1 > estrelasAtacadas)
        {
            if (cont == numDeEstrelas)
                estrelasAtacadas = cont;
            else
                estrelasAtacadas = cont+1;
        }
    }
    printf("%llu %llu\n", estrelasAtacadas, (totalDeCarneiros - carneirosRoubados));
    return 0;
}
