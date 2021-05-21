CC = g++
CFLAGS = -Wall -O2 -I/usr/local/include/opencv -I/usr/local/include  
LDLIBES = -lm  -L/usr/local/lib -lopencv_shape -lopencv_stitching -lopencv_objdetect -lopencv_superres -lopencv_videostab -lopencv_calib3d -lopencv_features2d -lopencv_highgui -lopencv_videoio -lopencv_imgcodecs -lopencv_video -lopencv_photo -lopencv_ml -lopencv_imgproc -lopencv_flann -lopencv_core -lopencv_hal 
SRC = main.cpp
OUT = main

main: ${SRC}
	${CC} -o ${OUT} ${SRC} ${CFLAGS} ${LDLIBES}

#main: main.cpp
#	g++ -o main main.cpp 
#	'pkg-config --cflags opencv' 'pkg-config --libes opencv'
