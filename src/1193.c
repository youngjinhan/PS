#include <stdio.h>

int main()
{
	int X;
	scanf("%d", &X);
	for (int i = 1;; i++)
	{
		if (X <= i)
		{
			int tmp = X;
			int right = i;
			for (int j = 1; j <= i; j++)
			{
				
				
				if (!--tmp)
				{
					if (i % 2 == 0)
					{
						printf("%d/%d", j, right);
						break;
					}
					else
					{
						printf("%d/%d", right,j);
						break;
					}
					
				}
				right--;
			}
			
			break;
			
		}
		X -= i;
	}
	
	return 0;
}
