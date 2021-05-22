#include <stdlib.h>
#include <stdio.h>
#include <string.h>

void UserInput(){
	//zailist.zaiの表示
	
	//入力受付
	printf ("材名 切り取る長さ 署名の形式で入力\n");
	printf (">> ");
	char zaiName[10], size[10], myName[10];
	scanf  ("%s %s %s", zaiName, size, myName);
	
	//材名が正常か判断

	//保存確認
	printf ("編集内容を保存します.宜しいですか?[y/n]\n");
	char c;
	scanf  ("%s", &c);
	
	if(c == 'y'){
		printf ("保存しました\n");
	}else if(c == 'n'){
		printf ("保存が保留されました.\n");
		printf ("とりあえず終了しときます.\n");
		exit(0);
	}
}
	
int main(int argc, char* argv[]){
	//----材の名前一覧----
	char zaiNameList[] = {"\
	-------------------------------------------------------------------\n\
	角管:\n\
	\tkaku9 kaku12 kaku15 kaku20t1.5 kaku20t2.0\n\
	\tkaku10x15 kaku12x25 kaku15x30\n\
	角柱:\n\
	\tniku10 niku10x15\n\
	アングル:\n\
	\tangle9 angle15 angle20t1.5 angle20t2.0\n\
	丸棒(Al):\n\
	\tcylinder6 cylinder8 cylinder10 cylinder12 cylinder15\n\
	\t pipe6-4 pipe6-5\n\
	丸棒(鉄):\n\
	\t Fcylinder6 Fcylinder8 Fcylinder10 Fcylinder12 Fcylinder15\n\
	-------------------------------------------------------------------\n"};

	//----引数が不正値ならエラーコード吐いて閉じる----
	if(argc != 1){
		if(argc != 4){
			printf ("引数が多すぎるか,引数の値が不正です.\n引数は(材名 切り取る長さ 署名)としてください\n");
			printf ("なお,材名には以下の文字が使用できます.\n%s",zaiNameList);
			exit(EXIT_FAILURE);
		}
	}
	if(argc == 1){//引数入力された時の処理

	
	//----ファイル関係初期化----
	FILE *fp;
	char filename[] = "zailist.zai";
	if ((fp = fopen(filename, "r+")) == NULL){
		fprintf(stderr, "%sのオープンに失敗しました.\n", filename);
		printf("zailist.zaiをcloneしてください.\n");
		exit(EXIT_FAILURE);
	}
	
	//----main loop----
	while(true){
		UserInput();//入力
		//ファイル出力
		//git pushの実装
	}
}
