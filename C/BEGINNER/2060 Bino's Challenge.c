#include <stdio.h>

void checkMultiples(int listLength, int list[]);

int main()
{
    int length;
    scanf("%d", &length);
    int list[length];
    for (int i = 0; i < length; i++)
    {
        scanf("%d", &list[i]);
    }
    checkMultiples(length, list);
    return 0;
}

void checkMultiples(int listLength, int list[])
{
    int multiplesOfTwo = 0, multiplesOfThree = 0, multiplesOfFour = 0, multiplesOfFive = 0;
    for (int i = 0; i < listLength; i++)
    {
        if ((list[i] % 2) == 0)
            multiplesOfTwo += 1;
        if ((list[i] % 3) == 0)
            multiplesOfThree += 1;
        if ((list[i] % 4) == 0)
            multiplesOfFour += 1;
        if ((list[i] % 5) == 0)
            multiplesOfFive += 1;
    }
    printf("%d Multiplo(s) de 2\n", multiplesOfTwo);
    printf("%d Multiplo(s) de 3\n", multiplesOfThree);
    printf("%d Multiplo(s) de 4\n", multiplesOfFour);
    printf("%d Multiplo(s) de 5\n", multiplesOfFive);
}
