#include <stdio.h>

void NaoVoltaram(int mergulharam[], int sobreviventes[], int numDeMergulhadores, int numDeSobreviventes);

int main()
{
    int numeroDeMergulhadores, numeroDeSobreviventes;
    while (scanf("%d %d", &numeroDeMergulhadores, &numeroDeSobreviventes) != EOF)
    {
        int mergulhadores[numeroDeMergulhadores], vivos[numeroDeSobreviventes];
        for (int i=0; i < numeroDeSobreviventes; i++)
            scanf("%d", &vivos[i]);
        if (numeroDeMergulhadores == numeroDeSobreviventes)
            printf("*\n");
        else
        {
            for (int i=0; i < numeroDeMergulhadores; i++)
                mergulhadores[i] = i+1;
            NaoVoltaram(mergulhadores, vivos, numeroDeMergulhadores, numeroDeSobreviventes);
        }
    }
    return 0;
}

void NaoVoltaram(int mergulharam[], int sobreviventes[], int numDeMergulhadores, int numDeSobreviventes)
{
    for (int i=0; i < numDeSobreviventes; i++)
        for (int j=0; j < numDeMergulhadores; j++)
            if (sobreviventes[i] == mergulharam[j])
                mergulharam[j] = 0;
    for (int i=0; i < numDeMergulhadores; i++)
        if (mergulharam[i] > 0)
            printf("%d ", mergulharam[i]);
    printf("\n");
}
