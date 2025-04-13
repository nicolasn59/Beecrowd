import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        String word1, word2, word3;
        word1 = keyboard.nextLine();
        word2 = keyboard.nextLine();
        word3 = keyboard.nextLine();
        if (word1.equals("vertebrado")) {
            if (word2.equals("ave")) {
                if (word3.equals("carnivoro")) System.out.println("aguia");
                else System.out.println("pomba");
            } else {
                if (word3.equals("onivoro")) System.out.println("homem");
                else System.out.println("vaca");
            }
        }
        else{
            if (word2.equals("inseto")){
                if (word3.equals("hematofago")) System.out.println("pulga");
                else System.out.println("lagarta");
            }
            else{
                if (word3.equals("hematofago")) System.out.println("sanguessuga");
                else System.out.println("minhoca");
            }
        }
    }
}
