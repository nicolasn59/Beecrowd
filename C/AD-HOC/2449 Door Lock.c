#include <stdio.h>
#include <math.h>

int main()
{
    int numPins, idealHeight;
    scanf("%d %d", &numPins, &idealHeight);
    int height[numPins];
    for (int i = 0; i < numPins; i++)
        scanf("%d", &height[i]);
    int total = 0;
    for (int i = 1; i < numPins; i++)
    {
        if (idealHeight >= height[i - 1])
            height[i] += idealHeight - height[i - 1];
        else
            height[i] -= height[i - 1] - idealHeight;
        total += abs(idealHeight - height[i - 1]);
    }
    printf("%d\n", total);
    return 0;
}