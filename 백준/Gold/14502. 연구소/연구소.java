import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.Array;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;


/* 벽 3개를 무조껀 세워야함
* 어디에 벽을 세워야 안전영역이 최대로 될까? 바이러스 상하좌우 근처에 놓으면 그게 최대로 될까? => 뭔가 예외상황 있을 느낌 든다
* 그러면 벽을 모든 경우로 세워본다음에 그거 deepcopy 받아서 그걸 bfs돌린다음 최대 안전 구역 하면 될듯?
* 
* 
* 사실 0인 부분의 대한 nP3 순열인데 백트래킹이랑 똑같으니까 백트래킹이라고 하자
* */

public class Main {
    static int N,M,res;
    static int[][] board;
    static int[] dx = {1,-1,0,0};
    static int[] dy = {0,0,1,-1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        board = new int[N][M];


        Queue<int[]> virus = new ArrayDeque<>();


        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        dfs(0);

        System.out.println(res);



    }

    public static void dfs(int depth){
        if (depth == 3){
            bfs();
            return;
        }
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (board[i][j] == 0){
                    board[i][j] = 1;
                    dfs(depth+1);
                    board[i][j] = 0;
                }
            }
        }
    }


    public static int[][] deepcopy(int[][] board){
        int[][] copy_board = new int[N][M];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                copy_board[i][j] = board[i][j];
            }
        }
        return copy_board;
    }


    public static void bfs(){
        int[][] copy_board = deepcopy(board);
        Queue<int[]> queue = new ArrayDeque<>();

        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (copy_board[i][j] == 2)
                    queue.add(new int[]{i,j});
            }
        }


        while (!queue.isEmpty()){
            int[] poll_data = queue.poll();
            int x = poll_data[0];
            int y = poll_data[1];

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx<0 || ny<0 || nx>=N || ny>=M)
                    continue;
                if (copy_board[nx][ny] == 0){
                    copy_board[nx][ny] = 2;
                    queue.add(new int[]{nx,ny});
                }

            }
        }

        int cnt = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (copy_board[i][j] == 0)
                    cnt++;
            }
        }

        res = Math.max(res, cnt);
    }


}
