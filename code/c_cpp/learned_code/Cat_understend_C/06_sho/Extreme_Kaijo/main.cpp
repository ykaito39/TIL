//1!, 2!, .... 10!の値を表示するプログラム

#include <stdio.h>

int Kaijo(int n){
	if (n == 0)
		return 1;
	else 
		return n * Kaijo(n-1);
}

int main(){
	for (int i = 1; i <= 10; i++){
		printf ("%d! = %d\n", i, Kaijo(i));
	}

	return 0;
}
