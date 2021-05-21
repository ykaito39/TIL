/************************************************************
 * Screen pic
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

	//display
	cvNamedWindow("pic", CV_WINDOW_AUTOSIZE);
	cvShowImage("pic", img);
	
	cvWaitKey(0);//wait for Infinity keyInput

	//destoroy
	cvDestroyWindow("lena");
	cvReleaseImage(&img);

	return 0;
}
