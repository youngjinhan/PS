/*
자연수 N과 정수 K가 주어졌을 때 이항 계수 구하기
첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 0 ≤ K ≤ N)
이항계수 결과를 출력한다.

ex.
input
5 2

output
10
*/

#include <stdio.h>

int main()
{
	int N, K, result, denom, nume;
	result = denom = nume = 1;
	scanf("%d %d", &N, &K);
	while (K != 0)
	{
		denom *= N;
		N--;
		nume *= K;
		K--;
	}
	result = denom / nume;

	printf("%d", result);
	return 0;
}
