import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n1, n2, n3, greater;
        n1 = scanner.nextInt();
        n2 = scanner.nextInt();
        n3 = scanner.nextInt();
        greater = (n1 + n2 + Math.abs(n1 - n2)) / 2;
        greater = (greater + n3 + Math.abs(greater - n3)) / 2;
        System.out.printf("%d eh o maior\n", greater);
    }
}
