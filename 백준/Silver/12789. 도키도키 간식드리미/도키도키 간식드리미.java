import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws  IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		int n = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());

		Queue<Integer> data = new LinkedList<>();

		for (int i = 0; i < n; i++) {
			data.add(Integer.parseInt(st.nextToken()));
		}
		
		int std = 1;
		Stack<Integer> stack = new Stack<>();

		while(!data.isEmpty()) {
			if (data.peek() == std) {
				data.poll();
				std++;
			}
			else if(!stack.isEmpty() && stack.peek() == std) {
				stack.pop();
				std++;
			}
			else {
				stack.push(data.poll());
			}
			//System.out.println(data.toString());
			//System.out.println(stack.toString());
		}
		
		while(!stack.isEmpty()) {
			if(stack.peek() == std) {
				stack.pop();
				std++;
			}
			else {
				System.out.println("Sad");
				return;
			}
		}
		System.out.println("Nice");



		

	}

}
