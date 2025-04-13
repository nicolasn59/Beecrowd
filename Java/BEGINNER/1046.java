import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner keyboard = new Scanner(System.in);
        int horaInicial = keyboard.nextInt();
        int horaFinal = keyboard.nextInt();

        if (horaInicial > horaFinal)
            System.out.printf("O JOGO DUROU %d HORA(S)\n", (24 + horaFinal) - horaInicial);
        else if (horaInicial < horaFinal)
            System.out.printf("O JOGO DUROU %d HORA(S)\n", horaFinal - horaInicial);
        else
            System.out.println("O JOGO DUROU 24 HORA(S)");
    }
}
