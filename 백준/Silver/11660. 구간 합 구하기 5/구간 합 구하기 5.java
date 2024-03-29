import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		int[][] board = new int[n+1][n+1];

		for (int i = 1; i < n+1; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 1; j < n+1; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		}


		int[][] dp = new int[n+1][n+1];

		for (int i = 1; i < n+1; i++) {
			for (int j = 1; j < n+1; j++) {
				dp[i][j] = dp[i-1][j] + dp[i][j-1] -dp[i-1][j-1] + board[i][j];
			}
		}
		
		for (int k = 0; k < m; k++) {
			st = new StringTokenizer(br.readLine());
			int res = 0;
			
			int x1 = Integer.parseInt(st.nextToken());
			int y1 = Integer.parseInt(st.nextToken());
			int x2 = Integer.parseInt(st.nextToken());
			int y2 = Integer.parseInt(st.nextToken());
			
			res = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1];
			System.out.println(res);
			

		}
		
		
		
		
		
		
		

	}

}
