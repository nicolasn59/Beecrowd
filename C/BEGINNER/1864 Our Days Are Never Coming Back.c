#include <stdio.h>
int main()
{
    int numChars, count;
    char phrase[] = "xLIFE IS NOT A PROBLEM TO BE SOLVED";
    scanf("%d", &numChars);
    for (count = 1; count < numChars; count++)
    {
        printf("%c", phrase[count]);
    }
    printf("%c\n", phrase[numChars]);
    return 0;
}