#include <opencv/cv.h>
#include <opencv/highgui.h>

using namespace std;

int main(int argc, char** argv){
	if (argc != 2){
		cout << "Bad files\n";
		return -1;
	}

	IplImage* img;				//画像ポインタ
	char* imgfile = argv[1]; 	//読み込む画像のファイル名

	//画像の読み込み
	img = cvLoadImage(imgfile, CV_LOAD_IMAGE_COLOR);

	//画像の表示
	cvNamedWindow(imgfile, CV_WINDOW_AUTOSIZE);
	cvShowImage(imgfile, img);
	cvWaitKey(0);
	cvDestroyWindow(imgfile);

	//画像の開放
	cvReleaseImage(&img);

	return 0;
}
