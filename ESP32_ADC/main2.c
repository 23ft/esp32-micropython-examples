#include <string.h>
#include <stdio.h>


int main (void)
{
 char buffer[256];
 char * s1, * s2;
 strcpy(buffer, "Start of line");
 s1 = buffer;
 s2 = "... end of linejshduiasgduiasgduyasgduiasgiod";
 strcat(buffer, s2);
 printf("Length = %d\n", strlen(buffer));
 printf("string = \"%s\"\n", buffer);
}