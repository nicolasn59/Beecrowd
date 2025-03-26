#include <stdio.h>

int main()
{
    int numMessages, count, messageLength, i, j;
    char message[1001], reversedMessage[1001];
    scanf("%d ", &numMessages);
    while (numMessages != 0)
    {
        fgets(message, 1001, stdin);
        messageLength = 0;
        while (message[messageLength] != '\0' && message[messageLength] != '\n') // COUNT CHARACTERS IN THE MESSAGE
            messageLength += 1;
        for (count = 0; count != messageLength; count++) // FIRST PASS
        {
            if ((message[count] >= 'a' && message[count] <= 'z') || (message[count] >= 'A' && message[count] <= 'Z'))
                message[count] = message[count] + 3;
        }
        // SECOND PASS
        i = messageLength - 1; // ELIMINATING THE \0
        j = 0;
        while (j < messageLength)
        {
            reversedMessage[j] = message[i];
            i -= 1;
            j += 1;
        }
        reversedMessage[messageLength] = '\0';
        for (count = messageLength - 1; count >= (messageLength / 2); count--)
        {
            reversedMessage[count] -= 1;
        }
        printf("%s\n", reversedMessage);
        numMessages -= 1;
    }
    return 0;
}
