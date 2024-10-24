#include <stdio.h>
#include <math.h>

int main()
{
    double money;
    scanf("%lf", &money);
    money *= 100;
    printf("NOTAS:\n");
    printf("%.0lf nota(s) de R$ 100.00\n", floor(money / 10000));
    printf("%0.lf nota(s) de R$ 50.00\n", floor(fmod(money, 10000) / 5000));
    printf("%0.lf nota(s) de R$ 20.00\n", floor(fmod(fmod(money, 10000), 5000) / 2000));
    printf("%.0lf nota(s) de R$ 10.00\n", floor(fmod(fmod(fmod(money, 10000), 5000), 2000) / 1000));
    printf("%.0lf nota(s) de R$ 5.00\n", floor(fmod(fmod(fmod(fmod(money, 10000) , 5000), 2000), 1000) / 500));
    printf("%.0lf nota(s) de R$ 2.00\n", floor(fmod(fmod(fmod(fmod(fmod(money, 10000), 5000), 2000), 1000), 500) / 200));
    printf("MOEDAS:\n");
    printf("%.0lf moeda(s) de R$ 1.00\n", floor(fmod(fmod(fmod(fmod(fmod(fmod(money, 10000), 5000), 2000), 1000), 500), 200) / 100));
    printf("%.0lf moeda(s) de R$ 0.50\n", floor(fmod(fmod(fmod(fmod(fmod(fmod(fmod(money, 10000), 5000), 2000), 1000), 500), 200), 100) / 50));
    printf("%.0lf moeda(s) de R$ 0.25\n", floor(fmod(fmod(fmod(fmod(fmod(fmod(fmod(fmod(money, 10000), 5000), 2000), 1000), 500), 200), 100), 50) / 25));
    printf("%.0lf moeda(s) de R$ 0.10\n", floor(fmod(fmod(fmod(fmod(fmod(fmod(fmod(fmod(fmod(money, 10000), 5000), 2000), 1000), 500), 200), 100), 50), 25) / 10));
    printf("%.0lf moeda(s) de R$ 0.05\n", floor(fmod(fmod(fmod(fmod(fmod(fmod(fmod(fmod(fmod(fmod(money, 10000), 5000), 2000), 1000), 500), 200), 100), 50), 25), 10) / 5));
    printf("%.0lf moeda(s) de R$ 0.01\n", floor(fmod(fmod(fmod(fmod(fmod(fmod(fmod(fmod(fmod(fmod(fmod(money, 10000), 5000), 2000), 1000), 500), 200), 100), 50), 25), 10), 5) / 1));
    
    return 0;
}
