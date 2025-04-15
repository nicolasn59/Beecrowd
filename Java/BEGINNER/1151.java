import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner teclado = new Scanner(System.in);
        int n = teclado.nextInt();
        int t_anterior = 0, t_atual = 1;
        if (n == 1) System.out.print("0\n");
        else if (n == 2) System.out.print("0 1\n");
        else{  // Se n > 2
            System.out.print("0 1 ");
            while ((n-3) != 0){ // Subtraí -3 de n, porque já foram impressos dois termos e o último termo não deve possuir espaço ao final
                System.out.printf("%d ", (t_anterior + t_atual));
                int temp = t_atual;
                t_atual += t_anterior;
                t_anterior = temp;
                n -= 1;
            }
            System.out.printf("%d\n", (t_anterior + t_atual));
        }
        teclado.close();
    }
}
