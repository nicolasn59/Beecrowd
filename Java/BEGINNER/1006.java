import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double A = scanner.nextDouble();
        double B = scanner.nextDouble();
        double C = scanner.nextDouble();
        System.out.printf("MEDIA = %.1f\n", ((A*2)+(B*3)+(C*5))/(10));
    }
}
