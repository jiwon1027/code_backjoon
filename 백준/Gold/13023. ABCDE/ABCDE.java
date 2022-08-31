import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	static int N,M;
	static List<Integer>[] list;
	static boolean[] visited;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		list = new ArrayList[N];
		for (int i = 0; i < N; i++) 
			list[i] = new ArrayList<>();
		
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			list[a].add(b);
			list[b].add(a);
		}
		
		for (int i = 0; i < N; i++) {
			visited = new boolean[N];
			dfs(i,0);
		}
		
		System.out.println(0);
		
		
	}
	
	 public static void dfs(int x, int depth) {
	        if(depth == 4) {
	            System.out.println(1);
	            System.exit(0);
	        }
	        
	        visited[x] = true;
	        for(int i = 0; i < list[x].size(); i++) {
	            int temp = list[x].get(i);
	            
	            if(!visited[temp]) {
	                dfs(temp, depth + 1);
	                visited[temp] = false;
	            }
	        }
	    }

}
