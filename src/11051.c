/*

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
