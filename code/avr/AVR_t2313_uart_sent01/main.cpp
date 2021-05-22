/***********************************************************************
 * Mon Jan 12 19:45
 * Created by ykaito39
 * filename AVR_t2313_uart_sent01/main.cpp
 *
 * 目的:			t2313間でのuart通信を確認する
 * 動作内容:		スイッチが押されたらデータを送信する.
 * 				スイッチは3つ使い,送信内容を変える.
 * 対応プログラム: AVR_t2313_uart_receive01/main.cpp
 * スイッチ:		PB0, PB1, PB2
 * 送信用データ:	PB0 ->	data_a (0b00000001)
 * 				PB1 ->	data_b (0b00000010)
 * 				PB2 ->	data_c (0b00000011)
 * 設定条件:		9600bit/sec, ansync, non parity, 1bit stop,
 * 				8bit-flame , receiver&transmitter enable, 倍速許可
 *
 * 動作順:		IO初期化 -> uart初期化
 * 				-> ループ開始
 *					PB0,PB1,PB2のどれが押されているか判断
 *						PB0の場合 -> data_aを送信
 *						PB1の場合 -> data_bを送信
 *						PB2の場合 -> data_cを送信
 *						どちらも押されていない場合 -> 0x00を送信(LEDが消える)
 **********************************************************************/

/****************************************************
 * ボーレートの計算(レジスタUBRRH,UBRRLに代入する値の導出)
 * 		F_CPU/使用したいボーレート値/非同期(=8)か同期(=16)か
 * 		F_CPU/9600/8
 * まあ,AVRデータシートの表読めばいい.
 ***************************************************/

#define F_CPU 8000000UL
#include <avr/io.h>

//IO初期化--------------------------------------------
void Init_io(){
	DDRB	=	0x00;	//PBを入力設定
	PINB 	=	0xff;	//PBをプルアップ
}

//uart初期化------------------------------------------
void Init_uart(){
	unsigned int rate = (F_CPU/9600/8)-1;	//ボーレート導出(12bit)
	UBRRH	|= rate >> 8;					//ボーレート上位レジスタに代入(8bit右シフトで上位4bitが得られる)
	UBRRL	|= rate;						//ボーレート下位レジスタに代入
	UCSRC	|= _BV(UCSZ1)|_BV(UCSZ0);		//ansync, non parity, 1bit stop, 8bit-flame
	UCSRB	|= _BV(RXEN)|_BV(TXEN);			//receiver&transmitter enable
	UCSRA	|= _BV(U2X);					//倍速許可
}

//データ送信関数--------------------------------------
void Sent_data(char data){
	while(bit_is_clear(UCSRA,UDRE));//送信完了待機, while( !( UCSRA & 0b00100000 ))と同義
	UDR	= data;						//送信データ格納,送信
}

//main-----------------------------------------------
int main(){
	Init_io();
	Init_uart();

	//送信用データ
	char data_a = 0b00000001;//PB0が押された時に送信するデータ
	char data_b = 0b00000010;//PB1が押された時に送信するデータ
	char data_c = 0b00000011;//PB2が以下略

	//Start main loop
	while(1){
		if(bit_is_set(PINB,0)){
			//data_aの送信
			Sent_data(data_a);
		}else if(bit_is_set(PINB,1)){
			//data_bの送信
			Sent_data(data_b);
		}else if(bit_is_set(PINB,2)){
			//data_cの送信
			Sent_data(data_c);
		}else{
			//受信側のレジスタをクリア
			Sent_data(0x00);
		}
	}//End main loop
}
