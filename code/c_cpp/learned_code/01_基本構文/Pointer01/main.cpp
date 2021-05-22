#include <iostream>

int main(){
	int buf = 0;
	int *p_test;

	p_test = &buf;

	std::cout << *p_test << '\n';

	return 0;
}
