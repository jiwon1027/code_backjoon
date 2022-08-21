import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main{
	static boolean[] visited;
	static int[][] data;
	static int res;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int c = Integer.parseInt(br.readLine());
		
		for (int tc = 0; tc < c; tc++) {
			data = new int[11][11];
			
			for (int i = 0; i < 11; i++) {
				String[] input = br.readLine().split(" ");
				for (int j = 0; j < 11; j++) {
					data[i][j] = Integer.parseInt(input[j]);
				}
			}
			
			visited = new boolean[11];
			res = 0;
			permutation(0,0);
			System.out.println(res);
		}
	}
	
	public static void permutation(int depth, int stats) {
		if (depth == 11) {
			res = Math.max(res, stats);
			return;
		}
		
		for (int i = 0; i < 11; i++) {
			if (!visited[i] && data[i][depth] != 0) {
				visited[i] = true;
				permutation(depth+1, stats+data[i][depth]);
				visited[i] = false;
			}
		}
		
	}

}
