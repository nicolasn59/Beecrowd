#include <stdio.h>
int main()
{
    int numPeople;
    scanf("%d", &numPeople);
    int possibleExecutors[numPeople], count, bestChoice, min;
    count = 0;
    while (count != numPeople)
    {
        scanf("%d", &possibleExecutors[count]);
        count += 1;
    }
    bestChoice = 1;
    min = possibleExecutors[0];
    count = 1;
    while (count != numPeople)
    {
        if (possibleExecutors[count] < min)
        {
            min = possibleExecutors[count];
            bestChoice = count + 1;
        }

        count += 1;
    }
    printf("%d\n", bestChoice);
    return 0;
}