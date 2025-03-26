#include<stdio.h>
#include <stdlib.h>

float calculateAverage(float *studentGrades, float numStudents);
int studentsAboveAverage(float *studentGrades, float numStudents, float averageGrade);

int main()
{
    int classes; // Number of test cases
    scanf("%d", &classes);
    while (classes != 0)
    {
        float *grades, students;
        scanf("%f", &students);
        grades = (float*) malloc(students * sizeof(float));
        for(int i = 0; i < students; i++)
            scanf("%f", &grades[i]);
        float average;    
        average = calculateAverage(grades, students);
        studentsAboveAverage(grades, students, average);
        free(grades);
        classes -= 1;
    }
    return 0;
}

float calculateAverage(float *studentGrades, float numStudents)
{
    float sumGrades = 0;
    for (int i = 0; i < numStudents; i++)
        sumGrades += studentGrades[i];
    return (sumGrades / numStudents);    
}

int studentsAboveAverage(float *studentGrades, float numStudents, float averageGrade)
{
    float count = 0; // Count students above average
    for (int i = 0; i < numStudents; i++)
    {
        if (studentGrades[i] > averageGrade)
            count += 1;
    }
    printf("%.3f%%\n", ((100.0 * count) / numStudents));
    return 0;
}
