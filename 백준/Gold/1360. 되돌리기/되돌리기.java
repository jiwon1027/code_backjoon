
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

/*
* 명령했던 값을 기억했다가 시간에 따라서 포인터가 왔다갔다 하는 개념이라 Deque로 하는거 아닌가? > 모르겠음
* 시간이 흐르면서 a000b00c이런식으로 기억하고 싶지만 10^9이기 때문에 메모리 낭비임
*
* 명령은 최대 50개이기 때문에 명령에 따라서 현재 상태를 저장할 순 있긴한데 어짜피 시간대로 흘러가는데 이게 쓸모가 있으려나
* undo - undo를 보면 한글자씩 back되는게 아니라 명령의 단위로 back이 되는거기 때문에 명령어에 따른 상태를 저장할 필요가 있음
* 현재시간 - time 이전의 상태를 불러오면 된다
*
* */
class Temp{
    int time;
    String str;

    public Temp(int time, String str){
        this.time = time;
        this.str = str;
    }
}


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        String res = "";
        List<Temp> list = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            String cmd = st.nextToken();
            String ch = st.nextToken();
            String t = st.nextToken() ;

            boolean flag = false;

            if (cmd.equals("type")){

                res += ch;
                list.add(new Temp(Integer.parseInt(t), res));
            }
            else{
                int back_time = Integer.parseInt(ch);
                int time = Integer.parseInt(t);

                for (int j = list.size()-1; j >=0 ; j--) {
                    if (list.get(j).time >= (time-back_time)) {
                        continue;
                    }

                    flag = true;
                    res = list.get(j).str;

                    list.add(new Temp(time, res));
                    break;
                    }
                if (!flag){
                    res = "";
                    list.add(new Temp(time, res));
                }
                }


            }
        System.out.println(list.get(list.size()-1).str);

        }

    }

