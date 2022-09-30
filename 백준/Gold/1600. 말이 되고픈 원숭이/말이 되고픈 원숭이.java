
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main{
	static int[][] board;
	static boolean[][][] visited;
	static int[] dx = {1,-1,0,0};
	static int[] dy = {0,0,1,-1};
	static int[] knight_dx = {-2,-1,1,2,2,1,-1,-2};
	static int[] knight_dy = {1,2,2,1,-1,-2,-2,-1};
	static int N,M,K;
	
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		K = Integer.parseInt(st.nextToken());
		
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		board = new int[M][N];
		visited = new boolean[M][N][K+1];
		
		
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());	
			for (int j = 0; j < N; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		System.out.println(bfs());

	}
	
	public static int bfs() {
		Queue<int[]> queue = new ArrayDeque<>();
		visited[0][0][0] = true;
		queue.add(new int[] {0,0,0,0});
		
		
		while (!queue.isEmpty()) {
			int[] poll_data = queue.poll();
			
			int x = poll_data[0];
			int y = poll_data[1];
			int cnt = poll_data[2];
			int k_cnt = poll_data[3];
			
			
			if (x==M-1 && y==N-1) 
				return cnt;
			
			
			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				if (nx<0 || ny<0 || nx>=M || ny>=N) 
					continue;
				if (board[nx][ny]==1)
					continue;
				if (!visited[nx][ny][k_cnt]) {
					visited[nx][ny][k_cnt] = true;
					queue.add(new int[] {nx,ny,cnt+1,k_cnt});
				}
			}
			if(k_cnt < K) {
			for (int i = 0; i < 8; i++) {
				int nx = x + knight_dx[i];
				int ny = y + knight_dy[i];
				if (nx<0 || ny<0 || nx>=M || ny>=N) 
					continue;
				if (board[nx][ny]==1)
					continue;
				if (!visited[nx][ny][k_cnt+1]) {
					visited[nx][ny][k_cnt+1] = true;
					queue.add(new int[] {nx,ny,cnt+1,k_cnt+1});
				}
			}
			}
		
		}

		return -1;
	}
	
	
	
	
	
	
}
