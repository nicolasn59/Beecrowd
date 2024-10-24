#include <stdio.h>

int main()
{
    int numDeHo;
    scanf("%d", &numDeHo);
    while (numDeHo != 0)
    {
        if (numDeHo > 1)
            printf("Ho ");
        else
            printf("Ho!\n");
        numDeHo -= 1;
    }
    return 0;
}
