import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        int val1, val2;
        val1 = keyboard.nextInt();
        val2 = keyboard.nextInt();
        if (val1 > val2){
            int temp = val1;
            val1 = val2;
            val2 = temp;
        }
        for (int i = val1+1; i < val2; i++){
            if ((i % 5 == 2) || (i % 5 == 3)) System.out.printf("%d\n", i);
        }
    }
}
