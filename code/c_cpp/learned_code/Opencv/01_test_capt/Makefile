#参考:http://qiita.com/wkentaro/items/3a770726deb8fa1f214a

#compile tool
CC = g++

#option etc...
CFLAGS 		= -Wall -O2 `pkg-config opencv --cflags` `pkg-config opencv --libs`
LDLIBES 	= -lm -opencv
INCLUDES 	= -I/usr/include/opencv

#commandow!
main:main.cpp
	$(CC) $< $(LDLIBES) $(CFLAGS) $(INCLUDES) -o $@
