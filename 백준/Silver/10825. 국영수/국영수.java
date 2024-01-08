
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.concurrent.atomic.AtomicReference;


/*

 * */


public class Main {

    public static class Person{
        String name;
        int kor;
        int math;
        int eng;

        public Person(String name, int kor, int eng, int math) {
            this.name = name;
            this.kor = kor;
            this.math = math;
            this.eng = eng;
        }

//        @Override
//        public int compareTo(Person o) {
//
//            // 국어점수가 같으면
//            if (this.kor == o.kor) {
//                // 영어점수도 같으면
//                if (this.eng == o.eng) {
//                    // 수학점수도 같다면
//                    if (this.math == o.math) {
//
//                        // 이름 사전순으로 출력
//                        return this.name.compareTo(o.name);
//                    }
//                    // 수학 감소하는 순
//                    return o.math - this.math;
//                }
//                // 영어 증가하는 순
//                return this.eng - o.eng;
//            }
//            // 국어 감소하는 순
//            return o.kor - this.kor;
//
//        }

    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        List<Person> list = new ArrayList<Person>();

        for (int i = 0; i < N; i++) {
            String[] input = br.readLine().split(" ");
            list.add(new Person(input[0], Integer.parseInt(input[1]), Integer.parseInt(input[2]), Integer.parseInt(input[3])));
        }

        Collections.sort(list, (o1, o2) -> {
            if (o1.kor == o2.kor) {
                if (o1.eng == o2.eng) {
                    if (o1.math == o2.math) {
                        return o1.name.compareTo(o2.name);
                    }
                    return o2.math - o1.math;
                }
                return o1.eng - o2.eng;
            }
            return o2.kor - o1.kor;
        });


        for (int i = 0; i < N; i++) {
            System.out.println(list.get(i).name);
        }


    }
}