import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
	static List<int[]> cctv_list = new ArrayList<int[]>();
	static int[] dx = {0,0,1,-1};
	static int[] dy = {1,-1,0,0};
	static int n,m;
	static int res = Integer.MAX_VALUE;
	static int[][][] direction = {
			{},
			{{0},{1},{2},{3}},
			{{0,1},{2,3}},
			{{0,3},{1,3},{1,2},{0,2}},
			{{0,1,3},{1,2,3},{0,1,2},{0,2,3}},
			{{0,1,2,3}}
	};
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] input = br.readLine().split(" ");
		n = Integer.parseInt(input[0]);
		m = Integer.parseInt(input[1]);
		int[][] board = new int[n][m];
		
		for (int i = 0; i < n; i++) {
			input = br.readLine().split(" ");
			for (int j = 0; j < m; j++) {
				if (1<=Integer.parseInt(input[j]) && (Integer.parseInt(input[j])<=5))
					cctv_list.add(new int[] {i,j,Integer.parseInt(input[j])});
				board[i][j] = Integer.parseInt(input[j]);
				
			}
		}
		
		dfs(board,0);		
		System.out.println(res);
	}
	
	public static void dfs(int[][]board, int depth) {
		
		int[][] board_temp = new int[n][m];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				board_temp[i][j] = board[i][j];
			}
		}
		
		if (depth == cctv_list.size()) {
			int cnt = 0;
			for(int[]row:board_temp) {
				for(int v:row) {
					if (v == 0)
						cnt++;
				}
			}
			res = Math.min(res, cnt);
				
		} else {
			int x = cctv_list.get(depth)[0];
			int y = cctv_list.get(depth)[1];
			int cctv = cctv_list.get(depth)[2];
			
			for(int[] temp:direction[cctv]) {
				watch(x,y,temp,board_temp);
				dfs(board_temp,depth+1);
				for (int i = 0; i < n; i++) {
					for (int j = 0; j < m; j++) {
						board_temp[i][j] = board[i][j];
					}
				}
				
			}		
		}
	}
	
	public static void watch(int x, int y, int[] direct, int[][] board) {
		for(int idx:direct) {
			int nx = x;
			int ny = y;
			while (true) {
				nx += dx[idx];
				ny += dy[idx];
				if ((0<=nx) && (0<=ny) && (nx<n) && (ny<m) && (board[nx][ny] !=6)) {
					if (board[nx][ny] == 0)
						board[nx][ny] = -1;
				}
				else
					break;
			}
		}
		
	}
	
	

}
