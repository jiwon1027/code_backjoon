import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	static int[][] board;
	static int n, m, r;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] input = br.readLine().split(" ");
		n = Integer.parseInt(input[0]);
		m = Integer.parseInt(input[1]);
		r = Integer.parseInt(input[2]);

		board = new int[n][m];

		for (int i = 0; i < n; i++) {
			input = br.readLine().split(" ");
			for (int j = 0; j < m; j++) {
				board[i][j] = Integer.parseInt(input[j]);
			}
		}
		
		String[] oper = br.readLine().split(" ");
		
		for(String x:oper) {
			if (x.equals("1"))
				fun1();
			else if (x.equals("2"))
				fun2();
			else if (x.equals("3")) {
				board = fun3(n,m);
				int temp = n;
				n = m;
				m = temp;
			}
			else if (x.equals("4")) {
				board = fun4(n,m);
				int temp = n;
				n = m;
				m = temp;
			}
			else if (x.equals("5"))
				board = fun5();
			else if (x.equals("6"))
				board = fun6();
		

		}
		
		for (int[] row : board) {
			for (int a : row)
				System.out.print(a + " ");
			System.out.println();
		}



	}

	public static void swap(int x1, int y1, int x2, int y2) {
		int temp;
		temp = board[x1][y1];
		board[x1][y1] = board[x2][y2];
		board[x2][y2] = temp;
	}

	public static void fun1() {
		int back_i = n - 1;
		for (int i = 0; i < n / 2; i++) {
			for (int j = 0; j < m; j++) {
				swap(i, j, back_i, j);
			}
			back_i--;
		}
	}

	public static void fun2() {
		for (int i = 0; i < n; i++) {
			int back_j = m - 1;
			for (int j = 0; j < m / 2; j++) {
				swap(i, j, i, back_j);
				back_j--;
			}
		}
	}

	public static int[][] fun3(int n, int m) {
		int[][] temp = new int[m][n];
		for (int i = 0; i < m; i++) {
			for (int j = 0; j < n; j++) {
				temp[i][j] = board[n - 1 - j][i];
			}
		}

		return temp;

	}

	public static int[][] fun4(int n, int m) {
		int[][] temp = new int[m][n];
		for (int i = 0; i < m; i++) {
			for (int j = 0; j < n; j++) {
				temp[i][j] = board[j][m - 1 - i];
			}
		}
		return temp;
	}

	public static int[][] fun5() {
		int[][] temp = new int[n][m];
		// 1->2
		for (int i = 0; i < n / 2; i++) {
			for (int j = 0; j < m / 2; j++) {
				temp[i][j + m / 2] = board[i][j];
			}
		}
		// 2->3
		for (int i = 0; i < n / 2; i++) {
			for (int j = m / 2; j < m; j++) {
				temp[i + n / 2][j] = board[i][j];
			}
		}
		// 3->4
		for (int i = n / 2; i < n; i++) {
			for (int j = m / 2; j < m; j++) {
				temp[i][j - m / 2] = board[i][j];
			}
		}
		// 4->1
		for (int i = n / 2; i < n; i++) {
			for (int j = 0; j < m / 2; j++) {
				temp[i - n / 2][j] = board[i][j];
			}
		}

		return temp;
	}

	public static int[][] fun6() {
		int[][] temp = new int[n][m];
		// 1->4
		for (int i = 0; i < n / 2; i++) {
			for (int j = 0; j < m / 2; j++) {
				temp[i + n / 2][j] = board[i][j];
			}
		}
		// 4->3
		for (int i = n / 2; i < n; i++) {
			for (int j = 0; j < m / 2; j++) {
				temp[i][j + m / 2] = board[i][j];
			}
		}
		// 3->2
		for (int i = n / 2; i < n; i++) {
			for (int j = m / 2; j < m; j++) {
				temp[i - n / 2][j] = board[i][j];
			}
		}
		// 2->1
		for (int i = 0; i < n / 2; i++) {
			for (int j = m / 2; j < m; j++) {
				temp[i][j - m / 2] = board[i][j];
			}
		}
		return temp;

	}

}
