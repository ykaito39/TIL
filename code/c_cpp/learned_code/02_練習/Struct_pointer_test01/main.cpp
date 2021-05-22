#include <iostream>

struct TEST{
	int value1;
	int value2;
	char name;
};

int main(){
	TEST test;
	TEST *ptest;
	
	//ptestにtestのアドレスを代入
	ptest = &test;

	//アロー演算子でアクセス
	ptest -> value1	 = 100;
	ptest -> value2	 = 50;
	ptest -> name	 = 'A';

	std::cout << ptest -> value1 <<'\n';
	std::cout << ptest -> value2 <<'\n';
	std::cout << ptest -> name   <<'\n';

}
