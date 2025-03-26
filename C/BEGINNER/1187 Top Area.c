#include <stdio.h>

int main()
{
    int i, j, mainDiagonal, secondaryDiagonal;
    char operation[2];
    double matrix[12][12], sum, count;
    scanf("%s ", operation);
    for (i = 0; i < 12; i++)
        for (j = 0; j < 12; j++)
            scanf("%lf", &matrix[i][j]);
    mainDiagonal = 0;
    secondaryDiagonal = 11;
    sum = count = 0;
    for (i = 0; i < 12; i++)
    {
        for (j = 0; j < 12; j++)
        {
            if (j > mainDiagonal && j < secondaryDiagonal && i < 5)
            {
                sum += matrix[i][j];
                count += 1.0;
            }
        }
        mainDiagonal += 1;
        secondaryDiagonal -= 1;
    }
    if (operation[0] == 'S')
        printf("%.1lf\n", sum);
    else
        printf("%.1lf\n", (sum / count));
    return 0;
}