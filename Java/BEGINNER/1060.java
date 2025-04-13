import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        double valor;
        int contador = 0;
        for (int i=0; i<6; i++){
            valor = keyboard.nextDouble();
            if (valor > 0) contador ++;
        }
        System.out.printf("%d valores positivos\n", contador);
    }
}
