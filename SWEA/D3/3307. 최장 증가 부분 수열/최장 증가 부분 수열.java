import sun.applet.Main;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int T = Integer.parseInt(st.nextToken());

        for (int tc = 1; tc < T+1; tc++) {
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int[] data = new int[N];
            
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                data[i] = Integer.parseInt(st.nextToken());
            }

            int[] dp = new int[N];
            Arrays.fill(dp,1);
            //LIS 수행

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < i; j++) {
                    if (data[i] > data[j]){
                        dp[i] = Math.max(dp[i],dp[j]+1);
                    }
                }
            }
            

            Arrays.sort(dp);

            System.out.println("#"+tc+" "+dp[N-1]);
            
            
            
            
        }


    }
}
