#include <stdio.h>

int main()
{
    int qtdCursos;
    char nomeDoCurso[101];
    scanf("%d\n", &qtdCursos);
    for (int i=0; i != (qtdCursos-1); i++)
    {
        scanf("%s\n", nomeDoCurso);
    }
    printf("Ciencia da Computacao\n");
    return 0;
}
