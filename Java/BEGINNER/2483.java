import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner keyboard = new Scanner(System.in);
        int i = keyboard.nextInt();
        System.out.print("Feliz nat");
        while (i != 0){
            System.out.print("a");
            i -= 1;
        }
        System.out.println("l!");
    }
}
