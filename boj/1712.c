// 코딩의 난이도가 높지 않지만 머리로 계산해야 하는 문제

#include <stdio.h>

int main()
{
	int a, b, c;
	scanf("%d %d %d", &a, &b, &c);
	if (b >= c)
		printf("-1");
	else
		printf("%d\n", a / (c - b) + 1);
	
	return 0;
}
