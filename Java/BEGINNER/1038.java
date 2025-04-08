import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner keyboard = new Scanner(System.in);
        int code, amount;
        code = keyboard.nextInt();
        amount = keyboard.nextInt();
        if (code == 1){
            System.out.printf("Total: R$ %.2f\n", (4.00*amount));
        }
        else if (code == 2){
            System.out.printf("Total: R$ %.2f\n", (4.5*amount));
        }
        else if (code == 3) {
            System.out.printf("Total: R$ %.2f\n", (5.00*amount));
        }
        else if (code == 4){
            System.out.printf("Total: R$ %.2f\n", (2.00*amount));
        }
        else{
            System.out.printf("Total: R$ %.2f\n", (1.5*amount));
        }

    }
}
