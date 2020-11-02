#include <stdio.h>
#pragma warning(disable:4996)


int main()
{
	int tmp[1000], N;
	scanf("%d", &N);

	for (int i = 0; i < N; i++)
	{
		scanf("%d", &tmp[i]);
	}

	for (int i = 0; i < N - 1; i++)
	{
		for (int j = i + 1; j < N; j++)
		{
			if (tmp[i] > tmp[j])
			{
				tmp[i] = tmp[i] ^ tmp[j];
				tmp[j] = tmp[i] ^ tmp[j];
				tmp[i] = tmp[i] ^ tmp[j];
			}
		}
	}


	for (int i = 0; i < N; i++)
	{
		printf("%d\n", tmp[i]);
	}
}
