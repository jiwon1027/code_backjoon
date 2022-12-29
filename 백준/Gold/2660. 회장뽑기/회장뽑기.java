
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[][] data = new int[N+1][N+1];

        int INF = 251;

        for(int i=1;i<=N;i++){
            for(int j=1;j<=N;j++){
                if(i!=j){
                    data[i][j] = INF;
                }
            }
        }

        
        while(true){
            StringTokenizer st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            if(a == -1 && b== -1){
                break;
            }
            data[a][b] = 1;
            data[b][a] = 1;
        }

//        for (int i = 1; i < N+1; i++) {
//            for (int j = 1; j < N+1; j++) {
//                System.out.print(data[i][j] +" ");
//            }
//            System.out.println();
//        }

        for(int k = 1; k < N+1; k++) {
            for(int i = 1; i < N+1; i++) {
                for(int j = 1; j < N+1; j++) {
                    if(data[i][j] > data[i][k] + data[k][j]) {
                        data[i][j] = data[i][k] + data[k][j];
                    }
                }
            }
        }

        int[] score = new int[N + 1];
        int min = Integer.MAX_VALUE;
        
        for(int i = 1; i < N+1; i++) {
            for(int j = 1; j < N+1; j++) {
                score[i] = Math.max(score[i], data[i][j]);
            }
            min = Math.min(min, score[i]);
        }

        List<Integer> list = new ArrayList<>();
        for(int i = 1; i < N+1; i++) {
            if(score[i] == min)
                list.add(i);
        }

        System.out.println(min + " " + list.size());
        for(int temp : list) {
            System.out.print(temp + " ");
        }
    }
}