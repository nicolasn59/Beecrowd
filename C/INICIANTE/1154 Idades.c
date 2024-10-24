#include <stdio.h>
int main()
{
    double idade=0, contarIdades=0, somarIdades=0, media;
    while (idade >= 0)
        {
            scanf("%lf", &idade);
            if (idade >= 0)
            {
                somarIdades += idade;
                contarIdades += 1.00;
            }
        }
    media = (somarIdades/contarIdades);
    printf("%.2lf\n", media);
    return 0;
}
