#include <stdio.h>

int main(int argc, char* argv[]){
    FILE *file;
    file = fopen("test.txt","a");       //open the file 'test.txt'
    fprintf(file,"Hello,FileIO!\n");    //write
    fclose(file);

    return 0;
}
