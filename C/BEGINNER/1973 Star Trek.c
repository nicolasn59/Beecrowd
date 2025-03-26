#include <stdio.h>

int main () 
{
    unsigned long long numStars;
    scanf("%llu", &numStars);
    
    unsigned long long sheepInStars[numStars], count, totalSheep;
    count = totalSheep = 0;
    while (count != numStars)
    {
        scanf("%llu", &sheepInStars[count]);
        totalSheep += sheepInStars[count];
        count += 1;
    }
    unsigned long long stolenSheep, attackedStars;
    count = stolenSheep = 0;
    attackedStars = 1;
    while (count != (unsigned long long)-1 && count != numStars)
    {
        if (sheepInStars[count] == 0)
        {
            printf("%llu %llu\n", attackedStars, (totalSheep - stolenSheep));
            return 0;
        }
        else if (sheepInStars[count] % 2 != 0)
        {
            sheepInStars[count] -= 1;
            stolenSheep += 1;
            count += 1;
        }
        else
        {
            sheepInStars[count] -= 1;
            stolenSheep += 1;
            count -= 1;
        }
        if (count + 1 > attackedStars)
        {
            if (count == numStars)
                attackedStars = count;
            else
                attackedStars = count + 1;
        }
    }
    printf("%llu %llu\n", attackedStars, (totalSheep - stolenSheep));
    return 0;
}