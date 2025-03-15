#include <stdio.h>
 
int main() 
{
    int hi, hf;
    scanf("%d %d", &hi, &hf);
    if (hi == hf)
        printf("O JOGO DUROU 24 HORA(S)\n");
    else if (hi > hf)
        printf("O JOGO DUROU %d HORA(S)\n", (24 - (hi - hf)));
    else
        printf("O JOGO DUROU %d HORA(S)\n", (hf - hi));
    return 0;
}
