import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int[][] board;
	static int ans, n, m, d, enemy;
	static int[] archer = new int[3];
	static int[] dx = { 0, -1, 0 };
	static int[] dy = { -1, 0, 1 };

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		d = Integer.parseInt(st.nextToken());

		board = new int[n + 1][m];

		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				int temp = Integer.parseInt(st.nextToken());
				if (temp == 1)
					enemy++;
				board[i][j] = temp;
			}
		}

		combi(0, 0);

		System.out.println(ans);

	}

	public static void combi(int depth, int start) {
		if (depth == 3) {
			int[][] board_temp = new int[n + 1][m]; // 깊은복사
			for (int i = 0; i < n + 1; i++) {
				for (int j = 0; j < m; j++) {
					board_temp[i][j] = board[i][j];
				}
			}

			game(board_temp);

			return;
		}

		for (int i = start; i < m; i++) {
			archer[depth] = i;
			combi(depth + 1, i + 1);
		}
	}

	public static int distance(int x, int y, int x1, int y1) {
		return Math.abs(x - x1) + Math.abs(y - y1);
	}

	public static void next_round(int[][] board) {
		for (int i = n; i > 0; i--) {
			for (int j = 0; j < m; j++) {
				board[i][j] = board[i - 1][j];
			}
		}
		for (int i = 0; i < m; i++) {
			board[0][i] = 0; 
		}
	}

	public static boolean end_test(int cnt,int[][] board, int enemy_cnt) {
		if (enemy_cnt == enemy)
			return false;
		else if(cnt == n)
			return false;

		return true;
	}

	public static int attack(int[][] board) {
		int enemy_cnt = 0;

		for (int k = 0; k < 3; k++) {
			boolean[][] visited = new boolean[n + 1][m];
			Queue<int[]> queue = new ArrayDeque<>();

			queue.add(new int[] { n, archer[k], 0 });
			visited[n][archer[k]] = true;
			while (!queue.isEmpty()) {
				int[] poll = queue.poll();

				if (poll[2] > d)
					break;

				if (board[poll[0]][poll[1]] >= 1) {
					board[poll[0]][poll[1]] = 2;
					break;
				}

				for (int i = 0; i < 3; i++) {
					int nx = poll[0] + dx[i];
					int ny = poll[1] + dy[i];
					if ((0 <= nx) && (0 <= ny) && (nx < n) && (ny < m) && !visited[nx][ny]) {
						visited[nx][ny] = true;
						queue.add(new int[] { nx, ny, poll[2] + 1 });
					}
				}
			}
		}

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (board[i][j] == 2) {
					enemy_cnt++;
					board[i][j] = 0;
				}
			}

		}
		return enemy_cnt;
	}

	public static void game(int[][] board) {
		int enemy_cnt = 0;
		int cnt=0;
		while (end_test(cnt++,board, enemy_cnt)) {

			enemy_cnt += attack(board);
			next_round(board);

		}
		ans = Math.max(ans, enemy_cnt);
	}

}
