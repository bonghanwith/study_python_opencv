#ifdef _CH_
#pragma package <opencv>
#endif

#include "opencv\cv.h"
#include "opencv\highgui.h"

// Load the source image. HighGUI use.
IplImage *image = 0, *gray = 0;
int x, y;

int main( int argc, char** argv )
{
    char* filename = argc == 2 ? argv[1] : (char*)"fruits.jpg";
    
    if( (image = cvLoadImage( filename, 1)) == 0 )
        return -1;
 
    printf("New Image width %d image height %d channels %d \n", 
            image->width, image->height, image->nChannels);
    // Convert to grayscale
    gray = cvCreateImage(cvSize(image->width, image->height), IPL_DEPTH_8U, 1);
    cvCvtColor(image, gray, CV_BGR2GRAY);
    // draw a red line in colour image
    for (y = 0; y < image->height; y++) {
        x = y;
        ((uchar*)(image->imageData + image->widthStep*y))[x*3] = 0;
         ((uchar*)(image->imageData + image->widthStep*y))[x*3+1] = 0;
        ((uchar*)(image->imageData + image->widthStep*y))[x*3+2] = 255;
   }
    // draw a white line in black white image
    for (y = 0; y < image->height; y++) {
        x = y;
        ((uchar*)(gray->imageData + gray->widthStep*y))[x] = 255;
    }

    // Create windows.
    cvNamedWindow("Source", 1);
    cvNamedWindow("Result", 1);

    // Show the images.
    cvShowImage("Source", image);
    cvShowImage("Result", gray);
    
    // Wait for a key stroke
    cvWaitKey(0);
    cvReleaseImage(&image);
    cvReleaseImage(&gray);
 
    cvDestroyWindow("Source");
    cvDestroyWindow("Result");

    return 0;
}