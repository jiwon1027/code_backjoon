
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	static int[][] line_idx_list = {
			{2,3,4,5},{5,7,10,12},{2,6,9,12},{8,9,10,11},{1,3,6,8},{1,4,7,11}
	};
	static boolean[] visited = new boolean[12];
	static boolean checked = false;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int[] data = new int[12];

		int idx = 0;
		
		for (int i = 0; i < 5; i++) {
			String input = br.readLine();
			for (int j = 0; j < 9; j++) {
				if (input.charAt(j) != '.') {
					if (input.charAt(j) == 'x') {
						data[idx++] = -1;
					}
					else {
						data[idx++] = input.charAt(j) - 'A';
						visited[input.charAt(j) - 'A'] = true;
					}
				}
			}
		}


		dfs(0, data);
		
	}
	

	public static void dfs(int depth, int[] data) {

		
		if (depth == 12) {
			if (line_check(data)) {
				draw(data);
				System.exit(0);
				}
			
			return; 
		}
		if(data[depth] != -1) {
			dfs(depth + 1,data);
		}
		else {
			for(int i = 0; i < 12; i++) {
				if(visited[i]) {
					continue;
				}
				data[depth] = i;
				visited[i] = true;
				dfs(depth + 1,data);
				data[depth] = -1;
				visited[i] = false;
			}
		}
	}
	
	public static boolean end_check(int[] data) {
		for (int i = 0; i < 12; i++) {
			if (data[i] == -1)
				return false;
		}
		return true;
	}
	
	public static boolean line_check(int[] data) {
		for (int i = 0; i < 6; i++) {
			int sum = 0;
			for (int j = 0; j < 4; j++) {
				sum += data[line_idx_list[i][j]-1];
			}
			if (sum != 22) //24
				return false;
		}
		return true;
	}
	
	private static void draw(int[] data) {
		int index = 0;
		for(int line = 0; line < 5; line++) {
			if (line == 0 || line == 4) {
				for(int i = 0; i < 9; i++) {
					if(i == 4) {
						System.out.print((char) (data[index++] + 65));
					}
					else {
						System.out.print(".");
					}
				}
			}
			else if(line == 1 || line ==3) {
				for(int i = 0; i < 9; i++) {
					if(i % 2 == 1) {
						System.out.print((char) (data[index++] + 65));
					}
					else {
						System.out.print(".");
					}
				}
			}
			else if(line == 2) {
				for(int i = 0; i < 9; i++) {
					if(i == 2 || i == 6) {
						System.out.print((char) (data[index++] + 65));
					}
					else {
						System.out.print(".");
					}
				}
			}
			System.out.println();
		}
	}

}
