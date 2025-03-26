#include <stdio.h>

int main()
{
    int password;
    while(scanf("%d", &password) != EOF)
        printf("%d\n", (password - 1));
    return 0;
}