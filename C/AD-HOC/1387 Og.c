#include<stdio.h>

int main()
{
    int filhos, filhas;
    scanf("%d %d", &filhos, &filhas);
    while ((filhos != 0) && (filhas != 0))
    {
        printf("%d\n", (filhos + filhas));
        scanf("%d %d", &filhos, &filhas);
    }
    return 0;
}
