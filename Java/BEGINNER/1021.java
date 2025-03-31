import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        double money = scanner.nextDouble();
        money *= 100;
        System.out.println("NOTAS:");
        System.out.printf("%.0f nota(s) de R$ 100.00\n", Math.floor(money/10000));
        System.out.printf("%.0f nota(s) de R$ 50.00\n", Math.floor((money%10000)/5000));
        System.out.printf("%.0f nota(s) de R$ 20.00\n", Math.floor(((money%10000)%5000)/2000));
        System.out.printf("%.0f nota(s) de R$ 10.00\n", Math.floor((((money%10000)%5000)%2000)/1000));
        System.out.printf("%.0f nota(s) de R$ 5.00\n", Math.floor(((((money%10000)%5000)%2000)%1000)/500));
        System.out.printf("%.0f nota(s) de R$ 2.00\n", Math.floor((((((money%10000)%5000)%2000)%1000)%500)/200));

        System.out.println("MOEDAS:");
        System.out.printf("%.0f moeda(s) de R$ 1.00\n", Math.floor(((((((money%10000)%5000)%2000)%1000)%500)%200)/100));
        System.out.printf("%.0f moeda(s) de R$ 0.50\n", Math.floor((((((((money%10000)%5000)%2000)%1000)%500)%200)%100)/50));
        System.out.printf("%.0f moeda(s) de R$ 0.25\n", Math.floor(((((((((money%10000)%5000)%2000)%1000)%500)%200)%100)%50)/25));
        System.out.printf("%.0f moeda(s) de R$ 0.10\n", Math.floor((((((((((money%10000)%5000)%2000)%1000)%500)%200)%100)%50)%25)/10));
        System.out.printf("%.0f moeda(s) de R$ 0.05\n", Math.floor(((((((((((money%10000)%5000)%2000)%1000)%500)%200)%100)%50)%25)%10)/5));
        System.out.printf("%.0f moeda(s) de R$ 0.01\n", ((((((((((((money%10000)%5000)%2000)%1000)%500)%200)%100)%50)%25)%10)%5)/1));
    }
}
