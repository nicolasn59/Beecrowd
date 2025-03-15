#include<stdio.h>
#include <stdlib.h>

float calcularMedia(float *notasDosAlunos, float qtdAlunos);
int alunosAcimaDaMedia(float *notasDosAlunos, float qtdAlunos, float mediaDasNotas);

int main()
{
    int turmas; //Quantidade dd casos de testes
    scanf("%d", &turmas);
    while (turmas != 0)
    {
        float *notas, alunos;
        scanf("%f", &alunos);
        notas = (float*) malloc(alunos*sizeof(float));
        for(int i=0; i < alunos; i++)
            scanf("%f", &notas[i]);
        float media;    
        media = calcularMedia(notas, alunos);
        alunosAcimaDaMedia(notas, alunos, media);
        free(notas);
        turmas -= 1;
    }
    return 0;
}

float calcularMedia(float *notasDosAlunos, float qtdAlunos)
{
    float somaDasNotas=0;
    for (int i=0; i < qtdAlunos; i++)
        somaDasNotas += notasDosAlunos[i];
    return (somaDasNotas/qtdAlunos);    
}

int alunosAcimaDaMedia(float *notasDosAlunos, float qtdAlunos, float mediaDasNotas)
{
    float contador=0; // contar alunos acima da media
    for (int i=0; i < qtdAlunos; i++)
    {
        if (notasDosAlunos[i] > mediaDasNotas)
            contador += 1;
    }
    printf("%.3f%%\n", ((100.0*contador)/qtdAlunos));
    return 0;
}
