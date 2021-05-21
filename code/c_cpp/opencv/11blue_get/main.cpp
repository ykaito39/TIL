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
		
		
		//ですぷれい
		namedWindow ("canny", CV_WINDOW_AUTOSIZE);
		imshow("canny", canny_img);
		namedWindow ("hough", CV_WINDOW_AUTOSIZE);
		imshow("hough", tmp_img);
	
		if (waitKey(5) == 'q')
			break;
		}

		return 0;
}
