/************************************************************                              
 * VideoCapture & hough                                                                           
 * Used Lib: OpenCV                                                                        
 * Write for C++                                                                             
 * Author:Kaito Izumi                                                                      
 * Tasks:Fix! can't move!!!
 ************************************************************/ 
#include <iostream>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>

using namespace std;
using namespace cv;

int main(int argc, char * argv[]){
	VideoCapture cap(0);
	
	while(1){
		Mat frame;
		cap >> frame;
		
		//canny
		Mat canny_img;
		Canny (frame, canny_img, 200, 50);
		
		//はふ変換
		vector<Vec2f> lines;
		HoughLines (canny_img, lines, 1, CV_PI/360, atoi(argv[1]));
		float rho, theta, ct, st;
		int z = canny_img.cols;
		Mat tmp_img = frame.clone();
		for (auto it = lines.begin(); it != lines.end(); ++it){
			rho = (*it)[0];
			theta = (*it)[1];
			ct = cos(theta);
			st = sin(theta);
			line(tmp_img, Point(rho*ct - z*st, rho*st + z*ct),
				  Point(rho*ct + z*st, rho*st - z*ct), Scalar(0, 255, 255));
		}

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
