import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int N, M;
    static char[][] map;
    static point player;
    static boolean [][][] visited;
    static int[] dx= {-1,1,0,0};
    static int[] dy= {0,0,-1,1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        map = new char[N][M];
        visited = new boolean[N][M][64];

        for (int i = 0; i < N; i++) {
            String temp = br.readLine();
            for (int j = 0; j < M; j++) {
                map[i][j]=temp.charAt(j);

                if(map[i][j]=='0')
                    player = new point(i,j,0,0);
            }
        }
        bfs();

    }
    private static void bfs() {
        Queue<point> q = new LinkedList<>();
        q.add(new point(player.x,player.y,player.k,player.cnt));
        visited[player.x][player.y][0] =true;
        while(!q.isEmpty()) {
            point temp = q.poll();
            int x = temp.x;
            int y = temp.y;
            int cnt = temp.cnt;
            int key = temp.k;

            if (map[x][y] == '1') {
                System.out.println(cnt);
                return;
            }

            for (int k = 0; k < 4; k++) {
                int nx = x + dx[k];
                int ny = y + dy[k];
                if(nx<0 || ny<0 || nx>=N || ny>=M )
                    continue;
                if(map[nx][ny]=='#' || visited[nx][ny][key])
                    continue;
                if(map[nx][ny]>='a' && map[nx][ny]<='f') {
                    int tkey = key | (1<<(map[nx][ny]-'a')) ;

                    if(!visited[nx][ny][tkey]) {
                        visited[nx][ny][tkey] = true;
                        visited[nx][ny][key] = true;
                        q.add(new point(nx, ny, tkey, cnt+1));
                    }
                }else if(map[nx][ny] >= 'A' && map[nx][ny] <= 'F' ) {
                    int door = key & (1<<(map[nx][ny])-'A');

                    if(door>0) {
                        visited[nx][ny][key] = true;
                        q.add(new point(nx, ny, key, cnt+1));
                    }
                }else {
                    visited[nx][ny][key] = true;
                    q.add(new point(nx, ny, key, cnt+1));
                }
            }
        }
        System.out.println(-1);
    }
    static class point{
        int x;
        int y;
        int k;
        int cnt;
        public point(int x, int y, int k,int cnt) {
            this.x = x;
            this.y = y;
            this.k = k;
            this.cnt=cnt;
        }

    }
}