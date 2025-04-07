import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner keyboard = new Scanner(System.in);
        String text = keyboard.nextLine();
        if (text.length() <= 140){
            System.out.print("TWEET");
        }
        else{
            System.out.print("MUTE");
        }
        System.out.println();
    }
}
