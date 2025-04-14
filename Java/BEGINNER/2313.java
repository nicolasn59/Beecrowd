import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        int[] valores = new int[3];
        for (int i=0; i<3; i++){
            valores[i] = keyboard.nextInt();
        }

        for (int i=0; i<3; i++){
            for (int j=0; j<3-1; j++){
                if (valores[j] < valores[j+1]){
                    int temp = valores[j];
                    valores[j] = valores[j+1];
                    valores[j+1] = temp;
                }
            }
        }
        int a = valores[0], b = valores[1], c = valores[2];

        if (((a + b) > c) && ((b + c) > a) && ((a + c) > b)){
            if (a == b && b == c) System.out.println("Valido-Equilatero");
            else if ((a != b) && (b != c) && (a != c)) System.out.println("Valido-Escaleno");
            else System.out.println("Valido-Isoceles");
            if ((a*a) == ((b*b) + (c*c))) System.out.println("Retangulo: S");
            else System.out.println("Retangulo: N");
        }
        else{
            System.out.println("Invalido");
        }
    }
}
