//sumsumするプログラム
//通常,変数は関数がreturnされると開放される.(寿命)
//そのため記憶クラス演算子 "static" を使い,プログラムが終了するまで値を保持させる.
//また,staticは最初の１回だけ初期化される.

#include <stdio.h>

int Add(int value){
	static int total = 0;
	total += value;
	return total;
}

int main(){
	int sum;
	
	sum = Add(20);//20
	printf ("%d\n", sum);
	
	sum = Add(40);//60
	printf ("%d\n", sum);

	sum = Add(100);//160
	printf ("%d\n", sum);

	return 0;
}
