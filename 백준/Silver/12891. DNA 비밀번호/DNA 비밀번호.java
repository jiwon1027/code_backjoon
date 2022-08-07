import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static String str;
	static int[] dna;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int s = Integer.parseInt(st.nextToken());
		int p = Integer.parseInt(st.nextToken());

		st = new StringTokenizer(br.readLine());
		str = st.nextToken();
		
		int[] data = new int[4];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < 4; i++) {
			data[i] = Integer.parseInt(st.nextToken());
		}
		
		dna = Arrays.copyOf(data, 4);
		int res = 0;

		// window_size : p
		// start_index는 0 ~ s-p가 되야함
		for (int i = 0; i <= s - p; i++) {

			if (i == 0) {
				for (int j = 0; j < p; j++) {
					minus(j);
				}
			}
			else {
				minus(i+p-1);
				plus(i-1);
			}
			
			res++;
			for (int idx = 0; idx < 4; idx++) {
				if(dna[idx]>0) {
					res--;
					break;
				}
			}
		}
		System.out.println(res);

	}
	
	public static void minus(int i) {
		if (str.charAt(i) == 'A')
			dna[0] -= 1;
		else if (str.charAt(i) == 'C')
			dna[1] -= 1;
		else if (str.charAt(i) == 'G')
			dna[2] -= 1;
		else if (str.charAt(i) == 'T')
			dna[3] -= 1;
	}
	
	public static void plus(int i) {
		if (str.charAt(i) == 'A')
			dna[0] += 1;
		else if (str.charAt(i) == 'C')
			dna[1] += 1;
		else if (str.charAt(i) == 'G')
			dna[2] += 1;
		else if (str.charAt(i) == 'T')
			dna[3] += 1;
	}

}
