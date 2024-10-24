#include <stdio.h>

void apertosMinimos(unsigned long int qtdAndares, unsigned long int atual, unsigned long int destino, unsigned long int subir, unsigned long int descer);

int main()
{
    unsigned long int quantidadeDeAndares, andarAtual, andarDestino, subida, descida;
    scanf("%lu %lu %lu %lu %lu", &quantidadeDeAndares, &andarAtual, &andarDestino, &subida, &descida);
    apertosMinimos(quantidadeDeAndares, andarAtual, andarDestino, subida, descida);
    return 0;
}

void apertosMinimos(unsigned long int qtdAndares, unsigned long int atual, unsigned long int destino, unsigned long int subir, unsigned long int descer)
{
    unsigned long int cont=0;
    for (unsigned long int i = 0; i <= qtdAndares; i++)
    {
        if (atual == destino)
        {
            printf("%lu\n", cont);
            return;
        }
        else if (atual < destino)
        {
            if (subir == 0)
            {
                printf("use the stairs\n");
                return;
            }
            else
            {
                atual += subir;
                cont += 1;
            }
        }
        else
        {
            if (descer == 0)
            {
                printf("use the stairs\n");
                return;     
            }
            else
            {
                atual -= descer;
                cont += 1;
            }
        }
    }
    printf("use the stairs\n");
}
