#include <iostream>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>

//#include <cv.h>
//#include <highgui.h>

using namespace cv;

int main(int argc, char * argv[]){
	//capture 
	//c言語的なのは型の関係で使えない気がする
	VideoCapture cap(0);
	cap.set(CV_CAP_PROP_FRAME_WIDTH, 640);
	cap.set(CV_CAP_PROP_FRAME_HEIGHT, 480);
	if(!cap.isOpened())
		return -1;

	while(1){
		Mat frame;
		Mat tmp;
		cap >> frame;	//frameにcapを読み取る。
						//capはうえのほうでなんか宣言している
	
		tmp = frame.clone();

		//juuzi
		line(tmp, Point(0, 240), Point(640, 240), Scalar(0, 0, 200), 2, 4);
		line(tmp, Point(320, 0), Point(320, 480), Scalar(0, 0, 200), 2, 4);
		circle(tmp, Point(320, 240), 200, Scalar(0, 200, 0), 2, 4);
		
		//ですぷれい
		namedWindow ("tmp", CV_WINDOW_AUTOSIZE);
		imshow("tmp", tmp);
//		namedWindow ("conved_cap", CV_WINDOW_AUTOSIZE);
//		imshow("conved_cap", noise_removal_img);

		char key = waitKey(10);
		if (key == 'q')
			break;
		else if (key == 's'){
			Mat shot_img = frame;
			namedWindow("shot", CV_WINDOW_AUTOSIZE);
			imshow("shot", shot_img);
		}
		
	}
	
	return 0;
}
