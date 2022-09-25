

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;



public class Main {
	static int n, m;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int[][] map = new int[1001][1001];
    static boolean[][][] visited = new boolean[1001][1001][2];
    
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int Hx = Integer.parseInt(st.nextToken());
        int Hy = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int Ex = Integer.parseInt(st.nextToken());
        int Ey = Integer.parseInt(st.nextToken());

        for(int i=1; i<=n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=1; j<=m; j++)
                map[i][j] = Integer.parseInt(st.nextToken());
        }
        System.out.println(bfs(Hx, Hy, Ex, Ey));
    }
		
	 public static int bfs(int Hx, int Hy, int Ex, int Ey){

        Queue<int[]> queue = new ArrayDeque<>();

        visited[Hx][Hy][0] = true;
        queue.add(new int[] {Hx, Hy, 0, 0});

        while(!queue.isEmpty()){
            int[] poll_data = queue.poll();
            int x = poll_data[0];
            int y = poll_data[1];
            int dist = poll_data[2];
            int use_skill = poll_data[3];

            if(x == Ex && y == Ey)
                return dist;

            for(int i=0; i<4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];

                if(nx < 1 || ny < 1 || nx > n || ny > m || visited[nx][ny][use_skill]) 
                	continue;

                if(map[nx][ny] == 1){
                    if(use_skill == 1) 
                    	continue;
                    else{
                    	visited[nx][ny][1] = true;
                    	queue.add(new int[] {nx, ny, dist + 1, 1});
                    }
                }
                else{
                	visited[nx][ny][use_skill] = true;
                	queue.add(new int[] {nx, ny, dist + 1, use_skill});
                }
            }
        }
        return -1;
    }	
	

}
