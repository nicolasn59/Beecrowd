import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner keyboard = new Scanner(System.in);
        int num=97, i=0;
        while (i != 26){
            System.out.printf("%d e %s\n", num, (char)num);
            num += 1;
            i += 1;
        }
    }
}
