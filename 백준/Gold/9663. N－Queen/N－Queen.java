import java.util.Scanner;

public class Main {
	static int n,res;
	static int[] cols;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		
		cols = new int[n+1];
		
		setQueen(1);
		System.out.println(res);
	}
	
	public static boolean isAvailable(int rowNo) {
		for (int i = 1; i < rowNo; i++) {
			if(cols[i] == cols[rowNo] || 
					rowNo-i == Math.abs(cols[rowNo]-cols[i]))
				return false;
		}
		return true;
	}
	
	public static void setQueen(int rowNo) {
		if(!isAvailable(rowNo-1))
			return;
		
		if (rowNo>n) {
			res++;
			return;
		}
		
		for (int i = 1; i <= n; i++) {
			cols[rowNo] = i;
			setQueen(rowNo+1);
		}
		
	}

}
