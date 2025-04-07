#include <stdio.h>
#include <string.h>


int contarCaracteres(char *text);


int main(){
    char text[501];
    fgets(text, sizeof(text), stdin);
    int contador = contarCaracteres(text);  
    if (contador <= 140){
        printf("TWEET\n");
    } 
    else{
        printf("MUTE\n");
    }
    return 0;
}


int contarCaracteres(char *text){
    int i=0;
    while (text[i] != '\0'){
        i++;
    }
    return i-1; // REMOVENDO O '\n'
}
