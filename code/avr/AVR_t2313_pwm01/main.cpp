/****************************************************
 * Sun Jan 11 12:01
 * Created by ykaito39
 * 目的:		pwmの実験.
 * 動作内容:	だんだん明るくなり,だんだん暗くなる,のループ
 * pwm出力:	OC0B(PD5)
 * 設定条件:	高速pwm, 1/8分周, タイマ初期値0,
 * 			タイマ最大値255, 初期デューティー比200
 *
 * fix:		Mon Jan 11 15:20	関数名の修正
 ***************************************************/
#define F_CPU 8000000UL
#include <avr/io.h>
#include <util/delay.h>

//pwm設定
void Init_pwm(){
	DDRD	= 0xff;		//1111 1111		pwm出力ピン,PD5
	TCCR0A	= 0x23;		//0010 0011		OCR0B出力,高速pwm(WGM00=1, WGM01=1)
	TCCR0B	= 0x0A;		//0000 1010		1/8分周,高速pwm(WGM02=1)
	TCNT0	= 0x00;		//0000 0000		タイマ0の初期値
	OCR0A	= 255;		//pwm最大値
	OCR0B	= 200;		//デューティー比
}

int main(){
	Init_pwm();
	while(1){
		while(OCR0B > 0)	{OCR0B -= 1;_delay_us(150);}//255 -> 0
		while(OCR0B < 255)	{OCR0B += 1;_delay_us(150);}//0 -> 255	のループ
	}
}
