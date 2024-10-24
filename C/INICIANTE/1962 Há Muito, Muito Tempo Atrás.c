#include <stdio.h>

int main() {
    int testes, ano;
    scanf("%d", &testes);
    while (testes != 0)
    {
        scanf("%d", &ano);
        if (ano >= 2015)
        {
            printf("%d A.C.\n", (ano - (2015-1)));
        }
        else
        {
            printf("%d D.C.\n", (2015-ano));
        }
        testes -= 1;
    }
    return 0;
}
