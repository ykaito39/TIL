#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

int main(int argc, char* argv[]){
	FILE *fp;
	char buf[256];

	fp = fopen (*argv[1], "r");

	if(argc != 2 && fp == NULL){
		printf ("error\n");
		exit (1);
	}
	
	while(1)
		fprintf(*fp, 
	
	fclose (*fp);
