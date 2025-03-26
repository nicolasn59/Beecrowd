#include <stdio.h>

int main()
{
    int matrixSize, i, j, startRow, endRow, startCol, endCol, value, middleValue;
    scanf("%d", &matrixSize);
    while (matrixSize != 0)
    {
        startRow = startCol = 0;
        endRow = endCol = matrixSize - 1;
        value = 1;

        if (matrixSize % 2 == 0)
            middleValue = matrixSize / 2;
        else
            middleValue = (matrixSize + 1) / 2;

        int matrix[matrixSize][matrixSize];

        for (j = value; j <= middleValue; j++)
        {
            for (i = startCol; i <= endCol; i++)
            {
                matrix[startRow][i] = value;
                matrix[endRow][i] = value;
            }
            for (i = (startRow + 1); i < endRow; i++)
            {
                matrix[i][startCol] = value;
                matrix[i][endCol] = value;
            }
            endRow -= 1;
            startCol += 1;
            startRow += 1;
            endCol -= 1;
            value += 1;
        }

        // PRINT MATRIX
        // char tx[2];
        for (i = 0; i < matrixSize; i++)
        {
            for (j = 0; j < matrixSize; j++)
            {
                if (matrixSize == 1)
                    printf("  %d\n", matrix[i][j]);
                else if (j == matrixSize - 1)
                    printf("   %d\n", matrix[i][j]);
                else if (j == 0)
                    printf("  %d", matrix[i][j]);
                else
                    printf("   %d", matrix[i][j]);
            }
        }
        // printf("\n");
        scanf("%d", &matrixSize);
    }
    // printf("\n");
    return 0;
}
