#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

unsigned short temp = 0;
int main () {
   char str[80];
   char buff[20];

   unsigned short data  = 0b00001010;

   printf(buff);
   for(int x = 0; x < 8; x++){       
        temp = 128 & data;
        sprintf(buff, "%d", temp>>7);       
        //printf(buff);
        strcat(str, buff);
        //printf("%s\n", s1);
        data <<= 1;
   }
   
   printf(str);
   
   return(0);
}