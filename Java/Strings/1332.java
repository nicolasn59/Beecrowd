import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner keyboard = new Scanner(System.in);
        int casos = keyboard.nextInt();
        keyboard.nextLine();
        String palavra;
        while (casos != 0){
            palavra = keyboard.nextLine();
            if (palavra.length() > 3) System.out.println("3");
            else if (((palavra.charAt(0) == 'o') && ((palavra.charAt(1) == 'n') || (palavra.charAt(2) == 'e'))) ||
                    ((palavra.charAt(1) == 'n') && ((palavra.charAt(0) == 'o' || palavra.charAt(2) == 'e'))) ||
                    ((palavra.charAt(2) == 'e') && ((palavra.charAt(0) == 'o' || palavra.charAt(1) == 'n')))) System.out.println("1");
            else System.out.println("2");
            casos -= 1;
        }
    }
}
