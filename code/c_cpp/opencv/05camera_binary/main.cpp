/************************************************************                              
 * Convert CapturedVideo to grayscale                                                                             
 * Used Lib: OpenCV                                                                        
 * Write for C                                                                             
 * Author:Kaito Izumi                                                                      
 ************************************************************/ 
#include "cv.h"
#include "highgui.h"

CvCapture *capture;
IplImage *frameImage;
IplImage *gray;
IplImage *binary;

void OnTrackber(int val){
	cvThreshold(gray, binary, val, 255, CV_THRESH_BINARY);
	cvShowImage(windowNameCapture, binary);
}

int main(){
	int key;

	int levels = 128;
	
	char windowNameCapture[] = "Capture";
	if((capture = cvCreateCameraCapture(0)) == NULL){
		printf ("Can/'t open Camera.\n");
		key = cvWaitKey(10);
	}
	
	//Create window & trackbar
	cvNamedWindow(windowNameCapture, CV_WINDOW_AUTOSIZE);
	cvCreateTrackbar("Trackber1", windowNameCapture, levels, 255, OnTrackber);

	while(1){
		frameImage = cvQueryFrame(capture);
		
		//conv to gray
		gray = cvCreateImage(cvGetSize(frameImage), IPL_DEPTH_8U, 1);
		cvCvtColor(frameImage, gray, CV_BGR2GRAY);
		
		//conv to binary
		binary = cvCreateImage(cvGetSize(gray), IPL_DEPTH_8U, 1);
//		cvThreshold(gray, binary, levels, 255, CV_THRESH_BINARY);

		cvShowImage(windowNameCapture, binary);
//		cvCreateTrackbar("Trackber1", windowNameCapture, levels, 255, OnTrackber);
		key = cvWaitKey(10);

		if(key == 'q'){
			break;
		}
	}

	cvReleaseCapture(&capture);
	cvDestroyWindow(windowNameCapture);

	return 0;
}
