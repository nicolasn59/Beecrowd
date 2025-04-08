import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner keyboard = new Scanner(System.in);
        int[] nums = new int[3];
        int[] numsCopy = new int[3];
        for (int i=0; i<3; i++){
            nums[i] = keyboard.nextInt();
            numsCopy[i] = nums[i];
        }
        for (int i=0; i<2; i++){
            for (int j=0; j<2; j++){
                if (nums[i] > nums[j+1]){
                    int temp = nums[i];
                    nums[i] = nums[j+1];
                    nums[j+1] = temp;
                }
            }
        }
        for (int i=0; i<3; i++){
            System.out.printf("%d\n", nums[i]);
        }
        System.out.println();
        for (int i=0; i<3; i++){
            System.out.printf("%d\n", numsCopy[i]);
        }
    }
}
