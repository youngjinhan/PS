#include <stdio.h>

int main()
{
	int out[1001], T;
	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		int a, b, mult;
		scanf("%d %d", &a, &b);
		mult = a * b;
		// a>=b 상태로 만듬
		if (b > a)
		{
			int tmp = b;
			b = a;
			a = tmp;
		}
		while (a % b != 0)
		{
			int tmp = a % b;
			a = b;
			b = tmp;
		}
		out[i] = mult / b;
		
	}

	for (int i = 0; i < T; i++)
		printf("%d\n", out[i]);
		
	return 0;
}
