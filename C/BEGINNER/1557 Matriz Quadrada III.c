#include <stdio.h>
#include <stdlib.h>


int lenght(int value);


int main (void){
    int tamanho;
    scanf("%d", &tamanho);
    while (tamanho != 0){
        int matriz[tamanho][tamanho], cont=1;
        for (int lin=0; lin<tamanho; lin++){
            matriz[lin][0] = cont;
            for (int col=1; col<tamanho; col++){
                matriz[lin][col] = (matriz[lin][col-1] * 2);
            }
            cont*=2;
        }
        // VERIFICAR A QUANTIDADE DE DÍGITOS DO MAIOR VALOR DA MATRIZ
        int len;
        len = lenght(matriz[tamanho-1][tamanho-1]);
        
        for (int lin=0; lin<tamanho; lin++){

            // ESPAÇO NO INÍCIO DA MATRIZ
            for (int temp=0; temp<len-(lenght(matriz[lin][0])); temp++){
                printf(" ");
            }
            for (int col=0; col<tamanho; col++){
                // VALORES DA MATRIZ
                printf("%d", matriz[lin][col]);

                if (col != (tamanho-1)){ // EVITANDO IMPRIMIR ESPAÇOS AO FINAL DA LINHA
                    // ESPAÇO ENTRE OS NÚMEROS DA MATRIZ
                    for (int temp2=0; temp2<(len+1)-(lenght(matriz[lin][col+1])); temp2++){
                        printf(" ");
                    }
                }
                
            }
            printf("\n");
        }
        scanf("%d", &tamanho);
        printf("\n");
    }
    return 0;
}


int lenght(int value){
    if (value == 0){
        return 0;
    }
    else{
        return 1 + lenght(value/10);
    }
}
