/* N개의 숫자가 공백없이 입력됐을때 숫자의 합을 출력
첫째줄에 숫자의 개수 N, 그 다음줄 부터 숫자 N개가 공백없이 입력

ex1.
input
1
1

output
1

ex2.
input
5
54321

output
15

ex3.
input
25
7000000000000000000000000

output
7
*/

#include <stdio.h>
#include <stdlib.h>
#pragma warning(disable:4996)



int main()
{
    char* string;
    int i, N, tmp, sum = 0;

    scanf("%d", &N);
    string = (char*)malloc(sizeof(char) * N);
    
    scanf("%s", string);
   

    for (i = 0; i < N; i++)
    {
        tmp = string[i] - '0';
        sum += tmp;
    }
    printf("\n");
    printf("%d", sum);

    return 0;

}
