import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner keyboard = new Scanner(System.in);
        int casos = keyboard.nextInt(); // Quantidade de casos de testes
        keyboard.nextLine();  // Consome a quebra de linha ('\n')
        String string;
        String num1 = "", num2="", num3="";
        while (casos != 0){
            string = keyboard.nextLine();  // Receber a entrada string
            num1 = string.substring(2,4);  // Separa parte da string em uma substring a partir do índice indicado e terminando um índice a menos
            num2 = string.substring(5, 8);
            num3 = string.substring(11, 13);
            int soma = ((Integer.parseInt(num1))) + ((Integer.parseInt(num2))) + ((Integer.parseInt(num3)));
            System.out.printf("%d\n", soma);
            casos -= 1;
        }
        keyboard.close();
    }
}
