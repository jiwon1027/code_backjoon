import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

	static int[][] data;
	static int[] parent;
	static int N,M;
	public static void main(String[] args) throws  IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		M = Integer.parseInt(br.readLine());
		
		data = new int[M+1][3];
		make();
		for (int i = 1; i < M+1; i++) {
			String[] input = br.readLine().split(" ");
			data[i][0] = Integer.parseInt(input[0]);
			data[i][1] = Integer.parseInt(input[1]);
			data[i][2] = Integer.parseInt(input[2]);
		}
		
		Arrays.sort(data, (o1,o2)->(o1[2]-o2[2]));
		
		int res = 0;
		int cnt = 0;
		for(int[] row:data) {
			if (cnt == N-1) {
				break;
			}
			
			if (union(row[0],row[1])) {
				res += row[2];
				cnt++;
			}
		}
		
		System.out.println(res);

		
		
	}
	
	public static void make() {
		parent = new int[N+1];
		for (int i = 1; i < N+1; i++) 
			parent[i] = i;
	}
	
	public static int find(int x) {
		if (parent[x] != x)
			parent[x] = find(parent[x]);
		return parent[x];
	}
	
	public static boolean union(int x, int y) {
		int rootA = find(x);
		int rootB = find(y);
		
		if (rootA == rootB)
			return false;
		if (rootA<rootB)
			parent[rootB] = rootA;
		else
			parent[rootA] = rootB;
		return true;
	}

}
