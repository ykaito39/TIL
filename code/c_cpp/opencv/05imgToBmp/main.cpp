#include <iostream>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/core/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>

using namespace std;
using namespace cv;

/* 静止画像の表示ウインドウ名を変更せよ */
void Kadai2(Mat img){
	namedWindow("Kadai1");
	imshow("Kadai1", img);
}

/* 静止画像を2つのウィンドウで表示せよ */
/* チャームポイント1:引数maxによって表示するウインドウの数を変更できるようにしたよ! */
/* チャームポイント2:ウインドウの名前は表示回数ごとに変化するよ! */
void Kadai3(Mat img, int max){
	for(int i=0; i < max; i++){
		char win[50];
		sprintf(win, "Kadai2_window%d", i+1);
		namedWindow(win);
		imshow(win, img);
	}
}

/* グレイ変換画像を表示せよ */
Mat Kadai4(Mat img){
	Mat gray;
	cvtColor(img, gray, CV_BGR2GRAY);
	namedWindow("Kadai4_gray");
	imshow("Kadai4_gray", gray);

	return gray;
}

/* グレイ変換画像をlena_gray.bmpとして保存せよ */
void Kadai5(Mat gray){
	imwrite("lena_gray.bmp", gray);
}

/* 2値化画像を表示せよ */
void Kadai6(Mat gray, int levels){
	Mat binary;
	threshold(gray, binary, levels, 255, CV_THRESH_BINARY);
	namedWindow("binary");
	imshow("binary", binary);
}

/* 2値化する際に使用した変数levelsについて説明せよ */
void Kadai7(){
	cout << "変数「levels」について" << endl;
	cout << "・・・はレポート本文に記す。" << endl;
}

/* gray, binary以外の処理画像を表示せよ */
void Kadai8(Mat img){
	Mat hsv;
	cvtColor(img, hsv, CV_BGR2HSV);
	namedWindow("Kadai8_hsv");
	imshow("Kadai8_hsv", hsv);
}

/* cameraからの入力を表示するウインドウの名前を変更せよ */
/* ウインドウを複製し、片方は2値化処理を施して表示せよ */
/* 2値化された画像をキー入力"s"によって保存できるようにせよ。 保存ファイル名は"camera_binary.bmp"とする。 */
int Kadai9_10_11(int levels){
	VideoCapture cap(0);
	if(!cap.isOpened()){
		cout << "can not open." << endl;
		return -1;
	}

	while(1){
		Mat frame;
		cap >> frame;

		Mat binary;
		cvtColor(frame, binary, CV_BGR2GRAY);
		threshold(binary, binary, levels, 255, CV_THRESH_BINARY);

		namedWindow("cap_frame");
		imshow("cap_frame", frame);

		namedWindow("binary2");
		imshow("binary2", binary);

		char key = waitKey(1);
		if(key == 's')
			imwrite("camera_binary.bmp", binary);
		else if(key == 'q')
			break;
	}

	return 0;
}
	

int main(int argc, char** argv){
	if(argc < 2)
		return -1;

	Mat src = imread(argv[1], 1);

//	Kadai2(src);
	Kadai3(src, atoi(argv[2]));
/*	Mat gray = Kadai4(src);
	Kadai5(gray);
	Kadai6(gray, 128);
	Kadai7();
	Kadai8(src);
	Kadai9_10_11(128);
*/
/*	const string base = "./file.bmp";
	Mat img = imread(argv[1] ,1);
	Mat gray;

	cvtColor(img, gray, CV_BGR2GRAY);
	imwrite(base, gray);

	namedWindow("ponzu");	//課題2
	imshow("ponzu", img);

	namedWindow("gray");
	imshow("gray", gray);
*/
	waitKey(0);

	return 0;
}
