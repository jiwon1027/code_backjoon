import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

/*
* K개의 글자로만 이루어진 단어만 읽을 수 있음
* 어떤 K개의 글자를 가르쳐야 학생들이 읽을 수 있는 단어의 개수가 최대가 될까
*
* anta - tica
* a:3, c:1, i:1, t:2, n:1
*
* 기본적으로 5글자는 알아야 단어를 읽을 수 있는 권한이 생김
* K<5면 그냥 0
* K>=5라면 어떤 단어를 추가했을 때 가장 적절한지 일일히 확인 해보기
*
* substring으로 일일이 단어를 뺄 수 있고 어떤 알파벳이 필요한지 리스트를 뽑아낼 수 있으며
* 총 몇개 중 K-5개를 뽑았을 떄 그때의 최댓값이니까 조합으로 풀면될 듯?
* 
*
* */

public class Main{
    static int res;
    static int N,K;
    static List<Character> list;
    static String[] data;
    static boolean[] alphabet;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        data = new String[N];
        alphabet = new boolean[26];

        alphabet['a'-'a'] = true;
        alphabet['c'-'a'] = true;
        alphabet['i'-'a'] = true;
        alphabet['t'-'a'] = true;
        alphabet['n'-'a'] = true;

        list = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            String temp = br.readLine();

            int str_length = temp.length();
            data[i] = temp.substring(4, str_length-4);

            for (int j = 0; j < data[i].length(); j++) {
                if (!alphabet[data[i].charAt(j) - 'a']){
                    list.add(data[i].charAt(j));
                    alphabet[data[i].charAt(j) - 'a'] = true;
                }
            }
        }

        for (int i = 0; i < list.size(); i++) {
            alphabet[list.get(i) - 'a'] = false;
        }

        if (K <5)
            System.out.println(0);
        else{
            res = 0;

//            System.out.println(Arrays.toString(data));
//            System.out.println(list.toString());

            if (list.size() <= K-5)
                res = data.length;

            // 여기서 조합을 한다고 치자
            // r을 골랐다고 했으면 r을 골랐을 때 몇개를 알 수 있는지 check()는 어케함?
            // for data해서 5개말고 고른 알파벳이 있다면 res++
            combi(0, 0, new char[K-5]);

            System.out.println(res);
        }
    }

    public static void combi(int start, int depth, char[] select){
        if (depth == (K-5)){

//            System.out.println(Arrays.toString(data));
//            System.out.println(list.toString());

            // visited = true;
            for (int i = 0; i < select.length; i++) {
                alphabet[select[i] - 'a'] = true;
            }

            int cnt = 0;

            for (int i = 0; i < data.length; i++) {
                boolean flag = true;
                for (int j = 0; j < data[i].length(); j++) {
                    if (!alphabet[data[i].charAt(j) - 'a']) {
                        flag = false;
                        break;
                    }
                }

                if (flag)
                    cnt++;
            }

            res = Math.max(res,cnt);

            // visited = false;
            for (int i = 0; i < select.length; i++) {
                alphabet[select[i] - 'a'] = false;
            }
            return ;
        }

        for (int i = start; i < list.size(); i++) {
            select[depth] = list.get(i);
            combi(i+1,depth+1,select);
        }
    }
}