/* 正方形の半分(直角三角形)を作るプログラム
 * 制約:標準出力はcout << "#"とcout << "\n"しか使えない
 *
 * 解決手順として,次のようにコーディングしていくと良い.
 * 		横1列に#を5つ出力する
 * 		5x5に#を出力する
 * 		コレを改良する
 */ 
#include <iostream>
using std::cout;
using std::cin;

int main(){
	for(int k = 0; k < 5; k++){
		for(int i = 0; i < 5-k; i++){
			cout << "#";
		}
		cout << "\n";
	}
	return 0;
}
