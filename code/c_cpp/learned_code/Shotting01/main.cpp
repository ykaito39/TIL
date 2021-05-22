#include <stdio.h>
#include <stdlib.h>
#include <ncurses.h>
#include <unistd.h>
#include <time.h>

//----初期設定----
void ncInit(){
	//ncurses init
	initscr();				//スクリーン表示開始
	noecho();				//入力文字を非表示
	keypad(stdscr, TRUE); 	//矢印使用可能に
	cbreak();				//バッファ非使用
	timeout(0);				//キー待ち時間
	curs_set(0);			//カーソル非表示
	
	//色設定
	start_color();
	init_pair(1, COLOR_GREEN, COLOR_BLACK);	//基本色
	init_pair(2, COLOR_WHITE, COLOR_GREEN);	//下部バー用
}

//----Gun action function----
/*void gun(int m_y, int m_x){
	attrset(COLOR_PAIR(1));
	mvaddstr(m_y-1, m_x, "i");
}*/

//----main loop function----
void run(){
	int h, w;
	getmaxyx(stdscr, h, w);
	
	//----位置変数(敵機,自機)----
	int e_y = h/2,
		e_x = w/2;
	int m_y = h/2+5,
		m_x = w/2;
	
	//----初期位置----
	attrset(COLOR_PAIR(1));
	mvaddstr(h/2, w/2, "o");//エネミー
	mvaddstr((h/2)+5, w/2, "Y");//自機

	//----main loop----
	while(true){
		int key = getch();
		if(key == 'q') break;

		//int gun_i = m_y;
		
		//----描画----
		//erase();
		attrset(COLOR_PAIR(1));
		mvaddstr(e_y, e_x, "o");//エネミー
		mvaddstr(m_y, m_x, "Y");//自機
		//mvaddstr(gun_i, m_x, "i");//機銃
		attrset(COLOR_PAIR(2));
		mvaddstr(h-1, 0, "Exit \'q\' Gun \'g\'\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t");//下部タブ
		refresh();

		//キー入力による分岐 -> 移動 or 発射
		switch(key){
			case KEY_UP:	m_y--;	break;
			case KEY_DOWN:	m_y++;	break;
			case KEY_LEFT:	m_x--;	break;
			case KEY_RIGHT: m_x++;	break;
			case 'g':
				int i=m_y-1;
				attrset(COLOR_PAIR(1));
				mvaddstr(i, m_x, "i");
				break;
		}
		//エネミーと自機の接触判定
		if((m_y == e_y)&&(m_x == e_x)){
			break;
		}
		//エネミーと機銃の接触判定
		if((i_y == e_y)&&(i_x == e_x)){
		}
	}
}

int main(){
	ncInit();	//初期化&設定
	run();		//メインループ
	endwin();	//スクリーン表示終わり
	return 0;
}
