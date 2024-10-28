#include <stdio.h>

int main() {
    int pressaoDigitada, pressaoDoPneu;
    scanf("%d %d", &pressaoDigitada, &pressaoDoPneu);
    printf("%d\n", (pressaoDigitada - pressaoDoPneu));
    return 0;
}
