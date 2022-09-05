
import java.util.Scanner;

public class Main {
	static int N; 
    private static int[] nums = new int[]{1, 5, 10, 50};
    private static boolean[] isVisited = new boolean[1001];
    private static int res = 0;


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        dfs(0, 0, 0);
        System.out.println(res);
    }

    private static void dfs(int depth, int index, int sum) {
        if (depth == N) {
            if (!isVisited[sum]) {
                isVisited[sum] = true;
                res++;
            }
            return;
        }
        for (int i = index; i < 4; i++) {
            dfs(depth + 1, i, sum + nums[i]);
        }
    }
	

}
