#include <stdio.h>

void sequentialSearch(int a[], int n, int key)
{
	int i = 0;
	printf("\n %d를 검색하여라! -> ", key);
	while (i < n && a[i] != key)
		i++;
	if (i < n)
		printf("%d번째에 검색 성공!\n\n", i + 1);
	else
		printf("%d번째에 검색 실패!\n\n", i + 1);
}

void main()
{
	int a[] = { 8,30,1,9,19,2 };
	int n = 7;

	sequentialSearch(a, n, 9);
	sequentialSearch(a, n, 6);
}