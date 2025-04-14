import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        // V = pi * (r*r) * h  -> VOLUME DO CILÍNDRO
        double pi = 3.14, volume, diametro, raio, altura, area;
        while (keyboard.hasNextDouble()){
            volume = keyboard.nextDouble();
            diametro = keyboard.nextDouble();
            raio = diametro/2;
            altura = volume / (pi * (raio*raio));
            area = pi * Math.pow(raio, 2);
            System.out.printf("ALTURA = %.2f\nAREA = %.2f\n", altura, area);
        }
        keyboard.close();
    }
}
