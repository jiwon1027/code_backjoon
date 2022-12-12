
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

/*
* 어떤 수 = 다른 수 2개의 합
*
* 수의 위치가 다르면 값이 같아도 다른 수(index로 구분을 해야된다는 의미)
*
* 2000C2 = 2000 * 1999 / 2 = 1,999,000
*
* */

public class Main {
    static int N, res;
    static long[] data;
    static boolean[] visited;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        data = new long[N];
        visited = new boolean[N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            data[i] = Long.parseLong(st.nextToken());
        }

        combi(0,0,new long[2], new int[2]);

        System.out.println(res);

    }

    private static void combi(int start, int depth, long[] selected, int[] index){
        if (depth == 2){

//            System.out.println(Arrays.toString(selected));
//            System.out.println(Arrays.toString(index));

            long sum = selected[0] + selected[1];


            for (int i = 0; i < N; i++) {
                if (!visited[i] && data[i] == sum){
                    if (i == index[0] || i == index[1])
                        continue;

                    visited[i] = true;
                    res++;
                }
            }

            return;
        }


        for (int i = start; i < N; i++) {
            selected[depth] = data[i];
            index[depth] = i;
            combi(i+1, depth+1, selected, index);
        }

    }


}
