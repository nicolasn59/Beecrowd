#include <stdio.h>
int main()
{
    int numCaracteres, cont;
    char frase[] = "xLIFE IS NOT A PROBLEM TO BE SOLVED";
    scanf("%d", &numCaracteres);
    for (cont=1; cont < numCaracteres; cont++)
    {
        printf("%c", frase[cont]);
    }
    printf("%c\n", frase[numCaracteres]);
    return 0;
}
