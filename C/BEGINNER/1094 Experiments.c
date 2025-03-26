#include <stdio.h>

int main()
{
    int numExperiments;
    float rabbits = 0, rats = 0, frogs = 0, totalAnimals, numAnimals;
    char animal[2], msg = '%';
    scanf("%d", &numExperiments);
    while (numExperiments != 0)
    {
        scanf("%f %s", &numAnimals, animal);
        if (animal[0] == 'C')
            rabbits += numAnimals;
        else if (animal[0] == 'R')
            rats += numAnimals;
        else
            frogs += numAnimals;
        numExperiments -= 1;
    }
        totalAnimals = (rabbits + rats + frogs);
        printf("Total: %.0f cobaias\n", totalAnimals);
        printf("Total de coelhos: %.0f\n", rabbits);
        printf("Total de ratos %.0f\n", rats);
        printf("Total de sapos: %.0f\n", frogs);
        printf("Percentual de coelhos: %.2f %c\n", ((100.00 * rabbits) / totalAnimals), msg);
        printf("Percentual de ratos: %.2f %c\n", ((100.00 * rats) / totalAnimals), msg);
        printf("Percentual de sapos: %.2f %c\n", ((100.00 * frogs) / totalAnimals), msg);
    return 0;
}
