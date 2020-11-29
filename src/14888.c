#include <stdio.h>

int num[12], oper[5];
int N, sum, max=-1000000000, min=1000000000, count = 0;

void sol(int a)
{
	
	if (count == N-1)
	{
		if (sum > max)
			max = sum;
		if (sum < min)
			min = sum;
		

	}

	if (oper[0] == 0 && oper[1] == 0 && oper[2] == 0 && oper[3] == 0)
		return;

	for (int i = 0; i < 4; i++)
	{
		if (i == 0)  // 덧셈
		{
			sum = num[a] + num[a + 1];
			if (oper[i] > 0)  // 연산 가능 (사용하지 않은 덧셈 기호 남아 있을 때)
			{
				oper[i]--;
				int tmp = num[a + 1];
				num[a + 1] = sum;
				count++;
				sol(a + 1);
				count--;
				oper[i]++;
				num[a + 1] = tmp;
			}

			else // 연산 불가 (더 이상 해당 연산 기호 남아있지 않음)
			{
				continue;
			}
		}
			
		else if (i == 1)
		{
			sum = num[a] - num[a + 1];
			
			if (oper[i] > 0)  // 연산 가능 (사용하지 않은 덧셈 기호 남아 있을 때)
			{
				oper[i]--;
				int tmp = num[a + 1];
				num[a + 1] = sum;
				count++;
				sol(a + 1);
				count--;
				oper[i]++;
				num[a + 1] = tmp;
			}

			else // 연산 불가 (더 이상 해당 연산 기호 남아있지 않음)
			{

				continue;
			}
		}
			
		else if (i == 2)
		{
			sum = num[a] * num[a + 1];
			if (oper[i] > 0)  // 연산 가능 (사용하지 않은 덧셈 기호 남아 있을 때)
			{
				oper[i]--;
				int tmp = num[a + 1];
				num[a + 1] = sum;
				count++;
				sol(a + 1);
				count--;
				oper[i]++;
				num[a + 1] = tmp;
			}

			else // 연산 불가 (더 이상 해당 연산 기호 남아있지 않음)
			{
				continue;
			}
		}
			
		else
		{
			sum = num[a] / num[a + 1];
			if (oper[i] > 0)  // 연산 가능 (사용하지 않은 덧셈 기호 남아 있을 때)
			{
				oper[i]--;
				int tmp = num[a + 1];
				num[a + 1] = sum;
				count++;
				sol(a + 1);
				count--;
				oper[i]++;
				num[a + 1] = tmp;
			}

			else // 연산 불가 (더 이상 해당 연산 기호 남아있지 않음)
			{
				continue;
			}
		}
			
	}

	
	

}

int main()
{
	
	scanf("%d", &N);
	for (int i = 0; i < N; i++)
		scanf("%d", &num[i]);
	for (int i = 0; i < 4; i++)
		scanf(" %d", &oper[i]);
		
	sol(0);
	printf("%d\n%d\n", max, min);
	return 0;

}


