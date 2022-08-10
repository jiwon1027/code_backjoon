import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
	static int[] dx = {-1,1,0,0};
	static int[] dy = {0,0,1,-1};
	static List<String> res;
	static String[][] data;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		data = new String[5][5];
		
		for (int i = 0; i < 5; i++) {
			String[] input = br.readLine().split(" ");
			for (int j = 0; j < 5; j++) {
				data[i][j] = input[j];
			}
		}
		
		res = new ArrayList<>();
		
		for (int i = 0; i < 5; i++) {
			for (int j = 0; j < 5; j++) {
				dfs(i,j,data[i][j]);
			}
		}
		
		System.out.println(res.size());
		
		
	}
	
	public static void dfs(int x, int y, String value) {
		if (value.length() == 6) {
			if (!res.contains(value))
				res.add(value);
			return;
		}
		
		
		
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			
			if ((0<=nx) && (0<=ny) && (nx<5) && (ny<5))
				dfs(nx,ny,value+data[nx][ny]);
			
		}
	}

}
