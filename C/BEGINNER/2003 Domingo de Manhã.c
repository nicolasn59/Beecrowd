#include <stdio.h>

int main()
{
    int horas, minutos;
    char pontos;
    while (scanf("%d %c %d", &horas, &pontos, &minutos) != EOF)
    {
        int atraso = 0;
        if (((horas <= 7) && (minutos == 0)) || (horas < 7))
        {
            printf("Atraso maximo: 0\n");
        }
        else
        {
            if (horas == 9)
                printf("Atraso maximo: %d\n", (60*2));
            else if (horas == 8)
                printf("Atraso maximo: %d\n", (60+minutos));    
            else
                printf("Atraso maximo: %d\n", (minutos));
        }
    }
    return 0;
}
