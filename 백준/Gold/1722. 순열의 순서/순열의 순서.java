

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	static int n;
	static int[] data;
	static boolean[] visited;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		visited = new boolean[n+1];
		data = new int[n];

		long[] dp = new long[n+1];
		dp[0] = 1;
		for (int i = 1; i < n+1; i++) {
			dp[i] = dp[i-1] * i;
		}
		
		
		String[] input = br.readLine().split(" ");
		int kind = Integer.parseInt(input[0]);
		
		if (kind==1) {
			long k = Long.parseLong(input[1]);
			for (int i = 0; i < n; i++) {
				for (int j = 1; j < n+1; j++) {
					if (visited[j])
						continue;
					if(dp[n-i-1] < k)
						k -= dp[n-i-1];
					else {
						data[i] = j;
						visited[j] = true;
						break;
					}
				}
			}
			
			
			for (int i = 0; i < n; i++) {
				System.out.print(data[i]+" ");
			}
		}
		else {
			for (int i = 0; i < n; i++) {
				data[i] = Integer.parseInt(input[i+1]);
			}
			
			long res = 1;
			
			for (int i = 0; i < n; i++) {
				for (int j = 1; j < data[i]; j++) {
					if(visited[j])
						continue;
					res += dp[n-i-1];
				}
				visited[data[i]] = true;
			}
			System.out.println(res);
		}
	
	}

}
