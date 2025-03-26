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
    sum = count = 0;
    mainDiagonal = 0;
    secondaryDiagonal = 11;
    for (i = 0; i < 12; i++)
    {
        for (j = 0; j < 12; j++)
        {
            if (i < 6 && j < mainDiagonal)
            {
                sum += matrix[i][j];
                count += 1.0;
            }
            else if (i > 5 && j < secondaryDiagonal)
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