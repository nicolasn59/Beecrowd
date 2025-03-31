import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int hours, minutes, seconds;
        seconds = scanner.nextInt();
        hours = seconds/3600;
        minutes = (seconds % 3600) /60;
        seconds %= 60;
        System.out.printf("%d:%d:%d\n", hours, minutes, seconds);
    }
}
