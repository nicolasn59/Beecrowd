#include <stdio.h>

void minPresses(unsigned long int numFloors, unsigned long int current, unsigned long int destination, unsigned long int up, unsigned long int down);

int main()
{
    unsigned long int numFloors, currentFloor, destinationFloor, up, down;
    scanf("%lu %lu %lu %lu %lu", &numFloors, &currentFloor, &destinationFloor, &up, &down);
    minPresses(numFloors, currentFloor, destinationFloor, up, down);
    return 0;
}

void minPresses(unsigned long int numFloors, unsigned long int current, unsigned long int destination, unsigned long int up, unsigned long int down)
{
    unsigned long int count = 0;
    for (unsigned long int i = 0; i <= numFloors; i++)
    {
        if (current == destination)
        {
            printf("%lu\n", count);
            return;
        }
        else if (current < destination)
        {
            if (up == 0)
            {
                printf("use the stairs\n");
                return;
            }
            else
            {
                current += up;
                count += 1;
            }
        }
        else
        {
            if (down == 0)
            {
                printf("use the stairs\n");
                return;     
            }
            else
            {
                current -= down;
                count += 1;
            }
        }
    }
    printf("use the stairs\n");
}