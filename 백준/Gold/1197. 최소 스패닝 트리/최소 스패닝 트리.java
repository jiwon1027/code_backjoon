import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/* 정점 V의 최대 개수 10,000 => 최대로 나올 수 있는 간선 10^8 / 2
 * but, 문제에서 10^5로 제한
 * 크루스칼을 쓰는게 좋아보임
 * 하지만 프림도 사용가능
 */

public class Main {
	static int V,E;
	static int[] parent;
	static int[][] data;
	public static void main(String[] args) throws IOException {
	    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	    StringTokenizer st = new StringTokenizer(br.readLine());
	    V = Integer.parseInt(st.nextToken());
	    E = Integer.parseInt(st.nextToken());
	    
	    parent = new int[V+1]; //index 1부터 시작하고 싶어서 V+1
	    data = new int[E][3]; //row : 간선의 수, col : from, to, cost
	    
	    for (int i = 0; i < E; i++) {
	    	st = new StringTokenizer(br.readLine());
	    	for (int j = 0; j < 3; j++) {
				data[i][j] = Integer.parseInt(st.nextToken());
			}
		}
	    
	    
	    Arrays.sort(data, (o1,o2) -> (o1[2] - o2[2])); //cost에 대해 오름차순

	    make();
	    
	    int res = 0;
	    int cnt = 0;
	    // 크루스칼 시작
	    // 오름차순된 간선들을 모두 살펴보면서 그리디 진행
	    for(int[] row:data) {
	    	if(cnt == V-1)
	    		break;
	    	
	    	if (union(row[0],row[1])) {
	    		res += row[2];
	    		cnt++;
	    	}
	    		
	    }
	    
	    System.out.println(res);
	    
	    
	}
	
	public static void make() {
		for (int i = 1; i < V+1; i++) {
			parent[i] = i;
		}
	}
	
	//경로 압축해서 표현한 find()
	public static int find(int x) {
		if (parent[x] != x)
			parent[x] = find(parent[x]);
		return parent[x];
	}
	
	//union
	public static boolean union(int x, int y) {
		int rootA = find(x);
		int rootB = find(y);
		
		//서로의 루트가 같다는건 사이클이 돈다는거니까 false
		if (rootA == rootB)
			return false;
		
		//서로 다르다면 union을 해주고 true
		if (rootA<rootB)
			parent[rootB] = rootA;
		else
			parent[rootA] = rootB;
		return true;
	}
	

}
