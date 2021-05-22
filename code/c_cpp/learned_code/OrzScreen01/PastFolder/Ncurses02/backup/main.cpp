/*
 * orzが画面の右から左へ流れてゆくプログラム?
 */


#include <stdio.h>
#include <stdlib.h>
#include <ncurses.h>
#include <unistd.h>
#include <time.h>

void ncInit(){
	initscr();	//スクリーン表示開始
	noecho();	//入力文字を非表示
	keypad(stdscr, TRUE); 	//矢印使用可能に
	cbreak();	//バッファ非使用
	timeout(0);	//キー待ち時間
	curs_set(0);
	
	//色設定
	start_color();
	init_pair(1, COLOR_GREEN, COLOR_BLACK);	//1
	init_pair(2, COLOR_WHITE, COLOR_GREEN);	//2
	//bkgd(COLOR_PAIR(1));//色設定1を反映
}

void run(){
	int h, w;
	getmaxyx(stdscr, h, w);//ターミナルの初期大きさ
	int y = 10;
	int x = w-3;

	while(getch() != 'q'){
		erase();
		//色1でorzを描画
		attrset(COLOR_PAIR(1));
		mvaddstr(y, x, "orz");
		//色2でExi...を描画
		attrset(COLOR_PAIR(2));
		mvaddstr(h-1, 0, "Exit \'q\'\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t");
		
		refresh();
		
		usleep(50000);
		x--;
	}
}

int main(){
	ncInit();//初期化&設定

	run();

	endwin();	//スクリーン表示終わり
	return 0;
}
