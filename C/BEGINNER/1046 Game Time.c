#include <stdio.h>
 
int main() 
{
    int startHour, endHour;
    scanf("%d %d", &startHour, &endHour);
    if (startHour == endHour)
        printf("O JOGO DUROU 24 HORA(S)\n");
    else if (startHour > endHour)
        printf("O JOGO DUROU %d HORA(S)\n", (24 - (startHour - endHour)));
    else
        printf("O JOGO DUROU %d HORA(S)\n", (endHour - startHour));
    return 0;
}
