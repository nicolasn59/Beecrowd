import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        int num = keyboard.nextInt();
        String listaNum = "";
        while (num != 0){
            for (int i=1; i<num; i++){
                listaNum = listaNum.concat(String.valueOf(i));  // Concatena o valor tipo inteiro "i" para tipo string
                listaNum += " ";  // Concatena um espaço ao final da String
            }
            listaNum = listaNum.concat(String.valueOf(num));
            System.out.printf("%s\n", listaNum);
            num = keyboard.nextInt();
            listaNum = "";
        }
    }
}
