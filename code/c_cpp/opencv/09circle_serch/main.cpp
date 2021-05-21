#include <iostream>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>

//#include <cv.h>
//#include <highgui.h>

using namespace cv;

int main(int argc, char * argv[]){
	//capture 
	VideoCapture cap(0);
	cap.set(CV_CAP_PROP_FRAME_WIDTH, 640);
	cap.set(CV_CAP_PROP_FRAME_HEIGHT, 480);
	if(!cap.isOpened())
		return -1;

	while(1){
		Mat frame;
		cap >> frame;	//frameにcapを読み取る。
						//capはうえのほうでなんか宣言している
		
		//reverse
		Mat reversed_img;
		flip(frame, reversed_img, -1); //両方の軸で反転 
		
		//ノイズ対策?
		Mat noise_removal_img;
		GaussianBlur(reversed_img, noise_removal_img, Size(7, 7), 0);
		
		//gray
		Mat gray_img;
		cvtColor (reversed_img, gray_img, COLOR_RGB2GRAY);

		//ここで円を検出する
		Mat circles;
		HoughCircles (gray_img, circles, CV_HOUGH_GRADIENT, 2, 10, 160, 50, 10, 20);
	
		//円の描画
		Mat circle_img;
		fncDrwCircles (circles, circle_img);


		//ですぷれい
		namedWindow ("gray", CV_WINDOW_AUTOSIZE);
		imshow("canny", gray_img);
		namedWindow ("circles", CV_WINDOW_AUTOSIZE);
		imshow("circles", circle_img);

		char key = waitKey(10);
		if (key == 'q')
			break;
		
	}
	
	return 0;
}
