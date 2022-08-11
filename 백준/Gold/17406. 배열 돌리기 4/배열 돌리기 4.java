import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int[][] board, rotate_infor, temp_board;
	static int n, m, k;
	static int res = Integer.MAX_VALUE;

	public static void main(String[] args) throws IOException {
		// 입력
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());

		board = new int[n][m];
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
			}

		}

		rotate_infor = new int[k][3];
		for (int i = 0; i < k; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 3; j++) {
				rotate_infor[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		// 구현

		// permu 돌리기위한 준비
		int[] data = new int[k];
		int[] number = new int[k];
		boolean[] visited = new boolean[k];

		for (int i = 0; i < k; i++) {
			data[i] = i;
		}
		permutation(0, data, number, visited);

		System.out.println(res);

	}

	public static int check_min_row() {
		int total = Integer.MAX_VALUE;
		for (int i = 0; i < n; i++) {
			int row_value = 0;
			for (int j = 0; j < m; j++) {
				row_value += temp_board[i][j];
			}
			total = Math.min(total, row_value);

		}
		return total;
	}

	public static void rotation(int x, int y, int length) {
		List<Integer> list_queue = new ArrayList<>();

		for (int i = y; i < y + length; i++) {
			list_queue.add(temp_board[x][i]);
		}

		for (int i = x + 1; i < x + length; i++) {
			list_queue.add(temp_board[i][y + length - 1]);
		}

		for (int i = y + length - 2; i > y - 1; i--) {
			list_queue.add(temp_board[x + length - 1][i]);
		}
		for (int i = x + length - 2; i > x; i--) {
			list_queue.add(temp_board[i][y]);
		}

		Collections.rotate(list_queue, 1);


		Queue<Integer> queue = new ArrayDeque<>(list_queue);

		for (int i = y; i < y + length; i++) {
			temp_board[x][i] = queue.poll();
		}

		for (int i = x + 1; i < x + length; i++) {
			temp_board[i][y + length - 1] = queue.poll();
		}

		for (int i = y + length - 2; i > y - 1; i--) {
			temp_board[x + length - 1][i] = queue.poll();
		}
		for (int i = x + length - 2; i > x; i--) {
			temp_board[i][y] = queue.poll();
		}

	}

	public static void permutation(int depth, int[] data, int[] number, boolean[] visited) {
		if (depth == k) {
			// 순열이 만들어질 때 마다 rotate돌려서 테스트 해야되니까 기저조건 안에 해보자

			temp_board = new int[n][m];
			for (int idx_i = 0; idx_i < n; idx_i++) {
				for (int idx_j = 0; idx_j < m; idx_j++) {
					temp_board[idx_i][idx_j] = board[idx_i][idx_j];
				}
			}
			
			
			for (int tc : number) {
				int r = rotate_infor[tc][0];
				int c = rotate_infor[tc][1];
				int s = rotate_infor[tc][2];

				int x = r - s - 1;
				int y = c - s - 1;
				int len = (s * 2) + 1;
				while (true) {
					if (len <= 0)
						break;
					rotation(x, y, len);
					x++;
					y++;
					len -= 2;
				}

			}

			res = Math.min(check_min_row(), res);
			return;
		}

		for (int i = 0; i < k; i++) {
			if (!visited[i]) {
				visited[i] = true;
				number[depth] = data[i];
				permutation(depth + 1, data, number, visited);
				visited[i] = false;
			}

		}

	}

}
