import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		int n = Integer.parseInt(br.readLine());
		int std = Integer.parseInt(br.readLine());
		PriorityQueue<Integer> prior_queue = new PriorityQueue<>(Collections.reverseOrder());
		for (int i = 0; i < n - 1; i++) {
			prior_queue.add(Integer.parseInt(br.readLine()));
		}

		int res = 0;

		if (n != 1) {
			while (prior_queue.peek() >= std) {
				res++;
				std++;
				prior_queue.add(prior_queue.remove() - 1);

			}

		}
		System.out.println(res);

	}

}
