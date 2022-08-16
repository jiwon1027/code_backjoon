import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;

public class Main{

	public static void main(String[] args) throws  IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		int[][] data = new int[t][2];
		
		for (int i = 0; i < t; i++) {
			String[] input = br.readLine().split(" ");
			data[i][0] = Integer.parseInt(input[0]);
			data[i][1] = Integer.parseInt(input[1]);
		}
		
		Arrays.sort(data, new Comparator<int[]>() {
			@Override
			public int compare(int[] o1, int[] o2) {
				if (o1[1] == o2[1])
					return o1[0]-o2[0];
				return o1[1] - o2[1];
			}
			
		});
		
		int last = 0;
		int res = 0;
		
		for(int[] row:data) {
			if (row[0] >= last) {
				res++;
				last = row[1];
			}
		}
		
		System.out.println(res);
			
		
		
		
		
		
		
	}

}
