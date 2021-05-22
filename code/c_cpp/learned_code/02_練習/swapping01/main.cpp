#include <iostream>

void swap(int *a, int *b){
	int c;
	c = *a;
	*a = *b;
	*b = c;
}

int main(){
	int a = 1;
	int b = 4;

	swap(&a, &b);

	std::cout << a << '\n';
	std::cout << b << '\n';

	return 0;
}

