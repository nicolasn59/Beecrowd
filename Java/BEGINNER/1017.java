import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int time, averageSpeed;
        time = scanner.nextInt();
        averageSpeed = scanner.nextInt();
        System.out.printf("%.3f\n", (averageSpeed * time)/12.0);
    }
}
