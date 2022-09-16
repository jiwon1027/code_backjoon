
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int n,m;
	static List<Integer>[] board;
	static List<Integer> res;
	static int[] data;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
	
		board = new ArrayList[n+1];
		for (int i = 1; i <n+1; i++) {
			board[i] = new ArrayList<>();
		}
		
		data = new int[n+1];
		res = new ArrayList<>();
		for (int i = 0; i < m; i++) {
			String[] input = br.readLine().split(" ");
			
			for (int j = 1; j < Integer.parseInt(input[0]); j++) {
				int from = Integer.parseInt(input[j]);
				int to = Integer.parseInt(input[j+1]);
				board[from].add(to);
				data[to]++;
				}
		}

		bfs();
		
		if(res.size() == n) {
			for(Integer num:res)
				System.out.println(num);
		}
		else
			System.out.println(0);
	}
	
	
	public static void bfs() {
		Queue<Integer> queue = new ArrayDeque<>();
		for (int i = 1; i < n+1; i++) {
			if(data[i]==0)
				queue.add(i);
		}
		
		
		while(!queue.isEmpty()) {
			int v = queue.poll();
			res.add(v);
			
			for(Integer num:board[v]) {
				data[num]--;
				
				if(data[num]==0)
					queue.add(num);
			}
		}
		return;
		
		
	}

}