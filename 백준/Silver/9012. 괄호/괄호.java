
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


/*
    1. (만 계속 넣고 ) 만나면 pop
    2.

    stack 비어있는데 ) 들어온경우 바로 종료
 * */


public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            Stack<Integer> stack = new Stack<>();

            String input = br.readLine();
            boolean res = true;

            for (int j = 0; j < input.length(); j++) {
                if (input.charAt(j) == '(') {
                    stack.push(0);
                } else if ((input.charAt(j) == ')') && stack.empty()) {
                    res = false;
                    break;
                } else {
                    stack.pop();
                }
            }

            if (stack.size() > 0) {
                res = false;
            }

            if (res) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }




    }
}