/************************************************************                              
 * Serch Edge                                                                             
 * Used Lib: OpenCV                                                                        
 * Write for C++                                                                             
 * Author:Kaito Izumi                                                                      
 ************************************************************/ 
#include <iostream>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>

using namespace cv;
using namespace std;

int main(int argc, char* argv[]){
	//grayscaleで読み込む
		//cv::imread(string imgfile, num)
		//num == 0 -> gray
		//num == 1 -> color で読み取る
	if(argc <= 1){
		cout << "can\'t open file." << endl
			 << "Pless command [./main FILENAME]." << endl;
		return -1;
	}

	Mat srcImg = imread(argv[1], 0);
	if (!srcImg.data)
		return -1;

	//sobel:空間の1次微分で輪郭を抽出
	Mat tmpImg;	//一時的なファイル
	Mat sobelImg;	//変換後の画像

	Sobel(srcImg, tmpImg, CV_32F, 1, 1);
	convertScaleAbs(tmpImg, sobelImg, 1, 0);
	
	//laplacian
	Mat laplacianImg;
	Laplacian(srcImg, tmpImg, CV_32F, 3);
	convertScaleAbs(tmpImg, laplacianImg, 1, 0);

	//Canny
	Mat cannyImg;
	Canny(srcImg, cannyImg, 50, 200);
	
	//Display
	namedWindow("Sobeled Img");
	imshow("Sobeled Img", sobelImg);
	namedWindow("Laplacianed Img");
	imshow("Laplacianed Img", laplacianImg);
	namedWindow("Cannyed Img");
	imshow("Cannyed Img", cannyImg);


	waitKey(0);
	return 0;
}
