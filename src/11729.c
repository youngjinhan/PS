#include <stdio.h>
#pragma warning(disable:4996)
//미완성
int n, * i, * j, * k, x, y, z,list[25][2];
*i = &x;
*j = &y;
*k = &z;

int hanoi(int n,int **list) {
   
    if (n == 1){
        *list[0] = 1;
        *list[1] = 3;
        return 1;
    }
    else
    {
        return hanoi(n - 1,list) * 2 + 1;
    }
}
        

int main()
{
    int result;
    scanf("%d", &n);

    result = hanoi(n, list);
    printf("%d\n", result);
    printf("%d %d", *list[0], *list[1]);
    /*for (int i = 0; i < n; i++) {
        printf("%d %d\n", list[i][0], list[i][1]);
    }*/

    

    return 0;
}
