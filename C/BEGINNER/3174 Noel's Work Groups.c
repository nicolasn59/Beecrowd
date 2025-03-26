#include <stdio.h>
#include <string.h>

void produceGifts(int numberOfElves);

int main()
{
    int numberOfElves;
    scanf("%d", &numberOfElves);
    produceGifts(numberOfElves);
    return 0;
}

void produceGifts(int numElves)
{
    char name[100], profession[100];
    int workTime, sumDolls=0, sumArchitects=0, sumMusicians=0, sumDesigners=0;
    for (int i=0; i < numElves; i++)
    {
        scanf("%s %s %d", name, profession, &workTime);
        if (strcmp(profession, "bonecos") == 0)
            sumDolls += workTime;
        else if (strcmp(profession, "arquitetos") == 0)
            sumArchitects += workTime;
        else if (strcmp(profession, "musicos") == 0)
            sumMusicians += workTime;
        else
            sumDesigners += workTime;
    }
    printf("%d\n", ((sumDolls/8) + (sumArchitects/4) + (sumMusicians/6) + (sumDesigners/12)));
}
