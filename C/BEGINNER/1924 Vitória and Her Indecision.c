#include <stdio.h>

int main()
{
    int numCourses;
    char courseName[101];
    scanf("%d\n", &numCourses);
    for (int i = 0; i != (numCourses - 1); i++)
    {
        scanf("%s\n", courseName);
    }
    printf("Ciencia da Computacao\n");
    return 0;
}