#include <stdio.h>

int main()
{
    int sequence, end, count = 1, lineBreak, stopLoop;
    scanf("%d %d", &sequence, &end);
    stopLoop = end;
    lineBreak = sequence;
    while (stopLoop != 0)
    {   
        if (lineBreak == 1)
            printf("%d\n", count);
        else
            printf("%d ", count);
        lineBreak -= 1;
        count += 1;
        stopLoop -= 1;
        if (lineBreak == 0)
            lineBreak = sequence;
    }
    return 0;
}