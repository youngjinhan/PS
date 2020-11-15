#include <stdio.h>

int result=0;
void swap(int a)
{
	int tmp = a / 100;
	a = (a % 10) * 100 + ((a / 10) % 10) * 10 + tmp;
	if (a > result)
		result = a;
}
int main()
{
	int n, m;
	scanf("%d %d", &n, &m);
	swap(n);
	swap(m);
	printf("%d", result);

	
	

	return 0;

}
