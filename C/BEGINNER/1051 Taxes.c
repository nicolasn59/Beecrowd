#include <stdio.h>

int main()
{
    float salary, remaining, tax1, tax2, tax3;
    scanf("%f", &salary);
    remaining = salary;
    if (salary <= 2000.00)
        printf("Isento\n");
    else
    {
        remaining -= 2000.00;
        if (salary >= 2000.01 && salary <= 3000.00)
        {
            tax1 = remaining * (8.00 / 100.00);
            printf("R$ %.2f\n", tax1);
        }
        else if (salary >= 3000.01 && salary <= 4500.00)
        {
            tax1 = 1000.00 * (8.00 / 100.00);
            remaining -= 1000.00;
            tax2 = remaining * (18.00 / 100.00);
            printf("R$ %.2f\n", (tax1 + tax2));
        }
        else
        {
            tax1 = 1000.00 * (8.00 / 100.00);
            remaining -= 1000.00;
            tax2 = 1500.00 * (18.00 / 100.00);
            remaining -= 1500.00;
            tax3 = remaining * (28.00 / 100.00);
            printf("R$ %.2f\n", (tax1 + tax2 + tax3));
        }
    }
    return 0;
}
