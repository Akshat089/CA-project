#include <stdio.h>
#include <math.h>
int main() {
    int count = 0;
    int num, originalnum, finalno;
    num = 1634;
    originalnum = num;
    finalno = num;
    while (num != 0) {
        num = num / 10;
        count++;
    }
    int result = 0;
    while (originalnum != 0) {
        int x = originalnum % 10;
        int y = pow(x, count);
        result = result + y;
        originalnum = originalnum / 10;
    }
    int flag = 0;
    if (finalno - result == 0) {
        flag = 1;
    }
    else {
        flag = 0;
    } 
}