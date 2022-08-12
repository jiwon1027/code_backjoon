import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;


public class Main {

	public static void main(String[] args) throws  IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int[][] meetings = new int[n][2];
		int cnt = 0;
		PriorityQueue<Integer> pq = new PriorityQueue<>();
		
		for (int i = 0; i < n; i++) {
			String[] input = br.readLine().split(" ");
			for (int j = 0; j < 2; j++) {
				meetings[i][0] = Integer.parseInt(input[0]);
				meetings[i][1] = Integer.parseInt(input[1]);
			}
		}
	
		Arrays.sort(meetings, new Comparator<int[]>() {
			@Override
			public int compare(int[] o1, int[] o2) {
				return o1[0] - o2[0];
			}
		});
		
		
		pq.add(Integer.MAX_VALUE);
		
		for(int[] time:meetings) {
			if (pq.peek() > time[0]) //min-heap이 시작시간보다 크면 회의실 추가
				cnt++;
			else
				pq.poll(); //회의실을 이어서 쓸 수 있다는 거니까 이전의 정보 삭제
			pq.add(time[1]);
		}
		
		
		
		
		System.out.println(cnt);

		
		
	}

}
