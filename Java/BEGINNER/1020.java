import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int age, years, mounths, days;
        age = scanner.nextInt();
        years = age / 365;
        mounths = (age % 365) / 30;
        days = (age % 365) % 30;
        System.out.printf("%d ano(s)\n%d mes(es)\n%d dia(s)\n", years, mounths, days);
    }
}
