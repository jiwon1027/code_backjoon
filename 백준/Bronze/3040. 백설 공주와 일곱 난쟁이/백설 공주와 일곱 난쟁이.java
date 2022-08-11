import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
	static List<Integer> list;
	static int total;
	
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		
		list = new ArrayList<>();
		
		for (int i = 0; i < 9; i++) {
			int temp =sc.nextInt();
			list.add(temp);
			total += temp;
		}
		
		fun();
		
		for(int x:list)
			System.out.println(x);
		
		
		
		
	}
	
	public static void fun() {

		for (int i = 0; i < 8; i++) {
			for (int j = i+1; j < 9; j++) {
				if (total - list.get(i) - list.get(j) == 100) {					
					list.remove(list.get(j));
					list.remove(list.get(i));
					return;
				}
			}
		}
		
	}

}
