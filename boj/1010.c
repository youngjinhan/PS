/*
강의 서쪽에는 N개의 사이트가 있고 동쪽에는 M개의 사이트가 있을 때 N개 다리를 지으려고 한다. (N ≤ M)
다리끼리는 서로 겹쳐질 수 없다고 할 때 다리를 지을 수 있는 경우의 수를 구한다.
입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 그 다음 줄부터 각각의 테스트케이스에 대해 강의 서쪽과 동쪽에 있는 사이트의 개수 정수 N, M (0 < N ≤ M < 30)이 주어진다.
각 테스트 케이스에 대해 주어진 조건하에 다리를 지을 수 있는 경우의 수를 출력한다.

ex.
input
3
2 2
1 5
13 29

output
1
5
67863915
*/

#include <stdio.h>

int d[1004][1004];
int result[100000];

int main()
{
	
	int T, N, M;
	d[0][0] = 1;
	d[0][1] = 0;
	scanf("%d", &T);
	for (int k = 1; k <= T; k++)
	{
		scanf("%d %d", &N, &M);

		for (int i = 1; i <= M; i++)
		{
			for (int j = 0; j <= i; j++)
			{
				d[i][j] = d[i - 1][j] + d[i - 1][j - 1];
			}
		}

		result[k] = d[M][N];
	}
	
	for (int i = 1; i <= T; i++)
		printf("%d\n", result[i]);
	

	return 0;
}
