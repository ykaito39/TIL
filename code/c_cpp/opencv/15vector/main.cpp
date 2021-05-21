#include <iostream>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>

#define CAP_W	640
#define CAP_H	480

using namespace std;
using namespace cv;

int main(int argc, char* argv[]){
	VideoCapture cap(0);
	cap.set(CV_CAP_PROP_FRAME_WIDTH,  CAP_W);
	cap.set(CV_CAP_PROP_FRAME_HEIGHT, CAP_H);
	if(!cap.isOpened()){
		printf("cant open camera.\n");
		return -1;
	}

	while(1){
		Mat frame;
		cap >> frame;
		Mat frame_tmp = frame.clone();
		Mat frame_tmp_binary;
		//binary
		threshold(frame, frame_tmp_binary, 100, 255, THRESH_BINARY);
		
		//screen
		namedWindow("hoge", CV_WINDOW_AUTOSIZE);
		imshow("hoge", frame_tmp);
		namedWindow("binary");
		imshow("binary", frame_tmp_binary);

		//debug
		char key = waitKey(5);
		if(key == 's'){
			cout << "Total: "    << frame_tmp.total() << endl;
			cout << "channels: " << frame_tmp.channels() << endl;
			cout << frame_tmp_binary << endl;
		}if(key == 'q')
			break;
	}

	return 0;
}
