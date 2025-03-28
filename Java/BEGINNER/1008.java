import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();
        int horasTrabalhadas = scanner.nextInt();
        double SalarioPorHora = scanner.nextDouble();
        System.out.printf("NUMBER = %d\n", num);
        System.out.printf("SALARY = U$ %.2f\n", (horasTrabalhadas*SalarioPorHora));
    }
}
