#include <stdio.h>
#include <string.h>

void lottery();

int main()
{
    lottery();
    return 0;
}

void lottery()
{
    char crow[10];
    int sum = 0, countShouts = 0;
    while (countShouts != 3)
    {
        fgets(crow, sizeof(crow), stdin);
        if (strcmp(crow, "caw caw\n") == 0)
        {   
            printf("%d\n", sum);
            sum = 0;
            countShouts += 1;
        }
        else if (strcmp(crow, "--*\n") == 0)
        {
            sum += 1;
        }
        else if (strcmp(crow, "-*-\n") == 0)
        {
            sum += 2;
        }
        else if (strcmp(crow, "-**\n") == 0)
        {
            sum += 3;
        }
        else if (strcmp(crow, "*--\n") == 0)
        {
            sum += 4;
        }
        else if (strcmp(crow, "*-*\n") == 0)
        {
            sum += 5;
        }
        else if (strcmp(crow, "**-\n") == 0)
        {
            sum += 6;
        }
        else
        {
            sum += 7;
        }
    }
    return;
}