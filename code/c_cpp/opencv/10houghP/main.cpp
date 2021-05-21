#include <iostream>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/core/core.hpp>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>

//#include <cv.h>
//#include <highgui.h>
using namespace std;
using namespace cv;

int main(int argc, char * argv[]){
	if (argc <= 1)
		return -1;

	//Read img
	VideoCapture cap(0);
	
	while(1){
		Mat frame;
		cap >> frame;
		
		//canny
		Mat canny_img;
		Canny (frame, canny_img, 200, 50);
		
		//はふ変換
		vector<Vec4i> lines_p;
		Vec4i pt;
		HoughLinesP(canny_img, lines_p, 1, CV_PI/180, 60, 40, 5);
		Mat tmp_img = frame.clone();
		for (auto it = lines_p.begin(); it != lines_p.end(); ++it){
			pt = *it;
			line(tmp_img, Point(pt[0], pt[1]), Point(pt[2], pt[3]),
				Scalar(0, 255, 255), 2, CV_AA);
		}
	
		//ですぷれい
		namedWindow ("original", CV_WINDOW_AUTOSIZE);
		imshow("original", frame);
		namedWindow ("canny", CV_WINDOW_AUTOSIZE);
		imshow("canny", canny_img);
		namedWindow ("hough", CV_WINDOW_AUTOSIZE);
		imshow("hough", tmp_img);
	
		if (waitKey(5) == 'q')
			break;
		}

		return 0;
}
