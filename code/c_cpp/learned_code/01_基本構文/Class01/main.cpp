#include <iostream>

class TEST{
public:
	int figure;
	void calc(int temp){
		figure = temp;
		std::cout << temp << '\n';
	}				
};

int main(){
	TEST test;
	test.calc(10);

	return 0;
}
