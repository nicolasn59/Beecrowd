#include<stdio.h>

int fat(int num);

int main()
{
    int number;
    scanf("%d", &number);
    printf("%d\n", fat(number));
    return 0;
}

int fat(int num)
{
    if (num == 1)
        return 1;
    else
        return num * fat(num-1);
}   
