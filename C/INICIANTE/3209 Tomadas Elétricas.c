/*
RECEBER NUM DE TESTES
INICIAR UM LOOP
    RECEBER QTD FILTRO DE LINHAS
    DEFINIR UMA FUNCAO PARA DETERMINAR QUAL APARELHOS PODEM SER CONECTADOS
    
    FUNCAO...
        INCIAR UM LOOP
            RECEBER NUMERO DE TOMADAS EM CADA FILTRO DE LINHA
        SABENDO QUE CADA FILTRO DE LINHA N-1 TOMADAS, CALCULAR O TOTAL DE APARELHOS
        QUE PODEM SER CONECTADOS

    IMPRIMIR TOTAL DE APARELHOS CONECTADOS
*/

#include <stdio.h>

void aparelhosConectados(int qtdFiltros);

int main()
{
    int numeroDeTestes, quantidadeDeFiltros;
    scanf("%d", &numeroDeTestes);
    for (int i=0; i < numeroDeTestes; i++)
    {
        scanf("%d", &quantidadeDeFiltros);
        aparelhosConectados(quantidadeDeFiltros);
    }
    return 0;
}

void aparelhosConectados(int qtdFiltros)
{
    int tomadasNoFiltro, total=0;
    for (int i=0; i < qtdFiltros; i++)
    {
        scanf("%d", &tomadasNoFiltro);
        total += (tomadasNoFiltro-1);
    }
    printf("%d\n", (total+1));
}
