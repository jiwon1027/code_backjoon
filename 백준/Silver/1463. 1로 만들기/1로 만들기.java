import java.util.Scanner;

public class Main {

    public static int min(int a, int b) { // 최소값을 구해야 하니까 더 작은것을 return함
        return a > b ? b : a; // import java.lang.Math에서 Math.min을 불러오는 방법도 있당
    }

    public static void main(String[] args) {

        Scanner stdin = new Scanner(System.in);
        int x = stdin.nextInt();
        stdin.close();

        int array[] = new int[x + 1]; // DP를 사용함. 배열의 index는 숫자x를 의미하고 array[x]는 x의 연산 횟수

        array[0] = array[1] = 0;

        for (int i = 2; i <= x; i++) {

            array[i] = array[i - 1] + 1;

            if (i % 3 == 0)
                array[i] = min(array[i], array[i / 3] + 1); // array[i] = array[i/3]+1 연산은 3종류 밖에 없고
                                                            // i의 연산횟수는 i/3의 연산횟수 +1이다.
            if (i % 2 == 0)
                array[i] = min(array[i], array[i / 2] + 1); // 나머지도 그렇게 적용해보자

        }

        System.out.println(array[x]);

        System.exit(0);
    }
}