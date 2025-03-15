#include <stdio.h>
#include <string.h>

void limparBuffer()
{
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

void resolverExpressoes(int ind, int num1, int num2, int *somatorio, int *subtratorio, int *produtorio)
{
    somatorio[ind] = (num1 + num2);
    subtratorio[ind] = (num1 - num2);
    produtorio[ind] = (num1 * num2);
}

int anotarPerdedores(char name[], char listaDePerdedores[][51], int pos)
{
    int len=0;
    for (int k=0; name[k] != '\0'; k++)
    {
        listaDePerdedores[pos][k] = name[k];
        len += 1;
    }
    listaDePerdedores[pos][len] = '\0';
    pos += 1;
    return pos;
}

void ordenaStrings(char listaDePerdedores[][51], int pos)
{
    int r;
    char auxiliar[51];
    // DIMINUI -1 DA POSICAO, PORQUE O INDICE COMEÇA EM 0 E A POSICAO É A QUANTIDADE DE PERDEDORES, ENTAO O VALOR DELA É IGUAL A 2
    for (int i=0; i <= (pos-1); i++)
    {
        for (int j=i+1; j <= (pos-1); j++)
        { 
            r = (strcmp(listaDePerdedores[i], listaDePerdedores[j]));
            if (r > 0)
            {
                strcpy(auxiliar, listaDePerdedores[i]);
                strcpy(listaDePerdedores[i], listaDePerdedores[j]);
                strcpy(listaDePerdedores[j], auxiliar);
            }
        }
    }
}

int main()
{
   int quantidadeDeExpressoes;
   while (scanf("%d", &quantidadeDeExpressoes) != EOF)
   {
        int numero1, numero2, indice, resultados[quantidadeDeExpressoes], resposta;
        int soma[quantidadeDeExpressoes], subtracao[quantidadeDeExpressoes], produto[quantidadeDeExpressoes];
        char igualdade;
        indice = 0;
        while (indice < quantidadeDeExpressoes)
        {
            scanf("%d %d %c %d", &numero1, &numero2, &igualdade, &resposta);
            resolverExpressoes(indice, numero1, numero2, soma, subtracao, produto);
            resultados[indice] = resposta;
            indice += 1;
        }

        char nome[51], perdedores[51][51], operador;
        int indiceDoJogador, i=0, acertos=0, erros=0, posicao=0;
        while (i < quantidadeDeExpressoes)
        {
            scanf("%s %d %c", nome, &indiceDoJogador, &operador);
            limparBuffer();
            if (operador == '+')
            {
                if ((soma[indiceDoJogador-1]) == resultados[indiceDoJogador-1])
                    acertos += 1;
                else
                {
                    erros += 1;
                    posicao = anotarPerdedores(nome, perdedores, posicao);
                }
            }
            else if (operador == '-')
            {
                if ((subtracao[indiceDoJogador-1] == resultados[indiceDoJogador-1]))
                    acertos += 1;
                else
                {
                    erros += 1;
                    posicao = anotarPerdedores(nome, perdedores, posicao);
                }
            }
            else if (operador == '*')
            {
                if ((produto[indiceDoJogador-1]) == resultados[indiceDoJogador-1])
                    acertos += 1;
                else
                {
                    erros += 1;
                    posicao = anotarPerdedores(nome, perdedores, posicao);
                }
            }
            else if (operador == 'I')
            {
                if ((soma[indiceDoJogador-1] != resultados[indiceDoJogador-1]) && (subtracao[indiceDoJogador-1] != resultados[indiceDoJogador-1]) && (produto[indiceDoJogador-1] != resultados[indiceDoJogador-1]))
                    acertos += 1;
                else
                {
                    erros += 1;
                    posicao = anotarPerdedores(nome, perdedores, posicao);
                }
            }
            i += 1;
        }
        if (acertos == quantidadeDeExpressoes)
            printf("You Shall All Pass!\n");
        else if (erros == quantidadeDeExpressoes)
            printf("None Shall Pass!\n");
        else
        {
            ordenaStrings(perdedores, posicao);
            for (int i=0; i < posicao; i++)
            {
                if (i != (posicao-1))
                    printf("%s ", perdedores[i]);
                else
                    printf("%s\n", perdedores[i]);
            }
        }
   }
   return 0;
}
