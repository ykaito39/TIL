#include <iostream>
#include <cv.h>
#include <highgui.h>

int main(int argc, char * argv[]){
	IplImage* src;
	char img_file[] = "../../src1.png";
	src = cvLoadImage(img_file, CV_LOAD_IMAGE_COLOR);
		
	// ポリライン近似
    CvMemStorage *polyStorage = cvCreateMemStorage(0);
    CvSeq *polys, *poly;
    
	IplImage* tmp;
	IplImage* dst;
	IplImage* point;
	IplImage* poli_imageData;
	IplImage* found;
	int i;

    tmp = cvCreateImage( cvGetSize(src), IPL_DEPTH_8U, 1);
    dst = cvCreateImage( cvGetSize(src), IPL_DEPTH_8U, 3);
    
    cvCvtColor( poli_imageData, tmp, CV_RGB2GRAY);
    cvCopy( poli_imageData, dst);
    
    //Contour生成
    found = cvFindContours( tmp, contStorage, &contours, sizeof( CvContour), CV_RETR_TREE, CV_CHAIN_APPROX_SIMPLE);
    
    // ポリライン近似
    polys = cvApproxPoly( contours, sizeof( CvContour), polyStorage, CV_POLY_APPROX_DP, 10, 10);
    
    //ポリライン近似した４点のデータを見て回る
    while( (poly = (CvSeq *)cvNextTreeNode( &polyIterator)) != NULL)
    {
        //４点の領域が1000（適当）以上のとき、その４点を描画
        if( ( abs(cvContourArea(poly, CV_WHOLE_SEQ) > 1000 ) ) )
            for( i = 0 ; i < poly -> total ; i++ )
            {
                point = *( CvPoint*)cvGetSeqElem( poly, i);
                cvCircle( dst, point, 3, VIRTEX_COLOR, -1);
                
            }
        
    }	
	
		//ですぷれい
		namedWindow ("pori", CV_WINDOW_AUTOSIZE);
		imshow("pori", point);
		namedWindow ("hough", CV_WINDOW_AUTOSIZE);
		imshow("hough", tmp_img);
	
		if (waitKey(5) == 'q')
			break;
		}

		return 0;
}
