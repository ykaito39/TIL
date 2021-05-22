#include <SDL/SDL.h>

int main(){
	SDL_Init(SDL_INIT_VIDEO);
	SDL_WM_SetCaption("hello, world",NULL);
	SDL_SetVideoMode(256, 256, 32, SDL_SWSURFACE);
	SDL_Event	ev;
	int			bExit = 0;

	while(bExit == 0){
		while(SDL_PollEvent(&ev)){
			if(ev.type == SDL_QUIT){
				bExit = 1;
				break;
			}
		}
		SDL_Delay(20);
	}
	SDL_Quit();

	return 0;
}
