/*
RECEIVE NUMBER OF TESTS
START A LOOP
    RECEIVE NUMBER OF POWER STRIPS
    DEFINE A FUNCTION TO DETERMINE HOW MANY DEVICES CAN BE CONNECTED
    
    FUNCTION...
        START A LOOP
            RECEIVE NUMBER OF OUTLETS IN EACH POWER STRIP
        KNOWING THAT EACH POWER STRIP HAS N-1 OUTLETS, CALCULATE THE TOTAL NUMBER OF DEVICES
        THAT CAN BE CONNECTED

    PRINT TOTAL NUMBER OF CONNECTED DEVICES
*/

#include <stdio.h>

void connectedDevices(int numStrips);

int main()
{
    int numberOfTests, numberOfStrips;
    scanf("%d", &numberOfTests);
    for (int i=0; i < numberOfTests; i++)
    {
        scanf("%d", &numberOfStrips);
        connectedDevices(numberOfStrips);
    }
    return 0;
}

void connectedDevices(int numStrips)
{
    int outletsInStrip, total=0;
    for (int i=0; i < numStrips; i++)
    {
        scanf("%d", &outletsInStrip);
        total += (outletsInStrip-1);
    }
    printf("%d\n", (total+1));
}