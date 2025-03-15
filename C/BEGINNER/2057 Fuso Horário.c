#include <stdio.h>

void calcularChegada(int s, int t, int f);

int main() {
    int saida, tempoViagem, fusoHorario;
    scanf("%d %d %d", &saida, &tempoViagem, &fusoHorario);
    calcularChegada(saida, tempoViagem, fusoHorario);
    return 0;
}

void calcularChegada(int s, int t, int f)
{
    if ((s+t+f) >= 24)
        printf("%d\n", ((s+t+f) - 24));
    else if ((s+t+f) < 0)
        printf("%d\n", ((s+t+f) + 24));
    else
        printf("%d\n", (s+t+f));
}
