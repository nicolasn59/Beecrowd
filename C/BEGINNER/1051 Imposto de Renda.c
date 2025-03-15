#include <stdio.h>

int main()
{
    float salario, cont, imposto1, imposto2, imposto3;
    scanf("%f", &salario);
    cont = salario;
    if (salario <= 2000.00)
        printf("Isento\n");
    else
    {
        cont -= 2000.00;
        if (salario >= 2000.01 && salario <= 3000.00)
        {
            imposto1 = cont * (8.00/100.00);
            printf("R$ %.2f\n", imposto1);
        }
        else if (salario >= 3000.01 && salario <= 4500.00)
        {
            imposto1 = 1000.00 * (8.00/100.00);
            cont -= 1000.00;
            imposto2 = cont * (18.00/100.00);
            printf("R$ %.2f\n", (imposto1 + imposto2));
        }
        else
        {
            imposto1 = 1000.00 * (8.00/100.00);
            cont -= 1000.00;
            imposto2 = 1500.00 * (18.00/100.00);
            cont -= 1500.00;
            imposto3 = cont * (28.00/100.00);
            printf("R$ %.2f\n", (imposto1 + imposto2 + imposto3));
        }
    }
    return 0;
}
