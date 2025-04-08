import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner keyboard = new Scanner(System.in);
        double n1, n2, n3, n4;
        n1 = keyboard.nextDouble();
        n2 = keyboard.nextDouble();
        n3 = keyboard.nextDouble();
        n4 = keyboard.nextDouble();

        double average;
        average = Math.floor((n1*2) + (n2*3) + (n3*4) + (n4)) / (2+3+4+1);
        System.out.printf("Media: %.1f\n", average);
        if (average >= 7.0){
            System.out.println("Aluno aprovado.");
        }
        else if (average < 5.0){
            System.out.println("Aluno reprovado.");
        }
        else{
            System.out.println("Aluno em exame.");
            double n5 = keyboard.nextDouble();
            System.out.printf("Nota do exame: %.1f\n", n5);
            average = (average+n5)/2;
            if (average >= 5.0){
                System.out.println("Aluno aprovado.");
            }
            else{
                System.out.println("Aluno reprovado.");
            }
            System.out.printf("Media final: %.1f\n", average);
        }
    }
}
