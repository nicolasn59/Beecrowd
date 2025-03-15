#include <stdio.h>

int main(int argc, char const *argv[])
{
    int seconds, minutes, hours;
    scanf("%d", &seconds);

    hours = seconds / 3600;
    minutes = seconds / 60 % 60;
    seconds = seconds % 60;

    printf("%d:%d:%d\n", hours, minutes, seconds);
    return 0;
}
