#include <stdio.h>
#include <stdlib.h>			
#include <string.h>       

void DelSpace(char* buf){
	//--------空白とタブを消す
	int i = 0;
	while (buf[i] != '\0'){						//文字列の終端に達するまでループ
        if (buf[i] == ' '||buf[i] == '\t'){		//カーソル位置(i文字目)の文字が' 'か'\t'のとき
            int j;								
	        for (j = i; buf[j] != '\0'; j++){		//終端文字にぶち当たるまで繰り返す
	        buf[j] = buf[j+1];					//右ッかわの文字をカーソル位置に持ってくる
            }									
         }else{									//その他
			i++;									//カウンタ変数iをインクリメント
		}
	}
	//--------空行を消す
	if (buf[0] == '\n')
		buf[0] = '\0';
}

int main(int argc, char* argv[]){
	FILE *fp;
	char buf[256];
	int count = 0;
	
	fp = fopen(argv[1], "r");

	if (fp == NULL){
		printf ("ファイル名を引数に指定してください.\n");
		exit(-1);
	}

	while(fgets(buf, 256, fp) != NULL){
		DelSpace (buf);
		if (buf[0] != '\0')//スパゲッティやないですかぁ!!!!!
			printf("%04d: %s", ++count, buf);
	}

	fclose(fp);
	return 0;
}
