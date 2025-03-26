#include <stdio.h>

void DidNotReturn(int divers[], int survivors[], int numDivers, int numSurvivors);

int main()
{
    int numDivers, numSurvivors;
    while (scanf("%d %d", &numDivers, &numSurvivors) != EOF)
    {
        int divers[numDivers], survivors[numSurvivors];
        for (int i = 0; i < numSurvivors; i++)
            scanf("%d", &survivors[i]);
        if (numDivers == numSurvivors)
            printf("*\n");
        else
        {
            for (int i = 0; i < numDivers; i++)
                divers[i] = i + 1;
            DidNotReturn(divers, survivors, numDivers, numSurvivors);
        }
    }
    return 0;
}

void DidNotReturn(int divers[], int survivors[], int numDivers, int numSurvivors)
{
    for (int i = 0; i < numSurvivors; i++)
        for (int j = 0; j < numDivers; j++)
            if (survivors[i] == divers[j])
                divers[j] = 0;
    for (int i = 0; i < numDivers; i++)
        if (divers[i] > 0)
            printf("%d ", divers[i]);
    printf("\n");
}
