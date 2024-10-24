#include <stdio.h>
int main()
{
    int A, B, C, D;
    scanf("%d %d %d %d", &A, &B, &C, &D);
    if (((A < B+C) && (B < C+A) && (C < A+B)) || ((A < B+D) && (B < A+D) && (D < A+B)) || ((A < C+D) && (C < A+D) && (D < A+C)) || ((B < C+D) && (C < B+D) && (D < B+C)))
    {
        printf("S\n");
    }
    else
    {
        printf("N\n");
    }
    return 0;
}
