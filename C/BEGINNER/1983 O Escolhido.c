#include <stdio.h>

int main() {
    int alunos;
    long int matricula, aprovado;
    float nota, maior=0;
    scanf("%d", &alunos);
    while (alunos != 0)
    {
        scanf("%ld %f", &matricula, &nota);
        if (maior < nota)
        {
            maior = nota;
            aprovado = matricula;
        }
        alunos -= 1;
    }
    if (maior < 8)
        printf("Minimum note not reached\n");
    else
        printf("%ld\n", aprovado);
    return 0;
}
