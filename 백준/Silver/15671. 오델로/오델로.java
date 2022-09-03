import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;
/*
 * 돌 놓은 자리 기준으로 8방 탐색하면서 std 다시 만나면 그걸로 다 바꾸면 되는거 같은데?
 * 돌을 어디다 놓는거 판단하는게 제일 어려웠는데 그걸 입력해서 해주니 괜찮을듯?
 * 만약 저 위치를 찾는 거면 어려웠을듯
 * 
 * 
 * 
 * */
public class Main {
	static int[] dx = {0,1,1,1,0,-1,-1,-1};
	static int[] dy = {1,1,0,-1,-1,-1,0,1};
	
	public static void main(String[] args) throws IOException {
		BufferedReader br =  new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		char[][] board = new char[7][7];
		
		for (int i = 1; i < 7; i++) {
			for (int j = 1; j < 7; j++) {
				board[i][j] = '.';
			}
		}
		
		board[3][3] = board[4][4] = 'W'; //백돌
		board[3][4] = board[4][3] = 'B'; //흑돌

		
		char stone = 'B'; //흑돌이 선
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			
			board[x][y] = stone;
			
			//8방 탐색하면서 돌 뒤집어 줘야함
			for (int j = 0; j < 8; j++) {
				int temp_x = x;
				int temp_y = y;
				
				Queue<int[]> queue = new ArrayDeque<>();
				while (true) {
					int nx = temp_x + dx[j];
					int ny = temp_y + dy[j];
					if(nx<1 || ny<1 || nx>6 || ny>6 || board[nx][ny]=='.')
						break;
					
					else if (board[nx][ny] == stone) {
						while(!queue.isEmpty()) {
							int[] data = queue.poll();
							board[data[0]][data[1]] = stone;
						}
						break;
					}
					
					queue.add(new int[] {nx,ny});
					temp_x = nx;
					temp_y = ny;
	
					}
				}
		
			if (stone == 'B')
				stone = 'W';
			else
				stone = 'B';
		}
		
		
		int white_cnt = 0;
		int black_cnt = 0;
		
		for (int i = 1; i < 7; i++) {
			for (int j = 1; j < 7; j++) {
				if (board[i][j] == 'W')
					white_cnt++;
				else if (board[i][j] == 'B')
					black_cnt++;
				System.out.print(board[i][j]);
			}
			System.out.println();
		}

		System.out.println(white_cnt<black_cnt?"Black":"White");
		
		
		
		
	}
}
