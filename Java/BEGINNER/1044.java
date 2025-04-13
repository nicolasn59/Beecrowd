import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner keyboard = new Scanner(System.in);
        int a = keyboard.nextInt();
        int b = keyboard.nextInt();
        if ((a % b == 0) || (b % a == 0)) System.out.print("Sao Multiplos\n");
        else System.out.print("Nao sao Multiplos\n");
    }
}
