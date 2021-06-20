/*
정수 N을 소인수분해하기.
첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.
N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.

ex1.
input
72

output
2
2
2
3
3

ex2.
input
3

output
3

ex3.
input
6

output
2
3

ex4.
input
9991

output
97
103

*/

#include <stdio.h>

int main()
{
	int N;
	scanf("%d", &N);
	while (N != 1)
	{
		for (int i = 2; i <= N; i++)
		{
			if (N % i == 0)
			{
				printf("%d\n", i);
				N /= i;
				break;
			}
		}
	}
	
	return 0;
}
