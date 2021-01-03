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
