#include <stdio.h>

int main()
{
    int cont=1, golsInter, golsGremio, grenal, empates=0, vitoriasInter=0, vitoriasGremio=0, somaDeGrenais=0;
    while (cont == 1)
    {

        scanf("%d %d", &golsInter, &golsGremio);
        if (golsInter > golsGremio)
            vitoriasInter += 1;
        else if (golsGremio > golsInter)
            vitoriasGremio += 1;
        else
            empates += 1;
        
        printf("Novo grenal (1-sim 2-nao)\n");
        scanf("%d", &grenal);
        if (grenal == 2)
            cont = 0;
        somaDeGrenais += 1;
    }
    printf("%d grenais\n", somaDeGrenais);
    printf("Inter:%d\n", vitoriasInter);
    printf("Gremio:%d\n", vitoriasGremio);
    printf("Empates:%d\n", empates);
    if (vitoriasInter > vitoriasGremio)
        printf("Inter venceu mais\n");
    else
        printf("Gremio venceu mais\n");
    return 0;
}
