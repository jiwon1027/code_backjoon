
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution {
	static List<Integer>[] graph = new ArrayList[101];
	static int[] dp;
	static int L, start, ans;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		for (int tc = 1; tc < 11; tc++) {
			String[] input = br.readLine().split(" ");

			L = Integer.parseInt(input[0]);
			start = Integer.parseInt(input[1]);

			dp = new int[101];

			for (int i = 1; i < 101; i++)
				graph[i] = new ArrayList<>();

			st = new StringTokenizer(br.readLine());

			for (int i = 0; i < L / 2; i++) {
				int from = Integer.parseInt(st.nextToken());
				int to = Integer.parseInt(st.nextToken());

				graph[from].add(to);
			}
			ans = 0;
			bfs();

			System.out.println("#" + tc + " " + ans);

		}

	}

	public static void bfs() {
		Queue<Integer> queue = new ArrayDeque<>();
		queue.add(start);
		dp[start] = 1;

		int res = 0;

		while (!queue.isEmpty()) {
			int temp = queue.poll();

			for (int i = 0; i < graph[temp].size(); i++) {
				int v = graph[temp].get(i);

				if (dp[v] == 0) {
					dp[v] = dp[temp] + 1;
					queue.add(v);
				}
			}

			res = dp[temp];
		}

		for (int i = 1; i < 101; i++) {
			if (dp[i] == res)
				ans = ans < i ? i : ans;
		}

	}

}
