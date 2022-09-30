
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main{

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		
		int[][] board = new int[N][N];
		int[][][] dp = new int[N][N][3];
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
	
		//처음에 맨 위의 줄은 모두 가로가 되니까 dp[0][i][0]=1로 초기화 했는데 벽이 있는 경우를 생각 못했음
		
		dp[0][1][0] = 1;
		
		for (int i = 0; i < N; i++) {
			for (int j = 2; j < N; j++) {
				
				if (board[i][j]==1) //가로
					continue;
				dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2];
				
				if (i==0) //세로
					continue;
				dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2];
				
				if (board[i-1][j]==1 || board[i][j-1]==1) //대각선
					continue;
				dp[i][j][2] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2];
	
			}
		}
	
		
		int res = dp[N-1][N-1][0] + dp[N-1][N-1][1] + dp[N-1][N-1][2];
		
		System.out.println(res);
		
		
	}

}
