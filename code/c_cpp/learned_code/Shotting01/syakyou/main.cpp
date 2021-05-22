#include <stdio.h>
#include <stdlib.h>
#include <ncurses.h>
#include <unistd.h>

#define FPS (1000/60)

void setting(){
	noecho();
	cbreak();
	curs_set(0);
	keypad(stdscr, TRUE);
	timeout(0);
}

void run(){
	int c;
	int a_x = 10;
	int a_y = 10;
	
	int beamDelay = 0;
	int beam = 0;//beam == 1で画面にbeamを表示
	int beam_x = 0, beam_y = 0;
	int delay;
	int wait = 9000;
	
	clock_t time, pre_time;
	pre_time = 0;

	while((c=getch()) != 'q'){
		erase();
		time = 0;

		switch(c){
			case KEY_UP:	a_y--;	break;
			case KEY_DOWN:	a_y++;	break;
			case KEY_LEFT:	a_x--;	break;
			case KEY_RIGHT:	a_x++;	break;
			case ' ':
				if(beam == 0){//beamは一度に一つしか描画できないっぽい
					beam_x = a_x;
					beam_y = a_y;
					beep();
					beam = 1;
				}
				break;
		}
		
		if((double)(time - pre_time) >= FPS){
			erase();
		}if((delay % wait) == 0){
			beam_y--;
			if(beam_y < 0){//画面の端に行ったら消す
				beam = 0;
			}
		}if(beam == 1){
			mvaddstr(beam_y, beam_x, "i");
		}

		mvaddstr(3, 9, "orz");
		mvaddstr(a_y, a_x, "A");
		move(LINES-1, COLS-1);

		delay++;

		refresh();//描画
	}
}

int main(){
	initscr();
	setting();
	
	run();

	endwin();
	return 0;
}
