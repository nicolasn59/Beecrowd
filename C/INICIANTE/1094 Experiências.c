#include <stdio.h>

int main()
{
    int qtdExperimentos;
    float coelhos=0, ratos=0, sapos=0, totalCobaias, qtdCobaias;
    char cobaia[2], msg='%';
    scanf("%d", &qtdExperimentos);
    while (qtdExperimentos != 0)
    {
        scanf("%f %s", &qtdCobaias, cobaia);
        if (cobaia[0] == 'C')
            coelhos += qtdCobaias;
        else if (cobaia[0] == 'R')
            ratos += qtdCobaias;
        else
            sapos += qtdCobaias;
        qtdExperimentos -= 1;
    }
        totalCobaias = (coelhos+ratos+sapos);
        printf("Total: %.0f cobaias\n", totalCobaias);
        printf("Total de coelhos: %.0f\n", coelhos);
        printf("Total de ratos %.0f\n", ratos);
        printf("Total de sapos: %.0f\n", sapos);
        printf("Percentual de coelhos: %.2f %c\n", ((100.00*coelhos) / totalCobaias), msg);
        printf("Percentual de ratos: %.2f %c\n", ((100.00*ratos) / totalCobaias), msg);
        printf("Percentual de sapos: %.2f %c\n", ((100.00*sapos) / totalCobaias), msg);
    return 0;
}
