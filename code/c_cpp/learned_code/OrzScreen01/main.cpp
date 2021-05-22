/*
 * orzが画面の右から左へ流れてゆくプログラム?
 */

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

int main(){
	ncInit();//初期化&設定
	
	//----get screen size----
	int h, w;
	getmaxyx(stdscr, h, w);

	int y[h], x[h];
	int random_val;//orzの出現位置を決定する.将来的に乱数を採用.
	
	//----配列初期化(x,yの初期位置を決定)----
	//sizeof(array)/sizeof(array[うんぬん]で,配列の要素数を求める
	for(int i=0; i < (sizeof(x)/sizeof(x[0])); i++){
		y[i] = h-2-i;
		x[i] = w-3;
	}
	
	//----main----
	while(getch() != 'q'){
		erase();

		//第0〜第h-1までのorzを描画
		for(int i=0; i < h-1; i++){
			attrset(COLOR_PAIR(1));
			mvaddstr(y[i], x[i], "orz");
		}

		//下のバーを描画
		attrset(COLOR_PAIR(2));
		mvaddstr(h-1, 0, "Exit \'q\'\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t");


		//すべてのx座標の値を一つ減らす(左に動かす)
		for(int i=0; i < (sizeof(x)/sizeof(x[0])); i++){
			x[i]--;
		}
		
		//待ち&描画
		usleep(50000);
		refresh();
	}


	endwin();	//スクリーン表示終わり
	return 0;
}
