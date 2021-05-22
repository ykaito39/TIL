#include <iostream>
#include <string>

struct bin{
	int price;
	std::string name;
};

int main(){
	bin test;
	test.price = 10;
	test.name = "Beaf";

	std::cout << test.name << "\'s price is " << test.price << '\n';

	return 0;
}
