#include <stdio.h>

int main() {
    int tests, year;
    scanf("%d", &tests);
    while (tests != 0)
    {
        scanf("%d", &year);
        if (year >= 2015)
        {
            printf("%d A.C.\n", (year - (2015 - 1)));
        }
        else
        {
            printf("%d D.C.\n", (2015 - year));
        }
        tests -= 1;
    }
    return 0;
}
