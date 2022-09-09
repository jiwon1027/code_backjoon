
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;


public class Main {
	static int R,C,N;
	static char[][] board;
	static int[] dx = {0,1,-1,0,0};
	static int[] dy = {0,0,0,1,-1};
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] input = br.readLine().split(" ");
		
		R = Integer.parseInt(input[0]);
		C = Integer.parseInt(input[1]);
		N = Integer.parseInt(input[2]);

		board = new char[R][C];
		
		for (int i = 0; i < R; i++) {
			String row = br.readLine();
			for (int j = 0; j < C; j++) {
				board[i][j] = row.charAt(j);
			}
		}
		
		N--;
		while (N>0){
			Queue<int[]> queue = new ArrayDeque<>();
			search(queue);
			putBomb();
			
			N--;
			if (N==0)
				break;
			BoomBomb(queue);
			N--;
		}
		
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				System.out.print(board[i][j]);
			}
			System.out.println();
		}
		
		
	}
	
	
	public static void search(Queue<int[]> queue) {
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (board[i][j] == 'O')
					queue.add(new int[] {i,j});
			}
		}
	}
	
	public static void putBomb() {
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (board[i][j] == '.')
					board[i][j] = 'O';
			}
		}
	}
	
	
	
	public static void BoomBomb(Queue<int[]> queue) {
		while(!queue.isEmpty()) {
			int[] poll = queue.poll();
			int x = poll[0];
			int y = poll[1];
			for (int k = 0; k < 5; k++) {
				int nx = x+dx[k];
				int ny = y+dy[k];
				
				if (0<=nx && 0<=ny && nx<R && ny<C && board[nx][ny]=='O') {
					board[nx][ny] = '.';
				}
			}
		}

	}
	

}
