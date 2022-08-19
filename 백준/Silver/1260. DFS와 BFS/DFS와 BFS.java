import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Queue;

public class Main {
	static List<List<Integer>> board;
	static boolean[] visited;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] input = br.readLine().split(" ");

		int n = Integer.parseInt(input[0]);
		int m = Integer.parseInt(input[1]);
		int v = Integer.parseInt(input[2]);

		board = new ArrayList<>();
		visited = new boolean[n + 1];

		for (int i = 0; i < n + 1; i++)
			board.add(new ArrayList<>());

		for (int i = 0; i < m; i++) {
			input = br.readLine().split(" ");
			board.get(Integer.parseInt(input[0])).add(Integer.parseInt(input[1]));
			board.get(Integer.parseInt(input[1])).add(Integer.parseInt(input[0]));

		}

		for (List<Integer> row : board) {
			Collections.sort(row);
		}

//		for(List<Integer> row:board) {
//			for(int x:row)
//				System.out.print(x+" ");
//			System.out.println();
//		}

		dfs(v);
		System.out.println();
		bfs(v);

	}

	public static void dfs(int v) {
		visited[v] = true;
		System.out.print(v + " ");
		for (int x : board.get(v)) {
			if (!visited[x])
				dfs(x);
		}
	}

	public static void bfs(int v) {
		Queue<Integer> queue = new ArrayDeque<>();
		queue.add(v);
		visited[v] = false;

		while (!queue.isEmpty()) {
			int temp = queue.poll();
			System.out.print(temp + " ");
			for (int x : board.get(temp)) {
				if (visited[x]) {
					queue.add(x);
					visited[x] = false;
				}
			}

		}

	}

}
