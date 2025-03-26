#include <stdio.h>

int main(){
    double score1, score2;
    scanf("%lf", &score1);
    scanf("%lf", &score2);
    printf("MEDIA = %.5lf\n", ((score1*3.5 + score2*7.5)/11));
    return 0;
}
