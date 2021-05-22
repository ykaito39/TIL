#include <iostream>

int main(){
	int value;
	int *pvalue;
	pvalue = &value;

	std::cout << "適当な数字を入力してください >> ";
	std::cin >> value;
	std::cout << "変数valueに" << value << "が代入されました." << '\n';
	std::cout << "変数valueのアドレスは" << pvalue << "です" << '\n';
	std::cout << "変数valueを指し示しているポインタはpvalueです." << '\n';
	std::cout << "*pvalueの値は" << *pvalue << "です." << '\n';
}
