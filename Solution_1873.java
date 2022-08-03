package pratice;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution_1873 {
	static char[][] board;
	static int t_x;
	static int t_y;
	static int h;
	static int w;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		// 입력
		int t = Integer.parseInt(br.readLine());
		for (int tc = 1; tc < t + 1; tc++) {
			st = new StringTokenizer(br.readLine());
			h = Integer.parseInt(st.nextToken());
			w = Integer.parseInt(st.nextToken());
			board = new char[h][w];

			for (int i = 0; i < h; i++) {
				board[i] = br.readLine().toCharArray();
			}
			int n = Integer.parseInt(br.readLine());
			String data = br.readLine();

			// 탱크 좌표 구하기
			for (int i = 0; i < h; i++) {
				for (int j = 0; j < w; j++) {
					if ((board[i][j] == '<') || (board[i][j] == '>') || (board[i][j] == 'v') || (board[i][j] == '^')) {
						t_x = i;
						t_y = j;
					}
				}
			}

			for (int i = 0; i < n; i++) {
				if (data.charAt(i) == 'S')
					s_fun();
				else 
					move(data.charAt(i));
				

			}

			System.out.print("#" + tc + " ");
			for (int i = 0; i < h; i++) {
				for (int j = 0; j < w; j++) {
					System.out.print(board[i][j]);
				}
				System.out.println();
			}

		}
	}

	
	public static void t_init(char direct) {
		// map으로 사용하면 더 좋을 것 같음
		if (direct == 'U')
			board[t_x][t_y] = '^';
		else if (direct == 'D')
			board[t_x][t_y] = 'v';
		else if (direct == 'L')
			board[t_x][t_y] = '<';
		else if (direct == 'R') {
			board[t_x][t_y] = '>';
		}
	}
	
	public static void ismove(int temp_x, int temp_y, char direct) {
		t_init(direct);

		if ((0 <= temp_x) && (0 <= temp_y) && (temp_x < h) && (temp_y < w)) {

			if (board[temp_x][temp_y] == '.') {
				board[t_x][t_y] = '.';
				t_x = temp_x;
				t_y = temp_y;
				t_init(direct);
 
			}
		}
	}

	public static void move(char direct) {
		if (direct == 'U') {
			int temp_x = t_x - 1;
			int temp_y = t_y;
			ismove(temp_x, temp_y, direct);

		} else if (direct == 'D') {
			int temp_x = t_x + 1;
			int temp_y = t_y;
			ismove(temp_x, temp_y, direct);

		} else if (direct == 'L') {
			int temp_x = t_x;
			int temp_y = t_y - 1;
			ismove(temp_x, temp_y, direct);

		} else if (direct == 'R') {
			int temp_x = t_x;
			int temp_y = t_y + 1;
			ismove(temp_x, temp_y, direct);
		}

	}

	public static void s_fun() {
		if (board[t_x][t_y]=='^') {
			for (int col = t_x-1; col >=0; col--) {
				if (board[col][t_y] == '#')
					break;
				if (board[col][t_y] == '*') {
					board[col][t_y] = '.';
					break;
				}
			}
		}
			
		else if (board[t_x][t_y]=='v') {
			for (int col = t_x+1; col <h; col++) {
				if (board[col][t_y] == '#')
					break;
				if (board[col][t_y] == '*') {
					board[col][t_y] = '.';
					break;
				}
			}
		}
			
		else if (board[t_x][t_y]=='<') {
			for (int row = t_y-1; row >=0; row--) {
				if (board[t_x][row] == '#')
					break;
				if (board[t_x][row] == '*') {
					board[t_x][row] = '.';
					break;
				}
			}
		}
			
		else if (board[t_x][t_y]=='>') {
			for (int row = t_y+1; row <w; row++) {
				if (board[t_x][row] == '#')
					break;
				if (board[t_x][row] == '*') {
					board[t_x][row] = '.';
					break;
				}
			}
		}
			
		
	}

}
