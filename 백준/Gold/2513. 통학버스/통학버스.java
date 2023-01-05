import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class Main {
    static int n, k, s; 

    static class Location implements Comparable<Location>{
        int locate;
        int student;

        public Location(int locate, int student) {
            this.locate = locate;
            this.student = student;
        }


        @Override
        public int compareTo(Location o) {
            return o.locate - this.locate;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        n = Integer.parseInt(input[0]);
        k = Integer.parseInt(input[1]);
        s = Integer.parseInt(input[2]);
        PriorityQueue<Location> leftSide = new PriorityQueue<>();
        PriorityQueue<Location> rightSide = new PriorityQueue<>();

        for (int i = 0; i < n; i++) {
            input = br.readLine().split(" ");
            int dist = Integer.parseInt(input[0]);
            int student = Integer.parseInt(input[1]);
            if (dist < s) {
                leftSide.offer(new Location(s - dist, student));
            } else {
                rightSide.offer(new Location(dist - s, student));
            }
        }

        int result = 0;
        result += busMoveTime(leftSide);
        result += busMoveTime(rightSide);
        System.out.println(result);
    }

    public static int busMoveTime(PriorityQueue<Location> pq) {
        int move = 0;
        while (!pq.isEmpty()) {
            Location now = pq.poll();
            int cnt = now.student / k; 
            if (now.student % k > 0) {
                cnt++;
            }
            int temp_stu = k * cnt - now.student; 
            while (!pq.isEmpty()) {
                Location next = pq.poll();
                if (next.student <= temp_stu) {
                    temp_stu -= next.student;
                } else {
                    next.student -= temp_stu;
                    pq.offer(next);
                    break;
                }
            }
            move += (2 * cnt * now.locate);
        }
        return move;
    }
}