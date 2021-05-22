#include <ncurses.h>

int main(){
	initscr();	//端末制御開始

	start_color();	//カラーの設定
	init_pair(1, COLOR_RED, COLOR_BLUE);
	bkgd(COLOR_PAIR(1));

	erase();
	move(10, 20);
	addstr("hello, world");
	refresh();

	timeout(-1);
	getch();

	endwin();	//端末制御終わり
	return 0;
}
