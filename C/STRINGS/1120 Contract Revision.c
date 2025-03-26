#include <stdio.h>

int main()
{
    char faultyDigit[2], originalNumber[150];
    int finalOriginal, i, j;
    scanf("%s ", faultyDigit);
    fgets(originalNumber, 103, stdin);
    while (faultyDigit[0] != '0' || originalNumber[0] != '0')
    {
        char contractNumber[150] = {};
        // SIZE OF THE ARRAY
        finalOriginal = 0;
        while (originalNumber[finalOriginal] != '\0' && originalNumber[finalOriginal] != '\n')
            finalOriginal += 1;
        // REMOVE FAULTY DIGITS
        i = j = 0;
        while (i != finalOriginal)
        {
            if (originalNumber[i] != faultyDigit[0])
            {
                contractNumber[j] = originalNumber[i];
                j += 1;
            }
            i += 1;
        }
        contractNumber[finalOriginal] = '\0';
        // Check beginning and end
        int confirm, finalContract;
        finalContract = j;
        confirm = 0;
        if (contractNumber[0] == '0' && contractNumber[finalContract - 1] == '0') // KEEP AN EYE
        {
            i = 0;
            while (i != finalContract)
            {
                if (contractNumber[i] == '0')
                    confirm += 1;
                i += 1;    
            }
        }
        if (confirm == j || j == 0)
            {
                printf("0\n");
            }
        else
        {   
            if (contractNumber[0] == '0')
            {
                i = 0;
                while (contractNumber[i] == '0')
                {
                    i += 1;
                }
                for (j = i; contractNumber[j] != '\0'; j++)
                {
                    printf("%c", contractNumber[j]);
                }
                printf("\n");
            }
            else
                printf("%s\n", contractNumber);
        }
        // char faultyDigit[2] = {}, originalNumber[150] = {};
        scanf("%s ", faultyDigit);
        fgets(originalNumber, 103, stdin);
    }
    return 0;
}
