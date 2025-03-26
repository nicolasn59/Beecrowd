#include <stdio.h>

int main() {
    int students;
    long int registration, approved;
    float grade, highest = 0;
    scanf("%d", &students);
    while (students != 0)
    {
        scanf("%ld %f", &registration, &grade);
        if (highest < grade)
        {
            highest = grade;
            approved = registration;
        }
        students -= 1;
    }
    if (highest < 8)
        printf("Minimum note not reached\n");
    else
        printf("%ld\n", approved);
    return 0;
}
