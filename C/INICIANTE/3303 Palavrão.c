#include <stdio.h>

int main()
{
    char palavra[21];
    int len;
    fgets(palavra, 21, stdin);
    for (int i=0; palavra[i] != '\0'; i++)
        len += 1;
    if (len > 10)
        printf("palavrao\n");
    else
        printf("palavrinha\n");
    return 0;
}
