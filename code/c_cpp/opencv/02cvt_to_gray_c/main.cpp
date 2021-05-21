/************************************************************                              
 * Convert to grayscale                                                                             
 * Used Lib: OpenCV                                                                        
 * Write for C                                                                             
 * Author:Kaito Izumi                                                                      
 ************************************************************/ 
#include "cv.h"
#include "highgui.h"

int main(int argc, char* argv[]){
	//file open--------------------------------------
	IplImage* img;
	IplImage* gray;

	if(argc <= 1){
		printf("can\'t open file.\npless command [./main FILENAME]\n");
		return -1;
	}

	img = cvLoadImage(argv[1], CV_LOAD_IMAGE_COLOR);

	//convert/---------------------------------------
	gray = cvCreateImage(cvGetSize(img), IPL_DEPTH_8U, 1);	//imgの大きさで、ビット深度8の画像?
	cvCvtColor(img, gray, CV_BGR2GRAY);						//img -> 白黒に変換 -> grayに格納

	//screen-----------------------------------------
	cvNamedWindow("lena_gray", CV_WINDOW_AUTOSIZE);
	cvShowImage("lena_gray", gray);

	cvWaitKey(0);
	
	//destroy----------------------------------------
	cvDestroyWindow("lena_gray");
	cvReleaseImage(&img);

	return 0;
}
