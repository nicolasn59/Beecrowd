import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner keyboard = new Scanner(System.in);
        double a, b, c, delta;
        a = keyboard.nextDouble();
        b = keyboard.nextDouble();
        c = keyboard.nextDouble();
        delta = (b*b) - 4 * a * c;
        if (delta < 0 || a == 0){
            System.out.println("Impossivel calcular");
        }
        else{
            System.out.printf("R1 = %.5f\nR2 = %.5f\n", (((-1)*b + Math.sqrt(delta))/(2*a)), (((-1)*b - Math.sqrt(delta))/(2*a)));
        }
    }
}
