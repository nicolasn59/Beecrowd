import java.util.Scanner;
import java.util.Locale;

public class Main {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner scanner = new Scanner(System.in);

        int cod1, cod2, num1, num2;
        double value1, value2;

        cod1 = scanner.nextInt();
        num1 = scanner.nextInt();
        value1 = scanner.nextDouble();

        cod2 = scanner.nextInt();
        num2 = scanner.nextInt();
        value2 = scanner.nextDouble();

        System.out.printf("VALOR A PAGAR: R$ %.2f\n", (num2 * value2) + (num1 * value1));
    }
}
