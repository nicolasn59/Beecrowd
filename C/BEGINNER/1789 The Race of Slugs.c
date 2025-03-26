#include <stdio.h>

int main()
{
    int numSlugs;
    while (scanf("%d", &numSlugs) != EOF)
    {
        int slugSpeeds[numSlugs], count;
        count = 0;
        while (count != numSlugs)
            {
                scanf("%d", &slugSpeeds[count]);
                count += 1;
            }
        int fastest;
        count = 1;
        fastest = slugSpeeds[0];
        while (count != numSlugs)
        {
            if (slugSpeeds[count] > fastest)
                fastest = slugSpeeds[count];
            count += 1;
        }
        if (fastest < 10)
            printf("1\n");
        else if (fastest >= 10 && fastest < 20)
            printf("2\n");
        else
            printf("3\n");        
    }
    return 0;
}