#include <stdio.h>
int main()
{
    double age = 0, countAges = 0, sumAges = 0, average;
    while (age >= 0)
        {
            scanf("%lf", &age);
            if (age >= 0)
            {
                sumAges += age;
                countAges += 1.00;
            }
        }
    average = (sumAges / countAges);
    printf("%.2lf\n", average);
    return 0;
}