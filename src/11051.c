/*
자연수 N과 정수 K가 주어졌을 때 이항 계수 구하기
첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 0 ≤ K ≤ N)
(이항계수 결과%10007)를 출력한다.

ex.
input
5 2

output
10
*/

#include <stdio.h>

int d[1004][1004];

int main()
{
	
	int N, K;
	d[0][0] = 1;
	d[0][1] = 0;
	scanf("%d %d", &N, &K);

	for (int i = 1; i <= N; i++)
	{
		for (int j = 0; j <= i; j++)
		{
			d[i][j] = (d[i - 1][j] + d[i - 1][j - 1]) % 10007;
		}
	}
	
	printf("%d", d[N][K]);

	return 0;
}
