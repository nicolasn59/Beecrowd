#include <stdio.h>

int main()
{
    int numberOfQuestions, answer;
    scanf("%d", &numberOfQuestions);
    for (int i=1; i <= numberOfQuestions; i++)
    {
        scanf("%d", &answer);
        printf("resposta %d: %d\n", i, answer);
    }
    return 0;
}
