#include <stdio.h>

int main()
{
    int hours, minutes;
    char colon;
    while (scanf("%d %c %d", &hours, &colon, &minutes) != EOF)
    {
        int delay = 0;
        if (((hours <= 7) && (minutes == 0)) || (hours < 7))
        {
            printf("Atraso maximo: 0\n");
        }
        else
        {
            if (hours == 9)
                printf("Atraso maximo: %d\n", (60 * 2));
            else if (hours == 8)
                printf("Atraso maximo: %d\n", (60 + minutes));    
            else
                printf("Atraso maximo: %d\n", (minutes));
        }
    }
    return 0;
}
