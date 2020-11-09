#include <stdio.h>


int Count[10001];
int max=0;


int main() {
	int N, i, tmp;
	scanf("%d", &N);

	for (i = 0; i < N; i++)
	{
		scanf("%d", &tmp);
		if (max < tmp) max = tmp;
		Count[tmp]++;
	}

	for (int i = 1; i <= max; i++)
	{

		
		while (Count[i]-- != 0)
		{
			printf("%d\n", i);
		}
			
	}


	return 0;
}
