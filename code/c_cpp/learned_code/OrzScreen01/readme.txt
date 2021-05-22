erase();//前の文字を消す

refresh();//描画

上のように画面が更新されるっぽいので,以下の方法はキビシイ.
		//ｺﾚﾂｶｴﾅｲ
		for(int i=0; i < h-1; i++){
			attrset(COLOR_PAIR(1));
			mvaddstr(y[i], x[i], "orz");
		}
		
		//ｺｺﾂｶｴﾙ
		//すべてのx座標の値を一つ減らす(左に動かす)
		for(int i=0; i < (sizeof(x)/sizeof(x[0])); i++){
			x[i]--;
		}
		
		//待ち&描画
		usleep(50000);
		refresh();
	}

なので,
