import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);
        int n = stdin.nextInt();
        stdin.close();
        /*
         * 최소값을 구하는 것이기 때문에 5kg를 최대한 구해놓고 나머지값에서 3kg으로 나눠 떨어지는지 확인한다. 만약 3kg로 안떨어지면 5kg를
         * 하나 버리고 5kg를 추가한 나머지 값이 3kg로 나눠 떨어지는지 확인하면 된다.
         */
        int five = n / 5; // 5kg의 개수
        int three = 0; // 3kg의 개수

        n = n % 5;

        while (five >= 0) { // 5kg가 있는상태가 좋으니까 5kg가 있다고 가정한 상태에서 Top-down으로 해보자.
            if (n % 3 == 0) {
                three = n / 3;
                System.out.println(five + three);
                break;
            }
            five--;
            n += 5;
        }

        if (five < 0)
            System.out.println(-1);

    }
}
