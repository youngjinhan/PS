#include <stdio.h>

int main()
{
	int num[10001][2];
	
	for (int i = 0; i < 10000; i++)
	{
		scanf("%d %d", &num[i][0], &num[i][1]);
		if (num[i][0] == 0 && num[i][1] == 0)
			break;
	}
		
	for (int i = 0; i < 10000; i++)
	{
		if (num[i][0] == 0 && num[i][1] == 0)
			break;
		else
		{
			if (num[i][0] < num[i][1])
			{
				if (num[i][1] % num[i][0] == 0)
					printf("factor\n");
				else
					printf("neither\n");
			}

			else
			{
				if (num[i][0] % num[i][1] == 0)
					printf("multiple\n");
				else
					printf("neither\n");
			}
		}
	}
	
		
	
	return 0;
}
