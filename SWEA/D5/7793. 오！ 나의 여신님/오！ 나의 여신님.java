import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution {
    static int N,M;
    static char[][] board;
    static int[] dx = {1,-1,0,0};
    static int[] dy = {0,0,1,-1};

    static Queue<int[]> devilQueue;
    static Queue<int[]> personQueue;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());

        for (int tc = 1; tc < T+1; tc++) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());

            devilQueue = new ArrayDeque<>();
            personQueue = new ArrayDeque<>();
            board = new char[N][M];

            for (int i = 0; i < N; i++) {
                String input = br.readLine();
                for (int j = 0; j < M; j++) {
                    board[i][j] = input.charAt(j);
                    if (board[i][j] == 'S'){
                        personQueue.add(new int[]{i,j,0});
                    }
                    else if (board[i][j] == '*'){
                        devilQueue.add(new int[]{i,j});
                    }
                }
            }

            int res = bfs();

            if (res == -1)
                System.out.println("#"+tc+" GAME OVER");
            else
                System.out.println("#"+tc+" "+res);


        }
    }

    public static int bfs(){
        while (!personQueue.isEmpty()){
            //악마 이동
            int length = devilQueue.size();
            for (int i = 0; i < length; i++) {
                int[] poll_data = devilQueue.poll();
                int x = poll_data[0];
                int y = poll_data[1];
                for (int j = 0; j < 4; j++) {
                    int nx = x + dx[j];
                    int ny = y + dy[j];
                    if (nx<0 || ny<0 || nx>=N || ny>=M)
                        continue;
                    if (board[nx][ny] == '.' || board[nx][ny] == 'S'){
                        board[nx][ny] = '*';
                        devilQueue.add(new int[]{nx,ny});
                    }
                }
            }

            //사람 이동
            length = personQueue.size();
            for (int i = 0; i < length; i++) {
                int[] poll_data = personQueue.poll();
                int x = poll_data[0];
                int y = poll_data[1];
                int cnt = poll_data[2];

                for (int j = 0; j < 4; j++) {
                    int nx = x + dx[j];
                    int ny = y + dy[j];

                    if (nx<0 || ny<0 || nx>=N || ny>=M)
                        continue;

                    if (board[nx][ny] == 'D')
                        return cnt+1;


                    if (board[nx][ny] == '.'){
                        board[nx][ny] = 'S';
                        personQueue.add(new int[]{nx,ny,cnt+1});
                    }
                }
            }
        }
       return -1;
    }


    public static void print(){
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                System.out.print(board[i][j]+" ");
            }
            System.out.println();
        }
        System.out.println();
    }



}
