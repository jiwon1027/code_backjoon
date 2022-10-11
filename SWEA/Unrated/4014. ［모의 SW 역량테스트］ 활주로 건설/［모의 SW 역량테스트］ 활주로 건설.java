import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;


/*
* Point: 경사로를 설치해서 높이를 일정하게 하라고 하는건 알겠는데 그럼 어느정도 높이를 맞춰야 활주로를 건설 할 수 있나?
* => 처음부터 끝까지 높이가 일정해지면 그떄 가능. 중간에 끊기면 아예 그 case는 포기해야됨
*
* 따라서 arr[0]부터 시작해서 +1, -1 차이나는 구간에 경사로를 설치할 수 있다는 뜻이니까 거기서
* for x만큼 검사를 해주면서 return false를 판단하면 되는 구현 문제이다.
*
* */

public class Solution {
    static int N,X,res;
    static int[][] board;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int T = Integer.parseInt(st.nextToken());
        for (int tc = 1; tc < T+1; tc++) {
            st = new StringTokenizer(br.readLine());

            N = Integer.parseInt(st.nextToken());
            X = Integer.parseInt(st.nextToken());

            board = new int[N][N];

            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    board[i][j] = Integer.parseInt(st.nextToken());
                }
            }


            res = 0;

            //행 검사
            for (int i = 0; i < N; i++) {
                if (check(board[i])){
                    res++;
                }
            }

            //열 검사
            for (int i = 0; i < N; i++) {
                int[] arr = new int[N];
                for (int j = 0; j < N; j++) {
                    arr[j] = board[j][i];
                }
                if (check(arr)){
                    res++;
                }
            }


            System.out.println("#"+tc+" "+res);

            
        }
    }

    public static boolean check(int[] arr){

        int std = arr[0];
        int cnt = 1; //for문을 1부터 시작하고 있기 때문
        for (int i = 1; i < N; i++) {
            if (arr[i] == std){
                cnt++;
                continue;
            }

            if (arr[i] == std+1){ //cnt에 담았던 개수만큼 판별하면됨, 다시 뒤로 for문 돌릴 필요가 없음
                if (cnt < X)
                    return false;

                std = arr[i];
                cnt = 1; //단순히 cnt로만 판별한 것이고 현재 지금 있는 위치는 std+1자리이니까 얘부터 cnt 고려를 해줘야되기 때문에
            }
            else if (arr[i] == std-1){ //앞으로 for x만큼 공간이 있는지 봐줘야함
                for (int j = 1; j < X; j++) {
                    if ((i+j)>=N || arr[i+j]!=std-1)
                        return false;
                }
                std = arr[i];
                cnt = 0; //for x까지 경사로를 설치했기 때문에 새로 0부터 시작해야됨
                i += X-1;
            }
            else{
                return false;
            }
        }
        return true;
    }

}
