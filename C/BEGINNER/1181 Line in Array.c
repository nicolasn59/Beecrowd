#include <stdio.h>
int main()
{
    int operationLine, i, j;
    char operation[2];
    double matrix[12][12], sum;
    sum = 0;
    scanf("%d %s", &operationLine, operation);
    for (i = 0; i < 12; i++)
        for (j = 0; j < 12; j++)
            scanf("%lf", &matrix[i][j]);
    for (i = 0; i < 12; i++)
        for (j = 0; j < 12; j++)
            if (i == operationLine)
                sum += matrix[i][j];
    if (operation[0] == 'S')
        printf("%.1lf\n", sum);
    else
        printf("%.1lf\n", (sum / 12.0));
    return 0;
}
