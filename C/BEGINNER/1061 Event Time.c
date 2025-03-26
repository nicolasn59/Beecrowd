#include <stdio.h>

int main()
{
    // startDay, endDay, startHour, endHour, startMinute, endMinute, startSecond, endSecond
    int startDay, endDay, startHour, endHour, startMinute, endMinute, startSecond, endSecond;

    // resultDay, resultHour, resultMinute, resultSecond
    int resultDay, resultHour, resultMinute, resultSecond;

    char x, y; // Sem utilidade, apenas armazenamento

    scanf("%s %d", &x, &startDay);
    scanf("%d %s %d %s %d", &startHour, &x, &startMinute, &y, &startSecond);
    scanf("%s %d", &x, &endDay);
    scanf("%d %s %d %s %d", &endHour, &x, &endMinute, &y, &endSecond);

    // DAYS

    if (startHour > endHour)
        resultDay = (endDay - startDay) - 1;
    else if (startHour == endHour)
    {
        if (startMinute == endMinute)
        {
            if (startSecond <= endSecond)
                resultDay = (endDay - startDay);
        }
        else if (startMinute >= endMinute)
            resultDay = (startHour - endHour);
        else
            resultDay = (endDay - startDay);
    }

    else
        if (startHour == endHour)
        {
            if (startMinute == endMinute)
            {
                if (startSecond > endSecond)
                    resultDay = (endDay - startDay);
            }
        }
        else
            resultDay = (endDay - startDay);
    
    // HOURS 

    if (startHour > endHour)
    {
        if (startMinute >= endMinute)
            resultHour = 23 - (startHour - endHour);
        else if (endMinute > startMinute)
        {
            resultHour = 24 - (startHour - endHour);
        }
    }
    else if (startHour == endHour)
    {
        if (startMinute > endMinute)
            resultHour = 24 - (startMinute - endMinute);
        else if (startMinute == endMinute)
            resultHour = 0;
    }
    else
    {
        if (startMinute == endMinute)
            if (startSecond <= endSecond)
                resultHour = (endHour - startHour);
            else
                resultHour = 0;
        else if (startMinute > endMinute)
        {   
            if (startSecond > endSecond)
                resultHour = 23 - (endHour - startHour);
            else
                resultHour = 0;
        }
        else
            resultHour = (endHour - startHour);
    }
    
    // MINUTES

    if (startMinute > endMinute)
    {
        if (endSecond > startSecond)
        resultMinute = 60 - (startMinute - endMinute);
        else
            resultMinute = 59 - (startMinute - endMinute);
    }
    else if (startMinute == endMinute)
    {
        if (startSecond > endSecond)
            resultMinute = 60 - (startSecond - endSecond); // ACABEI DE MUDAR DE 59 PARA 60
        else if (startSecond == endSecond)
            resultMinute = (startMinute - endMinute);
        else
            resultMinute = (startMinute - endMinute);
    }
    else
        if (startSecond > endSecond)
            resultMinute = (endMinute - startMinute) - 1;
        else
            resultMinute = (endMinute - startMinute);

    // SECONDS

    if (startSecond > endSecond)
        resultSecond = 60 - (startSecond - endSecond);
    else
        resultSecond = (endSecond - startSecond);

    printf("%d dia(s)\n", resultDay);
    printf("%d hora(s)\n", resultHour);
    printf("%d minuto(s)\n", resultMinute);
    printf("%d segundo(s)\n", resultSecond);
    return 0;
}
