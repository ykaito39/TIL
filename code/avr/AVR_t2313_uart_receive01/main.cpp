/***********************************************************************
 * Mon Jan 12 17:52
 * Created by ykaito39
 * filename AVR_t2313_uart_receive01/main.cpp
 *
 * 目的:			t2313間でのuart通信を確認する
 * 動作内容:		割り込みを使用せずに,データの受信を行う.
 * 対応プログラム: AVR_t2313_uart_sent01/main.cpp
 * LED:			PB0, PB1, PB2
 * 受信データ:	0b00000001
 * 				0b00000010
 * 				0b00000011の3パターン
 * 設定条件:		9600bit/sec, ansync, non parity, 1bit stop,
 * 				8bit-flame , receiver&transmitter enable, 倍速許可
 *
 * 動作順:		IO設定 -> uart初期化
 * 				-> ループ開始
 *					受信したデータは何??
 *						0b00000001 -> PB0をHigh
 *						0b00000010 -> PB1をHigh
 *						0b00000011 -> PB2をHigh
 **********************************************************************/

/****************************************************
 * ボーレートの計算(レジスタUBRRH,UBRRLに代入する値の導出)
 * 		F_CPU/使用したいボーレート値/非同期(=8)か同期(=16)か
 * 		F_CPU/9600/8
 * まあ,AVRデータシートの表読めばいい.
 ***************************************************/

#define F_CPU 8000000UL
#include <avr/io.h>

//IO初期化-----------------------------------------------
void Init_io(){
	DDRB 	|= 0xff;	//PBを出力設定
}

//uart初期化-----------------------------------------------
void Init_uart(){
	unsigned int rate = (F_CPU/9600/8)-1;	//ボーレート導出
	UBRRH	|= rate >> 8;					//ボーレート上位レジスタに代入
	UBRRL	|= rate;						//ボーレート下位レジスタに代入
	UCSRC	|= _BV(UCSZ1)|_BV(UCSZ0);		//ansync, non parity, 1bit stop, 8bit-flame
	UCSRB	|= _BV(RXEN)|_BV(TXEN);			//receiver&transmitter enable
	UCSRA	|= _BV(U2X);					//倍速許可
}

//データ受信------------------------------------------------
char Reseive_uart(){
	while(bit_is_clear(UCSRA,RXC));	//受信終了待機, while( !( UCSRA & 0b10000000 ))と同義
	return UDR;						//受信データ格納
}

//main----------------------------------------------------
int main(){
	Init_io();
	Init_uart();

	//Start main loop
	while(1){
		char value = Reseive_uart();//送られてきたデータ

		if(value == 0b00000001){
			PORTB = _BV(0);
		}else if(value == 0b00000010){
			PORTB = _BV(1);
		}else if(value == 0b00000011){
			PORTB = _BV(2);
		}else{
			PORTB = 0x00;
		}
	}//End main loop
}
