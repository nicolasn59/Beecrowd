import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        String texto = keyboard.nextLine();
        if (texto.length() > 80) System.out.println("NO");
        else System.out.println("YES");
        keyboard.close();
    }
}
