/************************************************************                              
 * VideoCapture                                                                             
 * Used Lib: OpenCV                                                                        
 * Write for C                                                                             
 * Author:Kaito Izumi                                                                      
 ************************************************************/ 
#include "cv.h"
#include "highgui.h"

int main(){
	int key;

	CvCapture *capture;
	IplImage *frameImage;
	IplImage *gray;
	
	char windowNameCapture[] = "Capture";
	if((capture = cvCreateCameraCapture(0)) == NULL){
		printf ("Can/'t open Camera.\n");
		key = cvWaitKey(10);
	}

	cvNamedWindow(windowNameCapture, CV_WINDOW_AUTOSIZE);

	while(1){
		frameImage = cvQueryFrame(capture);
		
		gray = cvCreateImage(cvGetSize(frameImage), IPL_DEPTH_8U, 1);
		cvCvtColor(frameImage, gray, CV_BGR2GRAY);

		cvShowImage(windowNameCapture, gray);
		key = cvWaitKey(10);

		if(key == 'q'){
			break;
		}
	}

	cvReleaseCapture(&capture);
	cvDestroyWindow(windowNameCapture);

	return 0;
}
