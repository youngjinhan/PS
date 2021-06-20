#include <stdio.h>

int main()
{
	int max[10], min[10], k, cur_max=9, cur_min=0;
	char sign[12];

	scanf("%d", &k);
	for (int i = 0; i < k; i++)
		scanf(" %c", &sign[i]);

	int i = 0, count=0, sub=0;  
	// count: 현재 위치에서 '<'가 몇개 나오는지 개수
	// sub: '<'가 처음 나오는 위치에서 count 값. count 값이 변화하기 때문에 새 변수로 저장. '<'가 끝나는 순간 cur_max에서 빼주기 위해 설정. 

	while (1)
	{
		if (sign[i] == '>')
		{
			max[i] = cur_max--;
			if (sub)
			{
				cur_max -= sub;
				sub = 0;
			}
		}
		else if(sign[i]=='<')
		{
			if (count == 0)
			{
				int j = i;
				while (sign[j] == '<')
				{
					j++;
					count++;
				}
				
				sub = count;
				max[i] = cur_max - count;
				count--;
			}
			else
			{
				max[i] = cur_max - count;
				count--;
			}
			
		}
		else
		{
			max[i] = cur_max;
			break;
		}
		i++;
	}

	for (int i = 0; i <= k; i++)
		printf("%d", max[i]);
	printf("\n");

	int add=0;
	i = 0, count=0;
	while (1)
	{
		if (sign[i] == '<')
		{
			min[i] = cur_min++;
			if (add)
			{
				cur_min += add;
				add = 0;
			}
		}
		else if (sign[i] == '>')
		{
			if (count == 0)
			{
				int j = i;
				while (sign[j] == '>')
				{
					j++;
					count++;
				}
				add = count;
				min[i] = cur_min + count;
				count--;
			}
			else
			{
				min[i] = cur_min + count;
				count--;
			}

		}
		else
		{
			min[i] = cur_min;
			break;
		}
		i++;
	}
	for (int i = 0; i <= k; i++)
		printf("%d", min[i]);
	return 0;
}
