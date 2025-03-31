import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int totalMoney = scanner.nextInt();
        int money100, money50, money20, money10, money5, money2, money1, tempMoney=totalMoney;

        money100 = totalMoney / 100;
        totalMoney %= 100;
        money50 = totalMoney / 50;
        totalMoney %= 50;
        money20 = totalMoney / 20;
        totalMoney %= 20;
        money10 = totalMoney / 10;
        totalMoney %= 10;
        money5 = totalMoney / 5;
        totalMoney %= 5;
        money2 = totalMoney / 2;
        totalMoney %= 2;
        money1 = totalMoney;

        System.out.println(tempMoney);
        System.out.printf("%d nota(s) de R$ 100,00\n%d nota(s) de R$ 50,00\n%d nota(s) de R$ 20,00\n%d nota(s) de R$ 10,00\n%d nota(s) de R$ 5,00\n%d nota(s) de R$ 2,00\n%d nota(s) de R$ 1,00\n", money100, money50, money20, money10, money5, money2, money1);
    }
}
