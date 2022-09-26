
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {
	static int[] price, data, dp;
	static int res;
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		
		for (int i = 1; i < T+1; i++) {
			price = new int[4];
			data = new int[13];
			dp = new int[13];

			String[] input = br.readLine().split(" ");
			for (int j = 0; j < 4; j++) {
				price[j] = Integer.parseInt(input[j]);
			}
			
			input = br.readLine().split(" ");
			for (int j = 1; j < 13; j++) {
				data[j] = Integer.parseInt(input[j-1]);
			}
			res = price[3];
			
			
			
			for (int j = 1; j < 13; j++) {
				int day = data[j] * price[0] + dp[j-1];
				int month_1 = price[1] + dp[j-1];
				dp[j] = Math.min(day, month_1);
				
				if (j>=3) {
					int month_3 = price[2] + dp[j-3];
					dp[j] = Math.min(dp[j], month_3);
				}
			}
			
			System.out.println("#"+i+" "+Math.min(dp[12], price[3]));
			
			
			
		}
				
	}
	

}
