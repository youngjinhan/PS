#include <stdio.h>

int main()
{
	int div[50], num, min, max;
	scanf("%d", &num);
	for (int i = 0; i < num; i++)
		scanf("%d", &div[i]);

	min = max = div[0];
	for (int i = 1; i < num; i++)
	{
		if (div[i] > max)
			max = div[i];
		else if (div[i] < min)
			min = div[i];
	}

	printf("%d", min * max);
	
	return 0;
}
