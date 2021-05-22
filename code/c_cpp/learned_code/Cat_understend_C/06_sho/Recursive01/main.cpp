//関数の再帰呼出し
//いっちゃん(小松ふう)簡単な例
//カウントアップ(最大10)を再帰呼出しで実装する.

#include <stdio.h>

int main(){
	static int i = 0;

	if ( i <= 10){
		printf ("i = %d\n", i);
		i++;
		main();//再帰呼出し
	}

	return 0;
}
