import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner keyboard = new Scanner(System.in);
        String string;
        String substring = "";

        while (keyboard.hasNext()){
            int i = 0, num1=0, num2=0, num3=0;
            string = keyboard.nextLine();  // Recebe nova entrada

            if (string.charAt(0) != 'R'){
                while (string.charAt(i) != '+'){
                    substring += string.charAt(i);  // Concatena o tipo char com a substring
                    i++;
                }
                i++; // Aumentando o valor de "i" em +1, porque "i" estava no índice de '+'
                num1 = Integer.parseInt(substring); // Converte o número para inteiro (antes era uma String)
                substring = ""; // Reseta a variável
            }
            else i += 2; // A variável "i" passa por 'R' (índice 0) e depois por '+' (índice 1)

            if (string.charAt(i) != 'L'){
                while (string.charAt(i) != '='){
                    substring += string.charAt(i);
                    i++;
                }
                i++; // Aumentando o valor de "i" em +1, porque "i" estava no índice de '='
                num2 = Integer.parseInt(substring);
                substring = "";
            }
            else i += 2; // A variável "i" passa por 'L' e depois por '='
            if (string.charAt(i) != 'J'){
                substring = string.substring(i); // substring recebe uma parte de string que vai de i até o final da string
                num3 = Integer.parseInt(substring);
            }

            if (num3 == 0) System.out.printf("%d\n", num1 + num2);
            else if (num2 == 0) System.out.printf("%d\n", num3 - num1);
            else System.out.printf("%d\n", num3 - num2);
            substring = "";  // Reseta substring
        }
        keyboard.close();
    }
}
