import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;
/* 플로이드-와샬 써서 모든노드 to 모든노드 써서 쉽게 해보려고 했지만 가중치를 구하는 과정에서 
 * 어짜피 벽때문에 단순히 맨해튼 거리로 안구해져서 BFS로 차근차근 해보는게 낫다는 생각을 했음
 * 
 * 
 * 
 * 
 * */
public class Main {
	static int[][] board,from,to;
	static int[] dx = {0,0,1,-1};
	static int[] dy = {1,-1,0,0};
	static int n,m,fuel,start_x,start_y;
	static boolean[] visited;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		fuel = Integer.parseInt(st.nextToken());
		
		board = new int[n][n];
		visited = new boolean[m];
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		st = new StringTokenizer(br.readLine());
		start_x = Integer.parseInt(st.nextToken())-1; //index 1부터 시작한다고함
		start_y = Integer.parseInt(st.nextToken())-1;

		from = new int[m][2];
		to = new int[m][2];
		
		
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			from[i][0] = Integer.parseInt(st.nextToken())-1;
			from[i][1] = Integer.parseInt(st.nextToken())-1;
			to[i][0] = Integer.parseInt(st.nextToken())-1;
			to[i][1] = Integer.parseInt(st.nextToken())-1;
		}
		

		
		System.out.println(func());
		
	}
	
	public static int func() {

		int s_x = start_x;
		int s_y = start_y;
			

		
		for (int z = 0; z < m; z++) {

			int min_dist = Integer.MAX_VALUE;
			int min_dist_x = 23;
			int min_dist_y = 23;
			int dest_index = -1;
			//어떤 손님을 태울지 하나씩 살펴보기
			for (int i = 0; i < m; i++) {
				
				if(visited[i]) {
					continue;

				}
				int e_x = from[i][0];
				int e_y = from[i][1];

				int move_dist = bfs(s_x,s_y,e_x,e_y);
				if (move_dist == min_dist) { //최단 거리가 똑같을 경우
					if (min_dist_x == e_x) { //행 똑같으면 
						if (min_dist_y>=e_y) { //열 작은거 선택
							min_dist_x = e_x;
							min_dist_y = e_y;
							dest_index = i;
							min_dist = move_dist;

						}
					}
					
					else if (min_dist_x>e_x) { //행 똑같으면
						min_dist_x = e_x;
						min_dist_y = e_y;
						dest_index = i;
						min_dist = move_dist;

					}	
				}
				
				else if (move_dist < min_dist) {//최단거리 일 때
					min_dist_x = e_x;
					min_dist_y = e_y;
					min_dist = move_dist;
					dest_index = i;
				} 
			}
			


			if (dest_index == -1 || fuel<min_dist) {
				fuel = -1;
				break;
			}
			

			
			//경로수정
			s_x = min_dist_x;
			s_y = min_dist_y;
			fuel -= min_dist;
			visited[dest_index] = true;


			// 선택한 손님의 도착지로 이동
			int curmove = bfs(s_x,s_y,to[dest_index][0],to[dest_index][1]);


			
			if (fuel<curmove) {
				fuel = -1;
				break;
			}
			
			s_x = to[dest_index][0];
			s_y = to[dest_index][1];
			fuel += curmove;

		}
		
		return fuel;
		
	}
	
	
	public static int bfs(int from_x, int from_y, int to_x, int to_y) {
		int res = Integer.MAX_VALUE;
		boolean[][] visited = new boolean[n][n];
		visited[from_x][from_y] = true;
		Queue<int[]> queue = new ArrayDeque<>();
		
		queue.add(new int[] {from_x,from_y, 0});
		
		while(!queue.isEmpty()) {
			int[] poll_data = queue.poll();
			
			if (poll_data[0] == to_x && poll_data[1]==to_y) {
				res = poll_data[2];
				break;
			}
			
			for (int i = 0; i < 4; i++) {
				int nx = poll_data[0] + dx[i];
				int ny = poll_data[1] + dy[i];
				if (0<=nx && 0<=ny && nx<n && ny<n) {
					if(!visited[nx][ny] && board[nx][ny] == 0) {
						visited[nx][ny] = true;
						queue.add(new int[] {nx,ny,poll_data[2]+1});
					}
				}

			}
			
		}
	
		return res;
	}
	
	
	

}
