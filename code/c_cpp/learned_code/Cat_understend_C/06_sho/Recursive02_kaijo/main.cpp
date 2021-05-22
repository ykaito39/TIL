//関数の再帰呼出し
//階乗を求める.
//階乗 n! = n * n-1 * n-2 ... 2 * 1

#include <stdio.h>

int Kaijo(int n){
	if (n == 0)	//0! = 1
		return 1;
	else		//kaijo-
		return n*Kaijo(n-1);
}

int main(){
	int i = 0;
	
	printf ("n! = ");
	printf ("%d\n", Kaijo(5));

	return 0;
}
