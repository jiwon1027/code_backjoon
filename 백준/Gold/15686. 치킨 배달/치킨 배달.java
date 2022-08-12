import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int n, m;
	static Queue<int[]> home = new ArrayDeque<>();
	static List<int[]> all_chicken = new LinkedList<>();
	static Queue<int[]> chicken = new ArrayDeque<>();
	static int[] number;
	static int[] data;
	static int res = Integer.MAX_VALUE;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());

		int[][] board = new int[n][n];

		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++) {
				int temp = Integer.parseInt(st.nextToken());
				board[i][j] = temp;

				if (temp == 1)
					home.add(new int[] { i, j });

				if (temp == 2)
					all_chicken.add(new int[] { i, j });
			}
		}
		
		number = new int[m];
		data = new int[all_chicken.size()];
		
		combi(0, 0);
		System.out.println(res);

	}

	public static void combi(int cnt,int start) {
		if (cnt == m) {
			//치킨집 조합결과에 대해서 집->치킨집들 거리 구하기
			checkien_distance(number);
			return;
		}
		
		for (int i = start; i < all_chicken.size(); i++) {
			number[cnt] = i;
			combi(cnt+1,i+1);
		}
		
		
	}
	
	public static int manhattan_distance(int x1, int y1, int x2, int y2) {
		return Math.abs(x1 - x2) + Math.abs(y1-y2);
	}
	
	public static void checkien_distance(int[] combi_arr) {
		int temp = 0;
		
		for (int[] h:home) {
			int min_temp = Integer.MAX_VALUE;
			for(int com_idx:combi_arr) {
				int temp_distance = manhattan_distance(h[0], h[1], all_chicken.get(com_idx)[0], all_chicken.get(com_idx)[1]);
				min_temp = Math.min(min_temp, temp_distance);
			}
			temp += min_temp;
		}
		
		res = Math.min(res, temp);
	}
	

}
