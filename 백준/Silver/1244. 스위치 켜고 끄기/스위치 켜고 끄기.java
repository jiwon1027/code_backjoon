
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int n = Integer.parseInt(br.readLine());
		
		st = new StringTokenizer(br.readLine());
		int[] arr = new int[n];
		for (int i = 0; i < n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		int stu_n = Integer.parseInt(br.readLine());
		
		
		for (int i = 0; i < stu_n; i++) {
			String[] input = br.readLine().split(" ");
			int sex = Integer.parseInt(input[0]);
			int num = Integer.parseInt(input[1]);
			
			if (sex == 1) {//남자
				for (int j = 0; j < n; j++) {
					if ((j+1) % num == 0)
						arr[j] = arr[j] == 1 ? 0 : 1;

				}
			}
			else {//여자
				int size = Math.min(num, n-num+1);
				num -= 1;
				arr[num] = arr[num] == 1 ? 0 : 1;

				for (int j = 1; j < size; j++) {

					if (arr[num+j] == arr[num-j]) {
						arr[num+j] = arr[num+j] == 1 ? 0 : 1;
						arr[num-j] = arr[num-j] == 1 ? 0 : 1;
					}
					else
						break;
					
				}
				
			}

		}

		for (int i = 0; i < n; i++) {
			System.out.print(arr[i] + " ");
			if((i+1)%20==0)
				System.out.println();
		}
	}

}
