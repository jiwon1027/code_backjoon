#include <stdio.h>

int main(){
	float f;
	scanf("%f", &f);
	
	int i;
	i =(int)(f * 100) % 100;
	
	i = i>0 ? i : -i;
	
	printf("%d\n",i);
	
	return 0;
} 
