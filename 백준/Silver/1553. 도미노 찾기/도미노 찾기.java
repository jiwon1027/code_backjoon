import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
/*
 * 모든경우 완탐이다 --> dfs
 * 2차원배열탐색이고 방향은 오->아 2개면 될 거같은데
 * 이게 0,0 -> 7,6 하나 만들어지면 res+=1이니까 모두 끝났을 때 return 1하면서 쌓이는 구조인듯?
 * 
 * dfs진행은 어케하냐
 * start자리 방문했으면 start오른쪽 ㄱㄱ
 * 방문 안했으면 거기 시작지점으로 두고 오,아 모두 완탐 해야됨
 * 근데 그 마저도 방문해야될듯?
 * 
 * */
	
	
	static int[][] board;
	static int[] dx = { 0, 1 };
	static int[] dy = { 1, 0 };
	static boolean[][] visited, isSelected;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		board = new int[8][7];

		for (int i = 0; i < 8; i++) {
			String[] input = br.readLine().split("");
			for (int j = 0; j < 7; j++) {
				board[i][j] = Integer.parseInt(input[j]);
			}

		}

		visited = new boolean[8][7];
		isSelected = new boolean[7][7];

		System.out.println(dfs(0, 0));

	}

	public static int dfs(int x, int y) {

		if (x == 8 && y == 0)
			return 1;

		int cnt = 0;
		int temp_x = x; // 오->아 순서로
		int temp_y = y + 1;

		// 오른쪽 경계값 넘어갈 수 있음
		if (temp_y == 7) {
			temp_x = x + 1;
			temp_y = 0;
		}

		if (visited[x][y]) {
			return dfs(temp_x, temp_y);
		} else {
			visited[x][y] = true;
			int one_domino = board[x][y];
			// 재귀
			for (int i = 0; i < 2; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];

				if (nx < 8 && ny < 7 && !visited[nx][ny]) {
					int two_domino = board[nx][ny];

					if (!isSelected[one_domino][two_domino]) {
						isSelected[one_domino][two_domino] = true;
						isSelected[two_domino][one_domino] = true;

						visited[nx][ny] = true;
						cnt += dfs(temp_x, temp_y);
						visited[nx][ny] = false;

						isSelected[one_domino][two_domino] = false;
						isSelected[two_domino][one_domino] = false;

					}
				}
			}

			visited[x][y] = false;
			return cnt;
		}

	}

}
