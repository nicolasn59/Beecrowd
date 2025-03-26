#include <stdio.h>
#include <string.h>

int main()
{
    int tests, power;
    char name[100];
    scanf("%d\n", &tests);
    for (int i = 0; i < tests; i++)
    {
        scanf("%s %d", name, &power);
        if (strcmp(name, "Thor") == 0)
            printf("Y\n");
        else
            printf("N\n");
    }
    return 0;
}