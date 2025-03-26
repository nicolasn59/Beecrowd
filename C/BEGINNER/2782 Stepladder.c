# include <stdio.h>

int main()
{
    int size, count, i, sequence;
    scanf("%d", &size);
    count = 0;
    long long int ladder[size];
    for (i=0; i != size; i++)
    {
        scanf("%lld", &ladder[i]);
        if (i == 1)
        {
            sequence = (ladder[i-1] - ladder[i]);
            count += 1;
        }
        else if (i > 1)
        {
            if ((ladder[i-1] - ladder[i]) != sequence)
            {
                count += 1;
                sequence = (ladder[i-1] - ladder[i]);
            }
        }
    }
    if (count == 0)
        printf("%d\n", ++count);
    else
        printf("%d\n", count);
    return 0;
}
