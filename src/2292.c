#include <stdio.h>

int main()
{
	int N,sub;
	scanf("%d", &N);
	sub = 1;
	for (int i = 1;; i++)
	{
		N -= sub;
		if (N <= 0)
		{
			printf("%d", i);
			break;
		}
		if (sub == 1)
			sub += 5;
		else
			sub += 6;
	}
}
