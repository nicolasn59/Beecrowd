#include <stdio.h>

int main()
{
    // diaInicial, diaFinal, horaInicial, horaFinal, minutoInicial, minutoFinal, segundoInicial, segundoFinal
    int di, df, hi, hf, mi, mf, si, sf;

    // diaResultado, horaResultado, minutoResultado,  segundoResultado
    int dr, hr, mr, sr;

    char x, y; // Sem utilidade, apenas armazenamento

    scanf("%s %d", &x, &di);
    scanf("%d %s %d %s %d", &hi, &x, &mi, &y, &si);
    scanf("%s %d", &x, &df);
    scanf("%d %s %d %s %d", &hf, &x, &mf, &y, &sf);

    // DIAS

    if (hi > hf)
        dr = (df - di) - 1;
    else if (hi == hf)
    {
        if (mi == mf)
        {
            if (si <= sf)
                dr = (df - di);
        }
        else if (mi >= mf)
            dr = (hi - hf);
        else
            dr = (df - di);
    }

    else
        if (hi == hf)
        {
            if (mi == mf)
            {
                if (si > sf)
                    dr = (df - di);
            }
        }
        else
            dr = (df - di);
    
    // HORAS 

    if (hi > hf)
    {
        if (mi >= mf)
            hr = 23 - (hi - hf);
        else if (mf > mi)
        {
            hr = 24 - (hi - hf);
        }
    }
    else if (hi == hf)
    {
        if (mi > mf)
            hr = 24 - (mi - mf);
        else if (mi == mf)
            hr = 0;
    }
    else
    {
        if (mi == mf)
            if (si <= sf)
                hr = (hf - hi);
            else
                hr = 0;
        else if (mi > mf)
        {   
            if (si > sf)
                hr = 23 - (hf - hi);
            else
                hr = 0;
        }
        else
            hr = (hf - hi);
    }
    
    // MINUTOS

    if (mi > mf)
    {
        if (sf > si)
        mr = 60 - (mi - mf);
        else
            mr = 59 - (mi - mf);
    }
    else if (mi == mf)
    {
        if (si > sf)
            mr = 60 - (si - sf); // ACABEI DE MUDAR DE 59 PARA 60
        else if (si == sf)
            mr = (mi - mf);
        else
            mr = (mi - mf);
    }
    else
        if (si > sf)
            mr = (mf - mi) - 1;
        else
            mr = (mf - mi);

    // SEGUNDOS

    if (si > sf)
        sr = 60 - (si - sf);
    else
        sr = (sf - si);

    printf("%d dia(s)\n", dr);
    printf("%d hora(s)\n", hr);
    printf("%d minuto(s)\n", mr);
    printf("%d segundo(s)\n", sr);
    return 0;
}
