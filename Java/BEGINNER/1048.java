import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner keyboard = new Scanner(System.in);
        double salario = keyboard.nextDouble();
        double novoSalario, reajuste, percentual;
        if (salario <= 400){
            percentual = 15.0;
            reajuste = salario * 0.15;
            novoSalario = reajuste + salario;
        }
        else if (salario <= 800){
            percentual = 12.0;
            reajuste = salario * 0.12;
            novoSalario = salario + reajuste;
        }
        else if (salario <= 1200){
            percentual = 10.0;
            reajuste = salario * 0.10;
            novoSalario = reajuste + salario;
        }
        else if (salario <= 2000)
        {
            percentual = 7.0;
            reajuste = salario * 0.07;
            novoSalario = salario + reajuste;
        }
        else{
            percentual = 4.0;
            reajuste = salario * 0.04;
            novoSalario = salario + reajuste;
        }
        System.out.printf("Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: %d %%\n", novoSalario, reajuste, ((int)percentual));
    }
}
