#include <ncurses.h>

void ncInit(){
	initscr();	//スクリーン表示開始
	noecho();	//入力文字を非表示
	keypad(stdscr, TRUE); 	//矢印使用可能に
	cbreak();	//バッファ非使用
	timeout(0);	//キー待ち時間

	//色設定
	start_color();
	init_pair(1, COLOR_GREEN, COLOR_BLACK);	//1
}

void run(){
	char c;
	int x = 10;
	int y = 10;
	int beem = 0;//1で表示
	int beem_x;
	int beem_y;
	
	//qが入力されるまでループ
	while((c=getch()) != 'q'){
		erase();
		mvaddstr(3, 19, "orz");	//指定位置に文字列を表示
		mvaddch(y, x, 'A');		//指定位置に文字を表示
		if(beem == 1){
			mvaddch(beem_y, beem_x, 'o');
			
		}
	
		//移動
		if(c == 'h'){	//左
			x--;
/*		}else if(c == 'j'){ //下
			y--;
		}else if(c == 'k'){ //上
			y++;
*/		}else if(c == 'l'){ //右
			x++;
		}else if(c == 'g'){	//弾
			beem_x = x;
			beem_y = y-1;
			beem = 1;
		}
		refresh();
	}
}
int main(){
	ncInit();//初期化&設定
	
	bkgd(COLOR_PAIR(1));

	run();

	endwin();	//スクリーン表示終わり
	return 0;
}
