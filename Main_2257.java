package pratice;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

public class Main_2257 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String data = br.readLine();
		
		Map<Character,Integer> dic = new HashMap<>();
		dic.put('H', 1);
		dic.put('C', 12);
		dic.put('O', 16);
		
		Stack stack = new Stack<>();
		
		for (int i = 0; i < data.length(); i++) {
			if (data.charAt(i) == '(')
				stack.push('(');
			
			else if (data.charAt(i) == ')') {
				int res = 0;
				while (true){
					char temp = (char)stack.pop();
					
					if (temp == '(')
						break;
					
					res += temp;
				}
			}
			else if (dic.containsKey(i))
				stack.push(dic.get(i));
			else 
				stack.set(stack.size()-1, (int)stack.get(stack.size()-1) * (int)data.charAt(i));	
				
			}
			System.out.println(stack.toString());
		}
		
		
		
	}


