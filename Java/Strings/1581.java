import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner keyboard = new Scanner(System.in);
        int casos = keyboard.nextInt();
        int qtdPessoas;
        keyboard.nextLine(); // Consome a quebra de linha após receber o inteiro
        String idioma, idioma_comparacao;  // Serão comparados um com o outro
        while (casos != 0){
            qtdPessoas = keyboard.nextInt();  // Recebe a quantidade de pessoas do grupo
            keyboard.nextLine();  // Consome a quebra de linha
            idioma = keyboard.nextLine();  // Recebe o idioma para a comparação
            qtdPessoas -= 1;  // Está sendo diminuído porque uma das entradas de String já foi recebida fora do loop
            while (qtdPessoas != 0){
                idioma_comparacao = keyboard.nextLine();
                if (!idioma.equals(idioma_comparacao))  // Se o idioma for diferente da String que virá na entrada
                    idioma = "ingles";
                qtdPessoas -= 1;
            }
            System.out.printf("%s\n", idioma);
            casos -= 1;
        }
        keyboard.close();
    }
}
