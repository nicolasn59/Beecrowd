#include <stdio.h>

void sumResult(int numTerms)
{
    int sum = 0;
    for (int i = 0; i < numTerms; i++)
    {
        if (sum == 0)
            sum += 1;
        else
            sum -= 1;
    }
    printf("%d\n", sum);
}

int main()
{
    int numTests, terms;
    scanf("%d", &numTests);
    for (int i = 0; i < numTests; i++)
    {
        scanf("%d", &terms);
        sumResult(terms);
    }
    return 0;
}