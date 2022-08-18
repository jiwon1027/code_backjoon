import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main{
	static char[][] data;
	static boolean[][] visited;
	static int r,c;
	static int[] dx = {-1,0,1};
	
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] input = br.readLine().split(" ");
		r = Integer.parseInt(input[0]);
		c = Integer.parseInt(input[1]);
		
		data = new char[r][c];
		visited = new boolean[r][c];

		for (int i = 0; i < r; i++) {
			input = br.readLine().split("");
			for (int j = 0; j < c; j++) {
				data[i][j] = input[j].charAt(0);
			}
		}
		
		int res = 0;
		
		for (int i = 0; i < r; i++) {
			if( data[i][0] == '.') {
				if (dfs(i,0))
					res++;
			}
		}
		
		System.out.println(res);
		
		
	}
	
	public static boolean dfs(int x, int y) {
		if (y==c-1)
			return true;
		
		for(int i:dx) {
			if ((0<=x+i) && (x+i<r) && data[x+i][y+1] == '.') {
				if (!visited[x+i][y+1]) {
					visited[x+i][y+1] = true;
					if (dfs(x+i,y+1))
						return true;
				}
			}
		}
		
		return false;
	}
	

}
