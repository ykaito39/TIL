//円の半径を入力 -> 円の面積を求める

#include <stdio.h>

#define PI 3.14

int main(){
	double radius;
	scanf ("%lf",&radius);

	double volume = radius*radius*PI;

	printf ("%f\n", volume);

	return 0;
}
