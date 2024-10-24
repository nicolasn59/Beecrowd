#include <stdio.h>

int main()
{
    // hora inicial, minuto inicial, hora final, minuto final, hora resultado e minuto resultado
    int hi, mi, hf, mf, hr, mr;
    scanf("%d %d %d %d", &hi, &mi, &hf, &mf);
    
    // HORAS
    if (hf > hi)
    {
        if (mf >= mi)
            hr = (hf - hi);
        else if (mi > mf)
            hr = (hf - hi) - 1;
    }
    else if (hi > hf)
    {
        if (mf >= mi)
            hr = (24 - (hi - hf));
        else if (mi > mf)
            hr = (23 - (hi - hf));
    }
    else
    {
        if (mf > mi)
            hr = (hf - hi);
        else if (mi > mf)
            hr = (23 - (hf - hi));
        else
            hr = 24;
    }

    // MINUTOS
    if (mf >= mi)
        mr = (mf - mi);
    else
        mr = (60 - (mi - mf));

    printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", hr, mr);
    return 0;
}
