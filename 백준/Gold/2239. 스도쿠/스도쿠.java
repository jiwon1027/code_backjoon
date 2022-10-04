
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
	static int[][] board;
	static List<int[]> list = new ArrayList<>();
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		board = new int[9][9];
		
		for (int i = 0; i < 9; i++) {
			String[] input = br.readLine().split("");
			for (int j = 0; j < 9; j++) {
				board[i][j] = Integer.parseInt(input[j]);
				if (board[i][j] == 0)
					list.add(new int[] {i,j});
				 
			}
		}
		dfs(0);	
		
	}	
	public static boolean rowCheck(int x, int num) {
		for (int i = 0; i < 9; i++) {
			if (board[x][i] == num)
				return false;
		}
		return true;
	}
	
	public static boolean colCheck(int y, int num) {
		for (int i = 0; i < 9; i++) {
			if (board[i][y] == num)
				return false;
		}
		return true;
	}

	public static boolean squareCheck(int x,int y, int num) {
		x = (x/3) * 3;
		y = (y/3) * 3;
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				if (board[x+i][y+j] == num)
					return false;
			}	
		}
		return true;
	}
	
	
	public static void dfs(int depth) {
		if (list.size() == depth) {
			for(int[] row:board) {
				for(int v:row)
					System.out.print(v);
				System.out.println();
			}
			System.exit(0);
		}
		
		int x = list.get(depth)[0];
		int y = list.get(depth)[1];

		for (int num = 1; num < 10; num++) {
			if (rowCheck(x, num) &&  colCheck(y, num) && squareCheck(x, y, num)) {
				board[x][y] = num;
				dfs(depth+1);
				board[x][y] = 0;
			}
		}
	}
}
