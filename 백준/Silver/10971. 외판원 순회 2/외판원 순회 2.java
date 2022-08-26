import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int n;
	static int[][] board;
	static boolean[] visited;
	static int start;
	static int res = Integer.MAX_VALUE;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		n = Integer.parseInt(br.readLine());

		board = new int[n][n];
		visited = new boolean[n];

		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		start = 0;
		visited[start] = true;
		dfs(start, 1, 0);

		System.out.println(res);
	}

	static void dfs(int now, int cnt, int total) {
		if (res < total)
			return;

		if (cnt == n && 0 < board[now][start]) {
			total += board[now][start];
			res = Math.min(res, total);
			return;
		}

		for (int i = 0; i < n; i++) {
			if (!visited[i] && 0 < board[now][i]) {
				visited[i] = true;
				dfs(i, cnt + 1, total + board[now][i]);
				visited[i] = false;
			}
		}
	}
}
