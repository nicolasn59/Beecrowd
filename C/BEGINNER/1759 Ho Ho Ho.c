#include <stdio.h>

int main()
{
    int numHos;
    scanf("%d", &numHos);
    while (numHos != 0)
    {
        if (numHos > 1)
            printf("Ho ");
        else
            printf("Ho!\n");
        numHos -= 1;
    }
    return 0;
}
