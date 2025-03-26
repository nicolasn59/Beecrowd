#include <stdio.h>

int main()
{
    int size;
    scanf("%d", &size);
    if (size % 2 == 0)
        printf("%d casas brancas e %d casas pretas\n", (size*(size/2)), (size*(size/2)));
    else
        printf("%d casas brancas e %d casas pretas\n", (((size*size)/2)+1), ((size*size)/2));
    return 0;
}
