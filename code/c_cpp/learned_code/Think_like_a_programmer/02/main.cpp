/* カウントダウンとカウントアップ
 * 欲しい数字(5,4,3,2,1)と,出力された値の差を観測し,
 * 差を埋める式を導出する
 */ 
#include <iostream>
using std::cout;
using std::cin;

int main(){
	for(int row = 1; row <= 5; row++){
		cout << 6-row << '\n';//カウントダウン. -rowでは差が常に6になるため,6-rowにする.
	}
	for(int row = 1; row <= 5; row++){
		cout << row << '\n';//カウントアップ
	}
	return 0;
}
