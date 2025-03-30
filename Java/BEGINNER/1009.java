import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String name = scanner.nextLine();
        double salary = scanner.nextDouble();
        double salesMoney = scanner.nextDouble();
        System.out.printf("TOTAL = R$ %.2f\n", (salary + (salesMoney * 15/100)));
    }
}
