import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner keyboard = new Scanner(System.in);
        double a, b, c;
        a = keyboard.nextDouble();
        b = keyboard.nextDouble();
        c = keyboard.nextDouble();
        if (((a+b) > c) && ((b+c) > a) && ((a+c) > b)){
            System.out.printf("Perimetro = %.1f\n", (a+b+c));
        }
        else{
            System.out.printf("Area = %.1f\n", ((a+b)*c)/2);
        }
    }
}
