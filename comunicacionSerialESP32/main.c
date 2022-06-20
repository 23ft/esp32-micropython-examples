#include <stdio.h>

char sum();
short int rest(char sig);
unsigned char product(char bcd);

short int xd, value;

unsigned int A = 7;
unsigned int B = 7;

void main(void){
    printf("result: %d\n", product(1));
}

char sum(){
    return 0xFF;
}

unsigned char product(char bcd){
    value = 0;
    value = A*B;
    printf("value: %d\n", value);

    if(bcd){
        if (value <= 99){
            unsigned char mask = 0x00; 
            char d = 0, u = 0;
            u = value % 10;
            d = ((value % 100)-u) / 10;

            printf("value u: %d\n value d: %d\n", u, d);            
            
            mask |= d;
            mask <<= 4;
            mask |= u;
            printf("mask: %d\n", mask);
            return mask;
            
        }
        else{
            return 0x00;
        }
                
    }
    else{
        
        return value;
    }
    
    
}

short int rest(char sig) {
    if(sig) {
        value = 0;
        value = A - B;
        
        if (value < 0){
            value *= -1;
            
            value |= 0x80;
            printf("%d\n", value);
        }
    }
    else{
        value = 0;
        printf("A: %d B: %d\n", A, B);
        value = A-B;
        
    }
    return value;
}