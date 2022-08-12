import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.PriorityQueue;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		PriorityQueue<Integer> fuel = new PriorityQueue<>(Collections.reverseOrder());

		int n = Integer.parseInt(br.readLine());
		int res = 0;

		int[] gas_station = new int[1000001];

		for (int i = 0; i < n; i++) {
			String[] input = br.readLine().split(" ");
			gas_station[Integer.parseInt(input[0])] = Integer.parseInt(input[1]);
		}
		String[] input = br.readLine().split(" ");
		int L = Integer.parseInt(input[0]);
		int P = Integer.parseInt(input[1]);

		for (int i = 0, j = 0; i < L; i++, P--) {
			if (gas_station[i] != 0)
				fuel.add(gas_station[i]);

			try {
				if (P == 0) {
					P += fuel.poll();
					res++;
				}
			} catch (Exception e) {
				System.out.println(-1);
				return;
			}
		}

		System.out.println(res);

	}

}
