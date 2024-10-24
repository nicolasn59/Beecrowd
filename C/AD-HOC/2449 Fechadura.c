#include <stdio.h>
#include <math.h>

int main()
{
    int numDePinos, alturaIdeal;
    scanf("%d %d", &numDePinos, &alturaIdeal);
    int altura[numDePinos];
    for (int i=0; i < numDePinos; i++)
        scanf("%d", &altura[i]);
    int total=0;
    for (int i=1; i < numDePinos; i++)
    {
        if (alturaIdeal >= altura[i-1])
            altura[i] += alturaIdeal - altura[i-1];
        else
            altura[i] -= altura[i-1] - alturaIdeal;
        total += abs(alturaIdeal - altura[i-1]);
    }
    printf("%d\n", total);
    return 0;
}
