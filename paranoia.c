$ date +%s ; nc 20.80.240.190 1234
1717798993
32 26 143 198 58 200 185 61 177 125 53 173 83 215 213 116 6 254 18 219 212 117 35 183 96 52 44 26 52 226 24 245 49 83 58 31 

/// obtain the seed with the stuff here very important
 
 
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
 
char flag[] = {32, 26, 143, 198, 58, 200, 185, 61, 177, 125, 53, 173, 83, 215, 213, 116, 6, 254, 18, 219, 212, 117, 35, 183, 96, 52, 44, 26, 52, 226, 24, 245, 49, 83, 58, 31};
#define flag_len (sizeof(flag)/sizeof(*flag))
#define SEED 1717798993
 
 
int brute_flag() {
    unsigned int var_5;
    int var_4;
    long i;
    srand(SEED);
 
    for (i = 0; i <= flag_len; i++) {
        var_4 = rand();
        var_5 = var_4 >> 31 >> 24;
        for (int j = 0; j < 256; j++) {
            char result = (char)((char)var_4 + var_5) - var_5 ^ (char)j; //(int)flag[i];
            if (result == flag[i])
                printf("%c", j);
        }
    }
    putchar(10);
    return 0;
}
 // you only bruteforce 255 vals instead of millions
int main(void) {
    brute_flag();
    return 0;
}

//akasec{n0t_t00_m4ny_br41nc3lls_l3ft} 
// XD #FR33P4L3S71N3&G4Z4 
 
