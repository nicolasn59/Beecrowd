#include <stdio.h>

int main()
{
    int complaint;
    
    while (scanf("%d", &complaint) != EOF)
    {
        if (complaint == 0)
            printf("vai ter copa!\n");
        else
            printf("vai ter duas!\n");
    }
    return 0;
}
