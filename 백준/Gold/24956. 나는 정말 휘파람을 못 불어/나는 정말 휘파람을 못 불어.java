
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/*
* '유사 휘파람 문자열' -> 'WHEE' + 'E'
* W
* WH
* WHE
* WHEE 하나씩 순차적으로 기억해서 푸는거 아닐까
*
* WHE + E라서 + data[2]
* WHEE + E일수도 있으니 *2
* 맞나?
*
* */
public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        String S = br.readLine();

        long[] data = new long[3];

        long res = 0;

        for (int i = 0; i < S.length(); i++) {
            char x = S.charAt(i);

            if (x == 'W'){
                data[0] += 1;
            } else if (x == 'H'){
                data[1] += data[0];
            } else if (x == 'E') {
                res = (res * 2 + data[2]) % 1000000007;
                data[2] += data[1];
            }
        }

        System.out.println(res);
    }

}
