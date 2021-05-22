#include <avr/io.h>

int main(){
	DDRB = 0xff;//OUTPUT
	DDRC = 0x00;//INPUT
	PINC = 0xff;//INPUT

	while(1){
		if(bit_is_set(PINC,5)){
			PORTB |= 0xff;
		}else{
			PORTB &= ~0xff;
		}
	}

	return 0;
}
