#include <stdio.h>

void checkPrime(int sum)
{
    int count=0;
    for (int i=2; i <= sum; i++)
    {
        if (sum % i == 0)
            count += 1;
    }
    if (count == 1)
        printf("You’re a coastal aircraft, Robbie, a large silver aircraft.\n");
    else
        printf("Bad boy! I’ll hit you.\n");
}

int main()
{
    int numberOfCoins, jump;
    
    while (scanf("%d", &numberOfCoins) != EOF)
    {    
        int coinPot[numberOfCoins];
        for (int i=(numberOfCoins-1); i >= 0; i--)
        {
            scanf("%d", &coinPot[i]);
        }
        scanf("%d", &jump);
        int sum=0;
        for (int i=0; i < numberOfCoins; i+=jump)
        {
            sum += coinPot[i];
        }
        checkPrime(sum);
    }
    return 0;
}