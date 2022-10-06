import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main{
    static int R,C;
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};

    static class P {
        int r;
        int c;

        public P(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        int[][] board = new int[R][C];

        int left = 0;

        for (int i = 0; i < R; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < C; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
                if (board[i][j] == 1) left++;
            }
        }

        int time = 0;

        int before = left;

        while (left != 0) {
            before = left;

            bfs(board);

            left = count(board);
            time++;
        }

        System.out.println(time);
        System.out.println(before);
    }

    private static int count(int[][] board) {
        int count = 0;
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (board[i][j] == -1) board[i][j] = 0;
                else if (board[i][j] == 1) count++;
            }
        }
        return count;
    }

    private static void bfs(int[][] board) {
        Queue<P> queue = new ArrayDeque<>();
        queue.add(new P(0, 0));

        boolean[][] visited = new boolean[R][C];
        visited[0][0] = true;

        while (!queue.isEmpty()) {
            P p = queue.poll();

            for (int i = 0; i < 4; i++) {
                int nx = p.r + dx[i];
                int ny = p.c + dy[i];

                if (0 <= nx && nx < R && 0 <= ny && ny < C && board[nx][ny] != -1 && !visited[nx][ny]) {
                    if (board[nx][ny] == 1)
                        board[nx][ny] = -1;
                    else {
                        visited[nx][ny] = true;
                        queue.add(new P(nx, ny));
                    }
                }
            }
        }
    }

}

