#include <stdio.h>
#include <string.h>

void clearBuffer()
{
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

void solveExpressions(int index, int num1, int num2, int *sum, int *subtraction, int *product)
{
    sum[index] = (num1 + num2);
    subtration[index] = (num1 - num2);
    product[index] = (num1 * num2);
}

int noteLosers(char name[], char listOfLosers[][51], int pos)
{
    int len=0;
    for (int k=0; name[k] != '\0'; k++)
    {
        listOfLosers[pos][k] = name[k];
        len += 1;
    }
    listOfLosers[pos][len] = '\0';
    pos += 1;
    return pos;
}

void sortStrings(char listOfLosers[][51], int pos)
{
    int r;
    char aux[51];
    // SUBTRACT 1 FROM POSITION, BECAUSE THE INDEX STARTS AT 0 AND THE POSITION IS THE NUMBER OF LOSERS, SO ITS VALUE IS EQUAL TO 2
    for (int i=0; i <= (pos-1); i++)
    {
        for (int j=i+1; j <= (pos-1); j++)
        { 
            r = (strcmp(listOfLosers[i], listOfLosers[j]));
            if (r > 0)
            {
                strcpy(aux, listOfLosers[i]);
                strcpy(listOfLosers[i], listOfLosers[j]);
                strcpy(listOfLosers[j], aux);
            }
        }
    }
}

int main()
{
   int numberOfExpressions;
   while (scanf("%d", &numberOfExpressions) != EOF)
   {
        int num1, num2, index, results[numberOfExpressions], answer;
        int sum[numberOfExpressions], subtration[numberOfExpressions], product[numberOfExpressions];
        char equality;
        index = 0;
        while (index < numberOfExpressions)
        {
            scanf("%d %d %c %d", &num1, &num2, &equality, &answer);
            solveExpressions(index, num1, num2, sum, subtration, product);
            results[index] = answer;
            index += 1;
        }

        char name[51], losers[51][51], operator;
        int playerIndex, i=0, correct=0, errors=0, position=0;
        while (i < numberOfExpressions)
        {
            scanf("%s %d %c", name, &playerIndex, &operator);
            clearBuffer();
            if (operator == '+')
            {
                if ((sum[playerIndex-1]) == results[playerIndex-1])
                    correct += 1;
                else
                {
                    errors += 1;
                    position = noteLosers(name, losers, position);
                }
            }
            else if (operator == '-')
            {
                if ((subtration[playerIndex-1] == results[playerIndex-1]))
                    correct += 1;
                else
                {
                    errors += 1;
                    position = noteLosers(name, losers, position);
                }
            }
            else if (operator == '*')
            {
                if ((product[playerIndex-1]) == results[playerIndex-1])
                    correct += 1;
                else
                {
                    errors += 1;
                    position = noteLosers(name, losers, position);
                }
            }
            else if (operator == 'I')
            {
                if ((sum[playerIndex-1] != results[playerIndex-1]) && (subtration[playerIndex-1] != results[playerIndex-1]) && (product[playerIndex-1] != results[playerIndex-1]))
                    correct += 1;
                else
                {
                    errors += 1;
                    position = noteLosers(name, losers, position);
                }
            }
            i += 1;
        }
        if (correct == numberOfExpressions)
            printf("You Shall All Pass!\n");
        else if (errors == numberOfExpressions)
            printf("None Shall Pass!\n");
        else
        {
            sortStrings(losers, position);
            for (int i=0; i < position; i++)
            {
                if (i != (position-1))
                    printf("%s ", losers[i]);
                else
                    printf("%s\n", losers[i]);
            }
        }
   }
   return 0;
}
