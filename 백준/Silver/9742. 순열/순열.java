import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	static char[] data_arr, temp;
	static boolean[] isUsed;
	static int order, now;
	static String res;
	static String input;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		
			while ((input=br.readLine()) !=null) {
				StringBuilder sb = new StringBuilder();

				st = new StringTokenizer(input);

				// EOF 처리 어케함?
				// 1. input == null
				// 2. input.equals(null)
				// 3. Arrays.deepEquals(input, null)

				String data = st.nextToken();
				order = Integer.parseInt(st.nextToken());

				data_arr = data.toCharArray();
				temp = new char[data.length()];
				isUsed = new boolean[data.length()];
				now = 0;
				res = "";

				// factorial
				int maxPer = 1;
				for (int i = data.length(); i >= 1; i--)
					maxPer *= i;

				sb.append(data).append(" ").append(order).append(" ").append("=").append(" ");

				if (maxPer < order)
					System.out.println(sb.append("No permutation").toString());
				else {
					permutation(0);
					System.out.println(sb.append(res).toString());
				}
			}
		

	}

	private static void permutation(int cnt) {
		if (cnt == data_arr.length) {
			now++;
			if (now == order) {
				for (int i = 0; i < temp.length; i++)
					res += temp[i];
			}
			return;

		}

		for (int i = 0; i < data_arr.length; i++) {
			if (isUsed[i])
				continue;

			isUsed[i] = true;
			temp[cnt] = data_arr[i];
			permutation(cnt + 1);
			isUsed[i] = false;

		}

	}

}
