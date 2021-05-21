/************************************************************                              
 * VideoCapture & canny                                                                           
 * Used Lib: OpenCV                                                                        
 * Write for C++                                                                             
 * Author:Kaito Izumi                                                                      
 ************************************************************/ 
#include <iostream>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>

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
		
		//ノイズ対策?
		Mat noise_removal_img;
		GaussianBlur(frame, noise_removal_img, Size(7, 7), 0);

		//canny
		Mat canny_img;
		Canny (noise_removal_img, canny_img, 30, 100);

		//ですぷれい
		namedWindow ("canny", CV_WINDOW_AUTOSIZE);
		imshow("canny", canny_img);

		char key = waitKey(10);
		if (key == 'q')
			break;
		
	}
	
	return 0;
}
