#include <stdio.h>
#include <string.h>

int main()
{
    int tests, numP1, numP2;
    char nameP1[101], choiceP1[6], nameP2[101], choiceP2[6];
    scanf("%d", &tests);
    for (int i = 0; i < tests; i++)
    {
        scanf("%s\n %s\n %s\n %s\n", nameP1, choiceP1, nameP2, choiceP2);
        scanf("%d %d", &numP1, &numP2);
        if ((numP1 + numP2) % 2 == 0)
        {
            if (strcmp(choiceP1, "PAR") == 0)
                printf("%s\n", nameP1);
            else
                printf("%s\n", nameP2);
        }
        else
        {
            if (strcmp(choiceP1, "IMPAR") == 0)
                printf("%s\n", nameP1);
            else
                printf("%s\n", nameP2);
        } 
    }
    return 0;
}