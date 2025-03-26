#include <stdio.h>

int main()
{
    // start hour, start minute, end hour, end minute, result hour, result minute
    int startHour, startMinute, endHour, endMinute, resultHour, resultMinute;
    scanf("%d %d %d %d", &startHour, &startMinute, &endHour, &endMinute);
    
    // HOURS
    if (endHour > startHour)
    {
        if (endMinute >= startMinute)
            resultHour = (endHour - startHour);
        else if (startMinute > endMinute)
            resultHour = (endHour - startHour) - 1;
    }
    else if (startHour > endHour)
    {
        if (endMinute >= startMinute)
            resultHour = (24 - (startHour - endHour));
        else if (startMinute > endMinute)
            resultHour = (23 - (startHour - endHour));
    }
    else
    {
        if (endMinute > startMinute)
            resultHour = (endHour - startHour);
        else if (startMinute > endMinute)
            resultHour = (23 - (endHour - startHour));
        else
            resultHour = 24;
    }

    // MINUTES
    if (endMinute >= startMinute)
        resultMinute = (endMinute - startMinute);
    else
        resultMinute = (60 - (startMinute - endMinute));

    printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", resultHour, resultMinute);
    return 0;
}
