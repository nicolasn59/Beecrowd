#include <stdio.h>

int main()
{
    char word[21];
    int len;
    fgets(word, 21, stdin);
    for (int i=0; word[i] != '\0'; i++)
        len += 1;
    if (len > 10)
        printf("palavrao\n");
    else
        printf("palavrinha\n");
    return 0;
}
