import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner keyboard = new Scanner(System.in);
        int casos = keyboard.nextInt(); // Quantidade de casos de testes
        keyboard.nextLine();
        String frase;
        while (casos != 0){
            frase = keyboard.nextLine();
            String[] palavras = frase.split(" "); // Separa cada string em um vetor
            for (String palavra: palavras){
                if (!palavra.equals(""))  //  Se palavra for diferente de ""
                    System.out.print(palavra.charAt(0)); // Imprime o primeiro caractere de cada palavra
            }
            System.out.println();
            casos--;
        }
        keyboard.close();
    }
}
