import java.util.Scanner;

public class Main {
    static int r, c;
    static int[] dy = {-1, 0, 1, 0}, dx = {0, 1, 0, -1};
    static char[][] s;
    static boolean[] visited;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        r = sc.nextInt(); c = sc.nextInt();
        s = new char[r][c];
        visited = new boolean[26];
        for(int i = 0; i < r; i++)
            s[i] = sc.next().toCharArray();
        visited[s[0][0] - 'A'] = true;
        System.out.println(dfs(0, 0));
    }

    static int dfs(int y, int x) {
        int res = 1;
        for(int i = 0; i < 4; i++) {
        	int nx = x + dx[i];
            int ny = y + dy[i];
            if(ny >= r || nx >= c || ny < 0 || nx < 0 || visited[s[ny][nx] - 'A']) 
            	continue;
            visited[s[ny][nx] - 'A'] = true;
            res = Math.max(res, dfs(ny, nx) + 1);
            visited[s[ny][nx] - 'A'] = false;
        }
        return res;
    }
}