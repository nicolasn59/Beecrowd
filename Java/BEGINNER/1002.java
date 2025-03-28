import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double pi = (double) 3.14159;
        double radius = scanner.nextDouble();
        System.out.printf("A=%.4f\n", pi * (radius * radius));
    }
}
