#include <stdio.h>

int main()
{
    int numDeMensagens, cont, tamanhoMsg, i, j;
    char mensagem[1001], mensagemInv[1001];
    scanf("%d ", &numDeMensagens);
    while (numDeMensagens != 0)
    {
        fgets(mensagem, 1001, stdin);
        tamanhoMsg = 0;
        while (mensagem[tamanhoMsg] != '\0' && mensagem[tamanhoMsg] != '\n') // CONTAR CARACTERES DA MSG
            tamanhoMsg += 1;
        for (cont = 0; cont != tamanhoMsg; cont++) // PRIMEIRA PASSADA
        {
            if ((mensagem[cont] >= 'a' && mensagem[cont] <= 'z') || (mensagem[cont] >= 'A' && mensagem[cont] <= 'Z'))
                mensagem[cont] = mensagem[cont] + 3;
        }
        // SEGUNDA PASSADA
        i = tamanhoMsg-1; // ELIMINANDO O \0
        j = 0;
        while (j < tamanhoMsg)
        {
            mensagemInv[j] = mensagem[i];
            i -= 1;
            j += 1;
        }
        mensagemInv[tamanhoMsg]='\0';
        for (cont=tamanhoMsg-1; cont >= (tamanhoMsg/2); cont--)
        {
            mensagemInv[cont] -= 1;
        }
        printf("%s\n", mensagemInv);
        numDeMensagens -= 1;
    }
    return 0;
}
