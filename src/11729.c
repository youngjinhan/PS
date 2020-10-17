#include <stdio.h>
#pragma warning(disable:4996)
//미완성
int n;
#define MAX 25
int stack1[MAX] , stack2[MAX], stack3[MAX];
int top1, top2, top3;

int hanoi(int n) {

    if (n == 1) {
       
        return 1;
    }
    else
    {
        return hanoi(n - 1) * 2 + 1;
    }
}


int main()
{
    int result;
    scanf("%d", &n);

    result = hanoi(n);
    printf("%d\n", result);
    printf("%d %d", list[0][0], list[0][1]);
    /*for (int i = 0; i < n; i++) {
        printf("%d %d\n", list[i][0], list[i][1]);
    }*/



    return 0;
}
