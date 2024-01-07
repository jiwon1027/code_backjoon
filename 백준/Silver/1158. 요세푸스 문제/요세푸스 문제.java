
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


/*
    원형은 Queue를 써서 한번 읽은거 다시 뒤로 보내서 다시 확인 가능

 * */


public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] input = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        int N = input[0];
        int K = input[1];

        Queue<Integer> queue = new ArrayDeque<>();
        List<Integer> list = new ArrayList<>();

        for (int i = 1; i < N + 1; i++) {
            queue.add(i);
        }

        int t = 0;

        while (queue.size() > 0) {
            t += 1;

            if (t == K) {
                list.add(queue.poll());
                t = 0;

            } else {
                queue.add(queue.poll());
            }
        }

        System.out.print("<");
        for (int i = 0; i < N; i++) {
            System.out.print(list.get(i));
            if (i != N - 1) {
                System.out.print(", ");
            }
        }
        System.out.print(">");

    }
}