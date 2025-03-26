#include <stdio.h>

int main()
{
    int sequenceNum, count, caseNum, i, j;
    caseNum = 1;
    while (scanf("%d", &sequenceNum) != EOF)
    {
        if (sequenceNum == 0)
        {
            printf("Caso %d: 1 numero\n", caseNum);
            printf("0\n");
        }
        else if (sequenceNum == 1)
        {
            printf("Caso %d: 2 numeros\n", caseNum);
            printf("0 1\n");
        }
        else
        {
            count = 1;
            for (i = 1; i <= sequenceNum; i++)
            {
                for (j = i; j != 0; j--)
                {
                    count += 1;
                }
            }
            printf("Caso %d: %d numeros\n", caseNum, count);
            printf("0 ");
            for (i = 1; i <= sequenceNum; i++)
            {
                for (j = i; j != 0; j--)
                {
                    if ((j == 1) && (i == sequenceNum))
                        break;
                    printf("%d ", i);
                }
            }
            printf("%d\n", sequenceNum);
        }
        printf("\n");
        caseNum += 1;
    }
    return 0;
}
