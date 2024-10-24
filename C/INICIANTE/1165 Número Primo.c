#include <stdio.h>

int main()
{
    int testes, num, i, primo;
    scanf("%d", &testes);
    while (testes != 0)
    {
        primo = 0;
        scanf("%d", &num);
        for (i=2; i != num; i++)
        {
            if (num % i == 0)
                primo += 1;
        }
        if (primo == 0)
            printf("%d eh primo\n", num);
        else
            printf("%d nao eh primo\n", num);
        testes -= 1;
    }
    return 0;
}
