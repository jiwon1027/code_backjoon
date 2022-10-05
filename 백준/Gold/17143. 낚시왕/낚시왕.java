import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/* 이거 SWEA 미생물 문제랑 똑같음
* 시작지점 : (0,0)
* y >= C면 이동을 멈춤
*
* 1. 오른쪽으로 한칸 이동
* 2. col탐색 하면서 가장 idx가 작은 상어를 잡는다. board에서 상어는 사라짐
* 3. 다른 상어들이 이동
* 
* 상어가 이동하려고 하는 칸이 격자판의 경계를 넘는 경우에는 방향을 반대로 바꿔서 속력을 유지한채로 이동
*크기가 가장 큰 상어가 나머지 상어를 모두 잡아먹는다(그러면 가장 큰 상어를 기준으로 정렬한다음 걔를 기준으로 하면 되지 않을까?)
*
*
*
* */


public class Main {
    static int R,C,M,res;
    static int[][] shark;
    static int[] dx = {-1,1,0,0}; //상하우좌
    static int[] dy = {0,0,1,-1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        shark = new int[M][5];

        //shark : x,y,속력, 방향, 크기, 존재여부
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            int s = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            int z = Integer.parseInt(st.nextToken());
            shark[i] = new int[]{r,c,s,d-1,z,1};
        }

        //가장 큰 상어부터 고려하면 다음 상어가 오더라도 덮어쓰기 가능
        Arrays.sort(shark,(o1, o2) -> (o2[4] - o1[4]));



        for (int i = 1; i < C+1; i++) { //총 C만큼만 이동하니까
            //System.out.println(i+"초");
            List<Integer>[][] board = new ArrayList[R+1][C+1];
            for (int j = 1; j < R+1; j++) {
                for (int k = 1; k < C+1; k++) {
                    board[j][k] = new ArrayList<>();
                }
            }

            //상어 잡기
            PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> (o1[0] - o2[0]));
            for (int j = 0; j < M; j++) {
                if (shark[j][1] == i && shark[j][5]==1){
                    pq.add(shark[j]);
                }
            }
            int[] catch_shark = pq.poll(); //take_shark 위에 값 덮어씌워도 가능(shallow copy라서)
            if (catch_shark != null){
                //System.out.println(Arrays.toString(catch_shark));
                catch_shark[5] = 0;
                res += catch_shark[4];
            }

            //상어 이동
            for (int j = 0; j < M; j++) {
                if (shark[j][5] == 1){ //살아있는 애들만
                    //System.out.println(shark[j][0]+" "+shark[j][1]);
                    int temp_dir = shark[j][3];
                    int temp = temp_dir < 2 ? R : C;
                    int move_length = shark[j][2] % ((temp-1) * 2);

                    //System.out.println("move_length : " + move_length);
                    for (int k = 0; k < move_length; k++) { //전진
                        int dir = shark[j][3];
                        int x = shark[j][0];
                        int y = shark[j][1];

                        int nx = x + dx[dir];
                        int ny = y + dy[dir];
                        //System.out.println("방향 전 : "+dir);

                        if (nx == 0 || ny == 0 || nx == R+1 || ny == C+1){
                            shark[j][3] = reverse_dir(shark[j]);
                            shark[j][0] = x + dx[shark[j][3]];
                            shark[j][1] = y + dy[shark[j][3]];
                            //System.out.println("방향 후 : "+shark[j][3]);
                        }
                        else{
                        shark[j][0] = nx;
                        shark[j][1] = ny;
                        }
                    }
                    //System.out.println(Arrays.toString(shark[j]));
                    //System.out.println();
                    board[shark[j][0]][shark[j][1]].add(j+1);
                }
            }

            //이동을 마친 후에 상어 2마리가 겹친다면?
            for (int j = 1; j < R+1; j++) {
                for (int k = 1; k < C+1; k++) {
                    if (board[j][k].size() > 1){
                        //print();
                        //System.out.println(j+" "+k);
                        //System.out.println("겹친다");

                        for (int l = 1; l < board[j][k].size(); l++) {
                            int index = board[j][k].get(l);
                            //System.out.println(Arrays.toString(shark[index-1]));
                            shark[index-1][5] = 0;
                        }
                    }

                }
            }
            //print();


        }
        System.out.println(res);




    }
    public static void print(){
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < 6; j++) {
                System.out.print(shark[i][j]+" ");
            }
            System.out.println();
        }
    }


    public static int reverse_dir(int[] shark) {
        int dir = shark[3];

        switch (dir){
            case 0:
                shark[3] = 1;
                break;
            case 1:
                shark[3] = 0;
                break;
            case 2:
                shark[3] = 3;
                break;
            case 3:
                shark[3] = 2;
                break;
        }
        return shark[3];
    }
}
