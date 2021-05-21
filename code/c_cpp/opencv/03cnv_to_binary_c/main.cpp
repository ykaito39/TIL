/************************************************************                              
 * conv to binary                                                                             
 * Used Lib: OpenCV                                                                        
 * Write for C                                                                             
 * Author:Kaito Izumi                                                                      
 ************************************************************/ 
#include "cv.h"
#include "highgui.h"

int main(int argc, char* argv[]){
	int levels = 128;
	//file open--------------------------------------
	IplImage* img;
	IplImage* gray;
	IplImage* binary;

	if(argc <= 1){
		printf("can\'t open file.\npless command [./main FILENAME]\n");
		return -1;
	}
	
	img = cvLoadImage(argv[1], CV_LOAD_IMAGE_COLOR);

	//convert to gray
	gray = cvCreateImage(cvGetSize(img), IPL_DEPTH_8U, 1);
	cvCvtColor(img, gray, CV_BGR2GRAY);

	//convert to binary
	binary = cvCreateImage(cvGetSize(gray), IPL_DEPTH_8U, 1);
	cvThreshold(gray, binary, levels, 255, CV_THRESH_BINARY);

	//show image
	cvNamedWindow("lena_binary", CV_WINDOW_AUTOSIZE);
	cvShowImage("lena_binary",binary);

	cvWaitKey(0);

	cvDestroyWindow("lena_binary");
	cvReleaseImage(&img);

	return 0;
}
