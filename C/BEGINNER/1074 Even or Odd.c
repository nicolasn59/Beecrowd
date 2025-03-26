#include <stdio.h>

int main(int argc, char const *argv[])
{
    int numValues, value;
    scanf("%d", &numValues);
    while (numValues != 0)
    {
        scanf("%d", &value);
        if (value == 0)
            printf("NULL\n");
        else if (value % 2 == 0) // EVEN
        {
            if (value > 0) // EVEN POSITIVE
                printf("EVEN POSITIVE\n");
            else if (value < 0) // EVEN NEGATIVE
                printf("EVEN NEGATIVE\n");
        }
        else if (value % 2 != 0) // ODD
        {
            if (value > 0) // ODD POSITIVE
                printf("ODD POSITIVE\n");
            else if (value < 0) // ODD NEGATIVE
                printf("ODD NEGATIVE\n");
        }
        numValues -= 1;
    }
    return 0;
}
