
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main{

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] input = br.readLine().split(" ");
		int H = Integer.parseInt(input[0]);
		int W = Integer.parseInt(input[1]);

		int[] data = new int[W];
		
		input = br.readLine().split(" ");
		for (int i = 0; i < W; i++) 
			data[i] = Integer.parseInt(input[i]);
		
		int start = data[0];
		int res = 0;

		
		for (int i = 1; i < W; i++) {
			
			int left = 0;
			int right = 0;
			
			for (int j = i-1; j >=0 ; j--) {
				left = Math.max(left, data[j]);
			}
			for (int j = i+1; j < W; j++) {
				right = Math.max(right, data[j]);
			}
			
			//빗물 못채우는 경우
			if (left > data[i] && right > data[i] ) {
				int std = Math.min(left, right);
				res += std - data[i];
			}
			
		}
		
		System.out.println(res);
		
		
		
	}

}
