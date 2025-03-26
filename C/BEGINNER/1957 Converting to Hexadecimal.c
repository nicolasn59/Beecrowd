#include <stdio.h>

void hex(long int n);

int main()
{
    long int num;
    scanf("%ld", &num);
    hex(num);
    return 0;
}

void hex(long int n)
{
    int len = 0; 
    int array[1000];
    while (n != 0)
    {
        array[len] = (n % 16);
        len += 1;
        n /= 16;
    }
    
    for (int i = len - 1; i >= 0; i--)
    {
        if (array[i] < 10)
            printf("%d", array[i]);
        else if (array[i] == 10)
            printf("A");
        else if (array[i] == 11)
            printf("B");
        else if (array[i] == 12)
            printf("C");
        else if (array[i] == 13)
            printf("D");
        else if (array[i] == 14)
            printf("E");
        else
            printf("F");
    }
    printf("\n");
}