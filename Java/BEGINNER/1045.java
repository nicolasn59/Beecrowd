import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner keyboard = new Scanner(System.in);
        double[] array = new double[3];
        for (int i=0; i<3; i++){
            array[i] = keyboard.nextDouble();
        }

        for (int i=0; i<3; i++){
            for (int j=0; j<3-1; j++){
                if (array[j] < array[j+1]){
                    double temp = array[j];
                    array[j] = array[j+1];
                    array[j+1] = temp;
                }
            }
        }
        double a = array[0], b = array[1], c = array[2];
        if (a >= (b+c)){
            System.out.println("NAO FORMA TRIANGULO");
        }
        else{
            if ((a*a) == ((b*b) + (c*c))){
                System.out.println("TRIANGULO RETANGULO");
            }
            if ((a*a) > ((b*b) + (c*c))){
                System.out.println("TRIANGULO OBTUSANGULO");
            }
            if ((a*a) < ((b*b) + (c*c))){
                System.out.println("TRIANGULO ACUTANGULO");
            }
            if (a == b && b == c){
                System.out.println("TRIANGULO EQUILATERO");
            }
            if ((a == b && b != c) || (a != b && b == c) || (a == c && b != a)){
                System.out.println("TRIANGULO ISOSCELES");
            }
        }
    }
}
