import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);
        int length[] = new int[9];

        int sum = 0;
        int sumtemp;
        for (int i = 0; i < 9; i++) {
            length[i] = stdin.nextInt();
            sum += length[i];
        }
        stdin.close();

        sumtemp = sum;
        Arrays.sort(length);

        int temp1 = -1;
        int temp2 = -1;

        for (int i = 0; i < 8; i++) {
            for (int j = i + 1; j < 9; j++) {
                sum = sum - (length[i] + length[j]);
                if (sum == 100) {
                    temp1 = i;
                    temp2 = j;
                }
                sum = sumtemp;
            }
        }

        for (int i = 0; i < 9; i++) {
            if (i != temp1 && i != temp2)
                System.out.println(length[i]);
        }
        System.exit(0);

    }
}