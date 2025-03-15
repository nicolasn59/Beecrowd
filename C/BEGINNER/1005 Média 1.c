#include <stdio.h>

int main(){
    double note1, note2;
    scanf("%lf", &note1);
    scanf("%lf", &note2);
    printf("MEDIA = %.5lf\n", ((note1*3.5 + note2*7.5)/11));
    return 0;
}
