#include <stdio.h>

int pickLen(char numStr[]);
void reversePrint(char numStr[], int lenString);

int main() {
    int len;
    unsigned long long int number;
    char numberString[100];
    scanf("%llu", &number); // Receber Número
    sprintf(numberString, "%llu", number); // Converter para String
    len = pickLen(numberString);
    reversePrint(numberString, len);
    return 0;
}

int pickLen(char numStr[])
{
    int lenString=0, i;
    for (i=0; numStr[i] != '\0'; i++)
    {
        lenString += 1;
    }
    return lenString;
}

void reversePrint(char numStr[], int lenString)
{
    lenString -= 1; // Retirando o índice do '\0'!!!
    while (lenString != 0)
    {
        printf("%c", numStr[lenString]);
        lenString -= 1;
    }
    printf("%c\n", numStr[0]);
}
