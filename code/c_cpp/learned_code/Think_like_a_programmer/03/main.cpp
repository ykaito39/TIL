/* 横倒しの三角形を作るプログラム
 * 制約:標準出力はcout << "#"とcout << "\n"しか使えない
 */ 
#include <iostream>
#include <stdlib.h>
using std::cout;
using std::cin;

int main(){
	for (int k=0; k < 7; k++){
		for (int i=0; i < 4-abs(3-k); i++){
			cout << "#";
		}
		cout << '\n';
	}
	return 0;
}
