import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner keyboard = new Scanner(System.in);
        int casos = keyboard.nextInt();  // Quantidade casos de testes
        keyboard.nextLine();  // Consome a quebra de linha
        while (casos != 0){
            char[] array = new char[26];
            String frase = keyboard.nextLine();  // Recebe frase
            String novaFrase = frase.replace(" ", "").replace(",", "");  // Retira espaços e vírgulas
            int lenFrase = novaFrase.length();  // Verifica o tamanho da string
            int cont = 0; // Variável de controle para os índices do array
            for (int i=0; i < lenFrase; i++){
                boolean letraNoVetor = false;
                for (int j=0; j < array.length; j++){
                    if (array[j] == '\u0000') break;  // O vetor é automáticamente preenchido com '\u0000' quando está vazio
                    if (novaFrase.charAt(i) == array[j]) { // Verifica se a letra está no vetor
                        letraNoVetor = true;
                    }
                }
                if (!letraNoVetor){  // Se letraNoVetor for false
                    array[cont] = novaFrase.charAt(i); // Vetor recebe a uma letra da frase
                    cont++; // Acrescenta +1 na variável de controle
                }
            }

            // Esse trecho irá contar a quantidade de letras no vetor
            int lenVetor = 0;
            for (int i=0; i < array.length; i++){
                if (array[i] == '\u0000') break; // O loop será interrompido se o índice estiver vazio
                lenVetor++; // Se o vetor não estiver vazio, será acrescentado +1 na contagem de elementos do vetor
            }

            if (lenVetor < 13) System.out.println("frase mal elaborada");
            else if (lenVetor < 26) System.out.println("frase quase completa");
            else System.out.println("frase completa");
            casos--; // Substrai -1 para casos de testes
        }
        keyboard.close();
    }
}
