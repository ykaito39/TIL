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
	init_pair(1, COLOR_GREEN, COLOR_BLACK);	//1
	init_pair(2, COLOR_WHITE, COLOR_GREEN);	//2
	//bkgd(COLOR_PAIR(1));//色設定1を反映
}

//----描画関数----
void draw(int *h, int *y, int *x){
	//色1でorzを描画
	attrset(COLOR_PAIR(1));
	mvaddstr(*y, *x, "orz");
	//色2でExi...を描画
	attrset(COLOR_PAIR(2));
	mvaddstr(*h-1, 0, "Exit \'q\'\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t");
	}

//----メインループ----
void mainRun(){
	int h, w;				//ターミナルの初期縦横値
	getmaxyx(stdscr, h, w);	//ターミナルの初期大きさ
	int y[h],x[h];			//個別にorzの位置を格納する
	
	//----配列初期化----
	//sizeof(array)/sizeof(array[うんぬん]で,配列の要素数を求める
	for(int i=0; i < (sizeof(x)/sizeof(x[0])); i++){
		y[i] = h-2-i;
		x[i] = w-3;
	}
	
	//int i_x = 0;

	while(getch() != 'q'){
		for(int i=0; i < (h-1); i++){
		//	erase();				//こいつのせいで...こいつのせいでｯ!!!!!! -> 描画状態を保存する関数でもどうです?
			draw(&h, &y[i], &x[i]);	//すべてのorzを描画
			refresh();				
		}
		for(int i=0; i < (sizeof(x)/sizeof(x[0])); i++){
			x[i]--;//左方向へ動かす
		}
		
		usleep(10000);
	}
}

int main(){
	ncInit();//初期化&設定

	mainRun();

	endwin();	//スクリーン表示終わり
	return 0;
}
