﻿#include <stdio.h>

void sequentialSortSearch(int a[], int n, int key)
{
	int i = 0;
	printf("\n %d를 검색하여라! ->", key);
	while (a[i] < key)
		i++;
	if (a[i] == key)
		printf("%d번째에 검색 성공!\n\n", i + 1);
	else
		printf("%d번째에 검색 실패! \n\n", i + 1);
}

void main()
{
	int a[] = { 1, 2, 8, 9, 11, 19, 29 };
	int n = 7;

	sequentialSortSearch(a, n, 9);
	sequentialSortSearch(a, n, 6);
}