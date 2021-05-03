// DP 문제인듯 하여 DP로 풀었으나 시간초과
// 재귀로 풀어서 시간초과 나는거였음.
// 재귀가 아닌 앞에서부터 결과를 저장해가는 DP로 품

#include <stdio.h>
int candy[1001][1001];

int main()
{
	
	int N, M;
	scanf("%d %d", &N, &M);
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			scanf("%d", &candy[i][j]);
		}
	}

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			if (i == 0 && j == 0)
				continue;
			if (i == 0)
				candy[i][j] += candy[i][j - 1];
			else if (j == 0)
				candy[i][j] += candy[i - 1][j];
			else
			{
				if (candy[i - 1][j] > candy[i][j - 1])
					candy[i][j] += candy[i - 1][j];
				else
					candy[i][j] += candy[i][j - 1];
			}
		}
	}
	printf("%d\n", candy[N - 1][M - 1]);

	return 0;
}
