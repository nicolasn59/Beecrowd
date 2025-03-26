#include <stdio.h>

int main()
{
    int count = 1, interGoals, gremioGoals, grenal, draws = 0, interWins = 0, gremioWins = 0, totalGrenais = 0;
    while (count == 1)
    {
        scanf("%d %d", &interGoals, &gremioGoals);
        if (interGoals > gremioGoals)
            interWins += 1;
        else if (gremioGoals > interGoals)
            gremioWins += 1;
        else
            draws += 1;
        
        printf("Novo grenal (1-sim 2-nao)\n");
        scanf("%d", &grenal);
        if (grenal == 2)
            count = 0;
        totalGrenais += 1;
    }
    printf("%d grenais\n", totalGrenais);
    printf("Inter:%d\n", interWins);
    printf("Gremio:%d\n", gremioWins);
    printf("Empates:%d\n", draws);
    if (interWins > gremioWins)
        printf("Inter venceu mais\n");
    else
        printf("Gremio venceu mais\n");
    return 0;
}